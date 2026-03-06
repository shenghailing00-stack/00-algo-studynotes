# second day daily log
## 数组part02
### 滑动窗口
 - 不断的调节子序列的起始位置和终止位置，从而得出我们想要的结果（毛毛虫）
   - 右指针：扩大窗口（头）
   - 左指针：缩小窗口（尾）
   - 在这个“头伸尾缩”的过程中，毛毛虫的身体（窗口）会在数组上不断向右滑动
 - 确定：
   - 窗口内是什么
   - 如何移动窗口起始位置
   - 如何移动窗口结束位置
- 精妙之处在于根据当前子序列和大小的情况，不断调节子序列的起始位置。从而将O(n^2)暴力解法降为O(n)
- [209.长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/description/)——**毛毛虫**
  - 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
   ```python
   class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0           # 尾巴一开始在最左边
        current_sum = 0    # 毛毛虫肚子里食物的总和
        
        # 准备一个无限大的数字，用来记录历史最短长度。
        # (因为我们要找"最小"，所以初始值要设得无穷大)
        min_len = float('inf') 
        
        # 头开始往前吃（遍历整个数组）
        for right in range(len(nums)):
            current_sum += nums[right]  # 吃下当前数字
            
            # 只要吃饱了（总和 >= 目标值），尾巴就开始尝试收缩
            while current_sum >= target:
                # 记录一下当前吃饱时的身体长度，看看是不是比以前记录的更短
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                
                # 尾巴往前缩：把最左边的数字减掉，left 往右走一步
                current_sum -= nums[left]
                left += 1
                
        # 如果遍历完了，min_len 还是无限大，说明把整个数组全吃进去都没吃饱，返回 0
        if min_len == float('inf'):
            return 0
        else:
            return min_len
   ```
###循环不变量原则
- 左闭右闭/左闭右开
- [59.螺旋矩阵](https://leetcode.cn/problems/spiral-matrix-ii/description/)
  左闭右开：
  写死边界！写死边界！
  ```python
  class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 1. 准备一个全是 0 的 n x n 矩阵（二维数组）
        # 这里用了一个小小的列表推导式，避免了 Python 中二维数组的坑
        matrix = [[0] * n for _ in range(n)]
        
        start_x, start_y = 0, 0  # 每一圈的起点坐标
        loop = n // 2            # 总共需要转几圈
        mid = n // 2             # 矩阵正中心的位置（n为奇数时会用到）
        count = 1                # 我们要填进去的数字，从 1 开始
        offset = 1               # 用来控制每条边的长度（每转一圈，边长都会缩短）
        
        # 2. 开始转圈圈啦！
        for _ in range(loop):
            i = start_x
            j = start_y
            
            # 第一步：画上边（从左到右）
            # 规矩：左闭右开。一直画到 n - offset 的位置停下
            for j in range(start_y, n - offset):
                matrix[start_x][j] = count # 行固定，列在动
                count += 1
                
            # 第二步：画右边（从上到下）
            # 规矩：左闭右开。此时 j 刚好停在最右列
            for i in range(start_x, n - offset):
                matrix[i][n-offset] = count # 列固定，行在动
                count += 1
                
            # 第三步：画下边（从右到左）
            # 规矩：左闭右开。倒着走，步长为 -1。此时i停在最下行
            for j in range(n - offset, start_y, -1):
                matrix[n-offset][j] = count # 行固定，列在倒着动
                count += 1
                
            # 第四步：画左边（从下到上）
            # 规矩：左闭右开。此时 j 回到了起点列，i 倒着走
            for i in range(n - offset, start_x, -1):
                matrix[i][start_y] = count
                count += 1
                
            # 一圈完美画完！准备画下一圈（往内层缩）
            start_x += 1  # 起点往下挪一行
            start_y += 1  # 起点往右挪一列
            offset += 1   # 下一圈的边长要缩短，所以 offset 增加
            
        # 3. 如果 n 是奇数，补上正中心那个最孤单的数字
        if n % 2 != 0:
            matrix[mid][mid] = count
            
        return matrix
  ```
### 前缀和——计算区间和
- 想象你每天都在存钱，每天都记录存了多少钱。——另外准备一个本子，只记录“截止到今天，我总共有多少钱”
  - vec=[1,2,3,3,2,1]
  - prefix=[1,3,6,9,11,12,14](前缀和）
  - vec[2]-vec[5]=p[5]-p[1]
- **求任意区间 [a, b] 的和:区间和 = prefix[b] - prefix[a - 1]**
- [58.区间和](https://kamacoder.com/problempage.php?pid=1070)
   - 需要自己写 sys.stdin.read() 的 ACM 模式：
  ```python
  import sys

  def main():
    # 1. 接收输入：一次性读取屏幕上的所有输入内容，并按空格或回车切分成一个个词
    input_data = sys.stdin.read().split()
    
    # 如果什么都没输入，就直接结束
    if not input_data:
        return
        
    # 2. 第一个数字是数组的长度 n
    n = int(input_data[0])
    
    # 3. 构建前缀和数组（核心魔法！）
    prefix = [0] * n      # 提前准备好前缀和的空本子
    current_sum = 0       # 记录当前的累加和
    
    # 接下来的 n 个数字就是原数组的元素（索引从 1 到 n）
    for i in range(n):
        num = int(input_data[i + 1])
        current_sum += num
        prefix[i] = current_sum  # 记下截止到当前位置的总和
        
    # 4. 处理后面的区间查询 (a, b)
    # 查完了前面的 n 个数字，后面的就全是查询条件了
    idx = n + 1 
    
    # 只要还有数据，就一直两个两个地往外取 (a 和 b)
    while idx < len(input_data):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        
        # 5. 应用前缀和公式
        if a == 0:
            # 如果从第 0 个开始算，直接取 b 位置的前缀和
            print(prefix[b])
        else:
            # 否则，用 b 位置的前缀和 减去 a 前面那个位置的前缀和
            print(prefix[b] - prefix[a - 1])
            
        # 指针往后跳两格，准备处理下一对 a 和 b
        idx += 2

    # 这一句是 Python 脚本的标准运行入口，照着写就好啦
    if __name__ == "__main__":
        main()

  
