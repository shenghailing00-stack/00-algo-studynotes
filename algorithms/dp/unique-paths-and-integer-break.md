# 动态规划基础：路径与整数拆分
- [不同路径](https://leetcode.cn/problems/unique-paths/description/)
  - 到达当前格子的方法数 = 到达上面格子的方法数 + 到达左边格子的方法数
  - 定义 dp[i][j] 为从左上角走到坐标 (i,j) 的不同路径数。
  - 由于机器人只能向右或向下移动，因此到达 (i,j) 的最后一步只能来自上方 (i-1,j) 或左方 (i,j-1)，所以状态转移方程为 dp[i][j] = dp[i-1][j] + dp[i][j-1]。
  - 初始化时，第一行和第一列都只有一种走法，因此都置为 1。
  - 然后按照从上到下、从左到右的顺序遍历二维数组，最终返回右下角 dp[m-1][n-1]
  - ![2e5feb20da7d3dbb6cb8c3efa36edb79](https://github.com/user-attachments/assets/7290231a-34cb-474f-bf87-07e55385d632)
- [不同路径II](https://leetcode.cn/problems/unique-paths-ii/description/)
  - “不同路径”的障碍物版本。
  - 定义 dp[i][j] 为从左上角到达 (i,j) 的不同路径数。
  - 如果当前位置不是障碍物，那么到达它的方法数等于上方和左方的方法数之和，即 dp[i][j] = dp[i-1][j] + dp[i][j-1]；如果当前位置是障碍物，则该位置不可达，路径数为 0。
  - 初始化时，第一行和第一列在遇到障碍物之前都为 1，一旦遇到障碍物，后面的格子都不可达，因此保持为 0。
  - 最后返回右下角 dp[m-1][n-1] 即可。
  - ![0a5bb1b1d4fb0b559342b7789c46ed44](https://github.com/user-attachments/assets/9b467bd5-79c8-4f0b-9d81-800de4adff1c)
- [整数拆分](https://leetcode.cn/problems/integer-break/description/)
  - 定义 dp[i] 为整数 i 拆分成至少两个正整数后得到的最大乘积。
  - 对于每个 i，枚举第一个拆出的数 j，此时剩余部分为 i-j。
  - 剩余部分有两种选择：一种是不再拆分，乘积为 j*(i-j)；另一种是继续拆分，乘积为 j*dp[i-j]。
  - 因此状态转移方程为 dp[i] = max(dp[i], max((i-j)*j, dp[i-j]*j))。
  - 初始化 dp[2]=1，然后按从小到大的顺序计算到 dp[n]，最终返回 dp[n]
![52c8fd681de8c2fc4e9cb026cc5b117f](https://github.com/user-attachments/assets/68c1136b-a698-4b82-baa7-0df22dfa7003)

