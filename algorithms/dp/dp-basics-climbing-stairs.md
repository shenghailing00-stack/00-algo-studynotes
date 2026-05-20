# 动态规划基础：递推与爬楼梯模型
- 理论基础
- ![a29f2548f43058a92fb3401d3751a5b9](https://github.com/user-attachments/assets/b81922cd-fffc-47d9-9e7e-d80691145701)

- [509.斐波那契数列](https://leetcode.cn/problems/fibonacci-number/description/)
  - 定义 dp[i] 为第 i 个斐波那契数。
  - 根据题意可得递推公式 dp[i] = dp[i - 1] + dp[i - 2]。
  - 初始化 dp[0] = 0，dp[1] = 1。
  - 由于当前状态依赖前两个状态，所以遍历顺序应从前往后。
  - 最后返回 dp[n] 即可。
  - 若进一步优化空间，由于每次只依赖前两个状态，因此可以只用两个变量进行滚动更新。
  - ![334487e408d3465d653f1bfc961744c3](https://github.com/user-attachments/assets/0f44f4ad-aaef-4b4a-8c55-69c3150d4acf)
 
- [70.爬楼梯](https://leetcode.cn/problems/climbing-stairs/description/)
  - 不考虑dp[0]如何初始化，只初始化dp[1] = 1，dp[2] = 2，然后从i = 3开始递推
  - ![7f91211df508b22c39002b39f42770c0](https://github.com/user-attachments/assets/c820b057-f875-40d3-9ac2-188221379b46)

- [746.使用最小的花费爬楼梯](https://leetcode.cn/problems/min-cost-climbing-stairs/description/)
  - 可以有两个途径得到dp[i]，一个是dp[i-1] 一个是dp[i-2]:一定是选最小的，所以dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
  -  “你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。” 也就是说 到达 第 0 个台阶是不花费的，但从 第0 个台阶 往上跳的话，需要花费 cost[0]:所以初始化 dp[0] = 0，dp[1] = 0
  -  从前到后遍历cost数组
  -  ![7da199db636a1ace1dfab67ef0030a62](https://github.com/user-attachments/assets/982458e8-8604-4069-a150-fd6826a7960f)
