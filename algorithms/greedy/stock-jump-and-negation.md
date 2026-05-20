# 贪心练习：股票、跳跃与数组取反
- [122.买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/)
  - 局部最优：收集每天的正利润，全局最优：求得最大利润
 ![d6075efc498196a924f2f42e195f331c](https://github.com/user-attachments/assets/1cef7b65-fe85-4037-a836-c8453b8b120a)

- [55.跳跃游戏](https://leetcode.cn/problems/jump-game/description/)
  - 局部最优解：每次取最大跳跃步数（取最大覆盖范围），整体最优解：最后得到整体最大覆盖范围，看是否能到终点。
  - ![e3e25a18b4d1c98d6a055e66001ae80a](https://github.com/user-attachments/assets/d9400218-1b5c-4567-9b97-d0cbe1cc999c)

  - ![810d42f46de542a2e2a5d076dd3833f1](https://github.com/user-attachments/assets/c3a2ce27-876c-4103-9d36-a0407f25143a)

- [1005.k次取反后最大化的数组和](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/description/)
  - 为了让数组和最大，应该优先把负数变成正数，而且优先翻转绝对值更大的负数，因为这样收益最大。
  - 先将数组按绝对值从大到小排序，再从前往后把负数依次翻转，直到没有负数或 k 用完。
  - 如果处理完后 k 仍然为奇数，就再翻转一次绝对值最小的元素。
  - 最后求数组和即可。
  - ![851f11e521fea963d2b53ea20b8538a0](https://github.com/user-attachments/assets/65df4fdf-3bb0-43d6-b638-9a8e9d075200)
