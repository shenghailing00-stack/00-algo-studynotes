# 01 背包进阶：目标和与二维费用
- [1049.最后一块石头的重量II](https://leetcode.cn/problems/last-stone-weight-ii/description/)
  <img width="1280" height="1786" alt="39c97e6a38084575e57776620c369145" src="https://github.com/user-attachments/assets/12325c41-4733-41ff-af7b-976a4c814ed0" />

- [494.目标和](https://leetcode.cn/problems/target-sum/description/)
  - 核心是先把原问题转化为 01 背包问题。
  - 设数组元素总和为 sum，若给某些数加正号后的和为 left，加负号后的和为 right，则有 left - right = target、left + right = sum，联立可得 left = (target + sum) / 2。
  - 因此题目本质上变成：从数组中选出若干个数，使它们的和恰好等于 (target + sum) / 2，求一共有多少种选法。
  - 如果 abs(target) > sum 或者 target + sum 为奇数，则直接无解。
  - 动态规划中，可以定义 dp[j] 表示当前遍历到的数字中，凑成和 j 的方法数，初始化 dp[0] = 1，表示什么都不选时凑成 0 有 1 种方法。
  - 随后遍历数组中的每个数字，对于每个数字都按 01 背包的方式倒序遍历容量 j，更新 dp[j] += dp[j - nums[i]]，意思是当前凑成 j 的方法数，等于原来不选当前数字的方法数，加上选当前数字后由 j - nums[i] 转移来的方法数。
  - 最终 dp[bagSize] 就是答案

- [474.一和零](https://leetcode.cn/problems/ones-and-zeroes/description/)
  - 二维费用的 01 背包问题。
  - 每个字符串可以看成一个物品，其中该字符串中 0 的个数和 1 的个数分别对应两种“重量”，而每选择一个字符串，子集长度就增加 1，因此它的“价值”是 1。
  - 定义 dp[i][j] 表示在最多使用 i 个 0 和 j 个 1 的条件下，能够选出的字符串最大数量。
  - 对于每个字符串，先统计其中 0 和 1 的个数，然后倒序遍历两个容量维度，用状态转移方程 dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum] + 1) 更新结果，表示当前字符串选或不选取最大值。
  - 最终 dp[m][n] 就是答案。
  - <img width="1279" height="1766" alt="c9366f39eb535e43c59b5451fcede687" src="https://github.com/user-attachments/assets/8eeabdcf-2b58-4ec4-befd-1741ce173d3e" />
