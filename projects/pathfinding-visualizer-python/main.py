import random
import tkinter as tk
from collections import deque
from tkinter import messagebox


ROWS = 20
COLS = 30
CELL_SIZE = 28

EMPTY = "empty"
START = "start"
END = "end"
WALL = "wall"
VISITED = "visited"
PATH = "path"

COLORS = {
    EMPTY: "#ffffff",
    START: "#2ecc71",
    END: "#e74c3c",
    WALL: "#2c3e50",
    VISITED: "#85c1e9",
    PATH: "#f1c40f",
}


class PathfindingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("迷宫寻路可视化器 - BFS")

        self.grid = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        self.start = (2, 2)
        self.end = (ROWS - 3, COLS - 3)
        self.grid[self.start[0]][self.start[1]] = START
        self.grid[self.end[0]][self.end[1]] = END

        self.current_tool = tk.StringVar(value=START)
        self.is_searching = False

        self.canvas = tk.Canvas(
            root,
            width=COLS * CELL_SIZE,
            height=ROWS * CELL_SIZE,
            bg="#ffffff",
            highlightthickness=0,
        )
        self.canvas.grid(row=0, column=0, columnspan=6, padx=12, pady=12)
        self.canvas.bind("<Button-1>", self.handle_cell_click)
        self.canvas.bind("<B1-Motion>", self.handle_cell_click)

        self.build_controls()
        self.draw_grid()

    def build_controls(self):
        tools = [
            ("起点", START),
            ("终点", END),
            ("障碍物", WALL),
            ("橡皮擦", EMPTY),
        ]

        for index, (label, value) in enumerate(tools):
            tk.Radiobutton(
                self.root,
                text=label,
                value=value,
                variable=self.current_tool,
            ).grid(row=1, column=index, padx=6, pady=(0, 12), sticky="w")

        tk.Button(self.root, text="开始寻路", command=self.start_search).grid(
            row=2, column=0, padx=6, pady=(0, 12), sticky="ew"
        )
        tk.Button(self.root, text="清空地图", command=self.clear_grid).grid(
            row=2, column=1, padx=6, pady=(0, 12), sticky="ew"
        )
        tk.Button(self.root, text="随机障碍物", command=self.random_walls).grid(
            row=2, column=2, padx=6, pady=(0, 12), sticky="ew"
        )

        self.status_label = tk.Label(
            self.root,
            text="选择工具后点击网格：绿色起点，红色终点，深色障碍物。",
            anchor="w",
        )
        self.status_label.grid(row=3, column=0, columnspan=6, padx=12, pady=(0, 12), sticky="ew")

    def draw_grid(self):
        self.canvas.delete("all")
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                cell_type = self.grid[row][col]
                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=COLORS[cell_type],
                    outline="#d5d8dc",
                )

    def handle_cell_click(self, event):
        if self.is_searching:
            return

        row = event.y // CELL_SIZE
        col = event.x // CELL_SIZE
        if not self.is_inside_grid(row, col):
            return

        tool = self.current_tool.get()
        if tool == START:
            self.set_start(row, col)
        elif tool == END:
            self.set_end(row, col)
        elif tool == WALL:
            self.set_wall(row, col)
        else:
            self.erase_cell(row, col)

        self.draw_grid()

    def set_start(self, row, col):
        if (row, col) == self.end:
            return

        old_row, old_col = self.start
        self.grid[old_row][old_col] = EMPTY
        self.start = (row, col)
        self.grid[row][col] = START

    def set_end(self, row, col):
        if (row, col) == self.start:
            return

        old_row, old_col = self.end
        self.grid[old_row][old_col] = EMPTY
        self.end = (row, col)
        self.grid[row][col] = END

    def set_wall(self, row, col):
        if (row, col) not in (self.start, self.end):
            self.grid[row][col] = WALL

    def erase_cell(self, row, col):
        if (row, col) not in (self.start, self.end):
            self.grid[row][col] = EMPTY

    def clear_grid(self):
        if self.is_searching:
            return

        self.grid = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        self.grid[self.start[0]][self.start[1]] = START
        self.grid[self.end[0]][self.end[1]] = END
        self.status_label.config(text="地图已清空。")
        self.draw_grid()

    def random_walls(self):
        if self.is_searching:
            return

        self.clear_grid()
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in (self.start, self.end):
                    continue
                if random.random() < 0.25:
                    self.grid[row][col] = WALL

        self.status_label.config(text="已随机生成障碍物。")
        self.draw_grid()

    def clear_search_marks(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.grid[row][col] in (VISITED, PATH):
                    self.grid[row][col] = EMPTY

        self.grid[self.start[0]][self.start[1]] = START
        self.grid[self.end[0]][self.end[1]] = END

    def start_search(self):
        if self.is_searching:
            return

        self.clear_search_marks()
        visited_order, path = self.bfs()
        if not path:
            self.status_label.config(text="没有找到从起点到终点的路径。")
            self.draw_grid()
            messagebox.showinfo("搜索结果", "没有找到可达路径。")
            return

        self.is_searching = True
        self.status_label.config(text="正在展示 BFS 搜索过程...")
        self.animate_search(visited_order, path, 0)

    def bfs(self):
        queue = deque([self.start])
        visited = {self.start}
        prev = {}
        visited_order = []

        # BFS 使用队列逐层扩展，因此第一次到达终点时就是最短路径。
        while queue:
            current = queue.popleft()
            if current != self.start:
                visited_order.append(current)

            if current == self.end:
                break

            for neighbor in self.get_neighbors(current):
                if neighbor in visited:
                    continue

                row, col = neighbor
                if self.grid[row][col] == WALL:
                    continue

                visited.add(neighbor)
                prev[neighbor] = current  # 记录前驱节点，方便最后反向还原路径。
                queue.append(neighbor)

        if self.end not in visited:
            return visited_order, []

        return visited_order, self.build_path(prev)

    def build_path(self, prev):
        path = []
        current = self.end

        # 从终点沿着前驱字典反向回溯，得到 BFS 找到的最短路径。
        while current != self.start:
            path.append(current)
            current = prev[current]

        path.reverse()
        return path

    def get_neighbors(self, cell):
        row, col = cell
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for row_delta, col_delta in directions:
            next_row = row + row_delta
            next_col = col + col_delta
            if self.is_inside_grid(next_row, next_col):
                neighbors.append((next_row, next_col))

        return neighbors

    def is_inside_grid(self, row, col):
        return 0 <= row < ROWS and 0 <= col < COLS

    def animate_search(self, visited_order, path, index):
        if index < len(visited_order):
            row, col = visited_order[index]
            if (row, col) not in (self.start, self.end):
                self.grid[row][col] = VISITED
            self.draw_grid()
            self.root.after(15, self.animate_search, visited_order, path, index + 1)
            return

        self.animate_path(path, 0)

    def animate_path(self, path, index):
        if index < len(path):
            row, col = path[index]
            if (row, col) not in (self.start, self.end):
                self.grid[row][col] = PATH
            self.draw_grid()
            self.root.after(35, self.animate_path, path, index + 1)
            return

        self.is_searching = False
        self.status_label.config(text=f"寻路完成，最短路径长度：{len(path)}。")


def main():
    root = tk.Tk()
    PathfindingVisualizer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
