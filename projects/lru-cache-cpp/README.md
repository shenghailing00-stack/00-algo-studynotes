# LRU Cache 缓存模拟器

## 项目简介

这是一个用 C++ 写的 LRU Cache 小项目。它不是单纯刷一道题，而是把 `unordered_map`、`list` 和命令行交互放在一起，模拟一个真实缓存的基本行为。

我做这个项目主要是想练习两个点：一是怎么用 STL 组合出更高效的数据结构，二是理解“最近使用”和“最久未使用”这件事在代码里到底怎么维护。

## 技术栈

- C++17
- STL `unordered_map`
- STL `list`
- 命令行输入输出

没有使用第三方库。

## 功能说明

程序启动后先输入缓存容量，然后可以输入以下命令：

- `put key value`：插入或更新缓存
- `get key`：查询缓存
- `show`：显示当前缓存状态
- `exit`：退出程序

缓存状态会按照“最近使用 -> 最久未使用”的顺序输出。

## 运行方式

在项目目录下编译：

```bash
g++ -std=c++17 main.cpp -o lru_cache
```

Windows 下也可以生成 `.exe`：

```bash
g++ -std=c++17 main.cpp -o lru_cache.exe
```

运行：

```bash
./lru_cache
```

Windows PowerShell 中运行：

```powershell
.\lru_cache.exe
```

## 命令示例

假设启动后输入容量 `2`，再输入：

```text
put 1 100
put 2 200
get 1
put 3 300
show
exit
```

过程说明：

- `put 1 100` 后缓存里有 key 1
- `put 2 200` 后缓存里有 key 2 和 key 1
- `get 1` 命中 key 1，所以 key 1 变成最近使用
- `put 3 300` 时容量已满，会淘汰最久未使用的 key 2
- `show` 应该能看到 key 3 和 key 1

## 核心算法说明

LRU 的全称是 Least Recently Used，意思是“最近最少使用”。当缓存满了以后，优先淘汰最长时间没有被访问过的数据。

这个项目里用两种 STL 容器配合实现：

- `list` 用来维护访问顺序
- `unordered_map` 用来快速定位 key

链表头部保存最近使用的数据，链表尾部保存最久未使用的数据。

当执行 `get key`：

1. 先用 `unordered_map` 查 key 是否存在。
2. 如果不存在，返回 `-1`。
3. 如果存在，直接拿到它在 `list` 中的位置。
4. 把这个节点移动到链表头部，表示它刚刚被访问过。

当执行 `put key value`：

1. 如果 key 已经存在，就更新 value，并把节点移动到链表头部。
2. 如果 key 不存在，就插入到链表头部。
3. 如果插入前容量已满，就删除链表尾部节点，并同步从 `unordered_map` 中删除这个 key。

这样 `unordered_map` 负责“找得快”，`list` 负责“顺序改得快”，两者结合后就可以让 `get` 和 `put` 平均达到 O(1)。

## 时间复杂度分析

- `get key`：平均 O(1)
- `put key value`：平均 O(1)
- `show`：O(n)，因为要把当前缓存内容遍历一遍

这里的 O(1) 主要依赖 `unordered_map` 的平均查找效率，以及 `list::splice` 移动节点时不需要重新拷贝元素。

## 学习收获

- 更熟悉了 `unordered_map` 的快速查找能力。
- 理解了双向链表适合频繁移动节点的场景。
- 学会了用迭代器把哈希表和链表连接起来。
- 对 LRU 缓存淘汰策略有了更具体的认识。
- 练习了 C++ 命令行程序的输入解析。

## 后续可优化方向

- 支持字符串类型的 key 和 value。
- 增加 `remove key` 命令。
- 增加缓存命中率统计。
- 把 `LRUCache` 拆成单独的头文件和源文件。
- 增加自动化测试用例。
