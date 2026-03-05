import os
import random
import sys
import time
from collections import deque

# Terminal Snake (Windows-friendly, no curses)
# Controls: W/A/S/D + Enter, Q + Enter to quit

WIDTH = 20
HEIGHT = 12
TICK = 0.12  # seconds per step


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def place_food(snake, width, height):
    occupied = set(snake)
    while True:
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        if (x, y) not in occupied:
            return (x, y)


def render(snake, food, width, height, score):
    grid = [[" " for _ in range(width)] for _ in range(height)]

    # walls
    for x in range(width):
        grid[0][x] = "#"
        grid[height - 1][x] = "#"
    for y in range(height):
        grid[y][0] = "#"
        grid[y][width - 1] = "#"

    # food
    fx, fy = food
    grid[fy][fx] = "*"

    # snake
    head = snake[0]
    hx, hy = head
    grid[hy][hx] = "O"
    for (x, y) in list(snake)[1:]:
        grid[y][x] = "o"

    lines = ["".join(row) for row in grid]
    lines.append(f"Score: {score}    (W/A/S/D + Enter, Q + Enter)")
    return "\n".join(lines)


def next_dir(cur_dir, cmd):
    cmd = cmd.strip().lower()
    if cmd == "w":
        nd = (0, -1)
    elif cmd == "s":
        nd = (0, 1)
    elif cmd == "a":
        nd = (-1, 0)
    elif cmd == "d":
        nd = (1, 0)
    elif cmd == "q":
        return None
    else:
        return cur_dir  # ignore unknown input

    # prevent direct reverse
    if (nd[0] == -cur_dir[0] and nd[1] == -cur_dir[1]):
        return cur_dir
    return nd


def main():
    random.seed()

    snake = deque()
    start = (WIDTH // 2, HEIGHT // 2)
    snake.appendleft(start)
    snake.append((start[0] - 1, start[1]))
    snake.append((start[0] - 2, start[1]))

    direction = (1, 0)
    food = place_food(snake, WIDTH, HEIGHT)
    score = 0

    clear_screen()
    print("Little Snake Baby Game")
    print("Controls: W/A/S/D then Enter. Q then Enter to quit.")
    print("Press Enter to start...")
    input()

    while True:
        clear_screen()
        print(render(snake, food, WIDTH, HEIGHT, score))

        # Read command (line input keeps it simple & Windows-friendly)
        cmd = input("Move (w/a/s/d, q to quit): ")
        nd = next_dir(direction, cmd)
        if nd is None:
            print("Bye!")
            return
        direction = nd

        hx, hy = snake[0]
        dx, dy = direction
        new_head = (hx + dx, hy + dy)

        # collision: wall
        if new_head[0] == 0 or new_head[0] == WIDTH - 1 or new_head[1] == 0 or new_head[1] == HEIGHT - 1:
            clear_screen()
            print(render(snake, food, WIDTH, HEIGHT, score))
            print("\nGame Over! You hit the wall.")
            return

        # collision: self
        if new_head in snake:
            clear_screen()
            print(render(snake, food, WIDTH, HEIGHT, score))
            print("\nGame Over! You hit yourself.")
            return

        snake.appendleft(new_head)

        # eat
        if new_head == food:
            score += 1
            food = place_food(snake, WIDTH, HEIGHT)
        else:
            snake.pop()

        time.sleep(TICK)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
