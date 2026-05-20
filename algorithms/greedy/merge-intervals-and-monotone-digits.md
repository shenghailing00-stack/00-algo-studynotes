# 贪心收尾：区间合并与数字调整
- [56.合并区间](https://leetcode.cn/problems/merge-intervals/description/)
  - 先按照区间的左边界升序排序。
  - 排序后，从左到右遍历区间，用结果数组保存已经合并好的区间。
  - 对于当前区间，判断它的左边界是否小于等于结果数组最后一个区间的右边界：如果 当前左边界 <= 已合并区间右边界，说明有重叠，可以合并
  - 否则说明不重叠，直接加入结果数组
  - 合并时，只需要更新结果数组最后一个区间的右边界为两个右边界的较大值。
  - ![b26123ab819fb711f0ecbd38c912d7ee](https://github.com/user-attachments/assets/415c90c2-1e62-4244-92b7-17a873eaf86f)

- [738.单调递增的数字](https://leetcode.cn/problems/monotone-increasing-digits/description/)
  - 1.先把整数转成字符串，方便逐位处理。
  - 2.从后往前遍历，如果发现前一位大于后一位，说明这里破坏了单调递增。
  - 3.把前一位减 1，并记录从当前位置开始，后面最终都要变成 9。
  - 4.遍历结束后，把 flag 及其后面的所有位都变成 9。
  - 5.最后把字符串转回整数。
  - ![86f3cb4034b610ceb03f74ea56f0911d](https://github.com/user-attachments/assets/4f13e5ab-7e10-4ecd-bc01-c3dc00d248f6)

