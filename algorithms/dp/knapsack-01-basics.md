# 01 背包基础与分割等和子集
  - **二维**标准状态转移方程:dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i]);
    - 当前物品，要么不拿，继承上一行；要么拿，价值等于“上一行去掉它重量后的最优值 + 当前物品价值”；两者取最大
    - <img width="1280" height="1718" alt="29e55c62a7f2226108c34a37f7da09f0" src="https://github.com/user-attachments/assets/07999112-9e76-43ff-a50c-b1c3dd337696" />
    <img width="1279" height="1689" alt="95042e13daf66c5e3a864dad11ff491f" src="https://github.com/user-attachments/assets/12c33de6-bc26-437f-b92b-1156f1b88702" />


  - **一维**
    - 一维 dp 版的本质，就是把二维 dp 的“上一行”压缩到同一个数组里；
    - 为了不让当前物品在同一轮被重复使用，01 背包必须把容量 从大到小倒序遍历。
    - <img width="1279" height="1807" alt="e3b824433b1629df4002dd74e5a9f835" src="https://github.com/user-attachments/assets/f6ac3649-3439-4a30-98e2-3fa90952252f" />

- [416.分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)
  - 这题本质是 01 背包。先求数组总和 sum，如果 sum 是奇数，直接返回 false。
  - 否则目标和是 target = sum / 2。问题转化为：能否从数组中选出若干个数，使它们的和恰好等于 target。
  - 定义 dp[j] 为容量为 j 的背包所能装出的最大总和。
  - 因为每个数只能使用一次，所以采用 01 背包的一维写法.
  - 外层遍历物品，内层倒序遍历容量，状态转移方程为 dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])。
  - 最后若 dp[target] == target，说明可以刚好凑出一半和，因此可以分割成两个等和子集。
  - <img width="1279" height="1789" alt="f27f1ebcb4ee36a60cbdfb473030d4da" src="https://github.com/user-attachments/assets/defb80c9-b119-43d8-809a-91e73572109a" />

    
