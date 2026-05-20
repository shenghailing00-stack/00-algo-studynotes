# 回溯综合：棋盘问题
- [51.N皇后](https://leetcode.cn/problems/n-queens/description/)
  - 因为每一行只能放一个皇后，所以递归按行进行，row 表示当前处理到第几行。
  - 在当前行中，枚举每一列，判断当前位置是否能放皇后。
  - 合法性检查只需要看当前列上方、左上对角线和右上对角线，因为棋盘是按行从上到下构造的，下面还没有放皇后。
  - 如果当前位置合法，就放一个皇后并递归到下一行；递归返回后再撤销当前位置，继续尝试当前行的其他列。
  - 当递归到 row == n 时，说明前 n 行都成功放置了皇后，此时得到一个完整解，将棋盘加入结果集
    ![845ec59faca856a04e552c50ef3c4220](https://github.com/user-attachments/assets/c8307686-db8f-452f-ae35-be36ed473663)
    ![06959360af00b59193f498520fed4083](https://github.com/user-attachments/assets/b66cf5d0-d966-4506-ba3c-de5af790c3ed)
- [37.解数独](https://leetcode.cn/problems/sudoku-solver/)
  ![ac93c47cf72d97785914ce2a9941ebf8](https://github.com/user-attachments/assets/1e2dbfd3-22aa-44b9-9684-fa30ab9fc50a)


