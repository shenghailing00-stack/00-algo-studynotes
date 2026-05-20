# 贪心区间问题
- [452.用最少数量的箭射穿气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)
  - ![374f05162b3709d1097a1adaa2b8ba27](https://github.com/user-attachments/assets/9ce5657c-7855-4895-ac20-55a693193713)
- [435.无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/description/)
  - ![44f87dbf1eef07dec391f083ebe04e7c](https://github.com/user-attachments/assets/618fdce4-4b78-4d2c-ae7c-2f0cf230f4a8)
- [763.划分字母区间](https://leetcode.cn/problems/partition-labels/)
  - 先统计每个字符最后一次出现的位置。
  - 然后从左到右遍历字符串，用 right 维护当前片段中所有字符的最远右边界。
  - 每遇到一个字符，就用它最后出现的位置更新 right。
  - 当遍历下标 i 等于 right 时，说明当前片段中的所有字符都已经完整包含在这一段内，可以切分出一个片段，其长度为 right - left + 1。
  - 然后更新下一段的起点继续处理即可
    ![c064d80992674992c9529d127c8f0df7](https://github.com/user-attachments/assets/b472abfa-dea4-4bb0-bc66-d5f9b1f31948)


