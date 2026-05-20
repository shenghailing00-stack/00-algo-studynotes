#include <iostream>
#include <list>
#include <sstream>
#include <string>
#include <unordered_map>

class LRUCache {
public:
    explicit LRUCache(int capacity) : capacity_(capacity) {}

    int get(int key) {
        auto found = cache_map_.find(key);
        if (found == cache_map_.end()) {
            return -1;
        }

        // 命中后移动到链表头部，表示最近刚使用过。
        cache_items_.splice(cache_items_.begin(), cache_items_, found->second);
        return found->second->second;
    }

    void put(int key, int value) {
        auto found = cache_map_.find(key);
        if (found != cache_map_.end()) {
            found->second->second = value;
            // 更新已有 key 时，也刷新最近使用状态。
            cache_items_.splice(cache_items_.begin(), cache_items_, found->second);
            return;
        }

        if (static_cast<int>(cache_items_.size()) == capacity_) {
            // 链表尾部是最久未使用的数据，容量满时优先淘汰它。
            auto least_used = cache_items_.back();
            cache_map_.erase(least_used.first);
            cache_items_.pop_back();
        }

        cache_items_.push_front({key, value});
        cache_map_[key] = cache_items_.begin();
    }

    void show() const {
        if (cache_items_.empty()) {
            std::cout << "Cache is empty.\n";
            return;
        }

        std::cout << "Cache state (most recent -> least recent): ";
        bool is_first = true;
        for (const auto& item : cache_items_) {
            if (!is_first) {
                std::cout << " -> ";
            }
            std::cout << "[" << item.first << ":" << item.second << "]";
            is_first = false;
        }
        std::cout << "\n";
    }

private:
    int capacity_;
    std::list<std::pair<int, int>> cache_items_;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> cache_map_;
};

void print_help() {
    std::cout << "Commands:\n";
    std::cout << "  put key value  Insert or update a cache item\n";
    std::cout << "  get key        Query a cache item\n";
    std::cout << "  show           Show cache state\n";
    std::cout << "  exit           Quit program\n";
}

int main() {
    std::cout << "Enter cache capacity: ";
    int capacity = 0;
    if (!(std::cin >> capacity) || capacity <= 0) {
        std::cout << "Capacity must be a positive integer.\n";
        return 1;
    }

    LRUCache cache(capacity);
    print_help();

    std::string line;
    std::getline(std::cin, line);

    while (true) {
        std::cout << "> ";
        if (!std::getline(std::cin, line)) {
            break;
        }

        std::istringstream parser(line);
        std::string command;
        parser >> command;

        if (command == "put") {
            int key = 0;
            int value = 0;
            if (parser >> key >> value) {
                cache.put(key, value);
                std::cout << "put " << key << " " << value << " ok\n";
            } else {
                std::cout << "Usage: put key value\n";
            }
        } else if (command == "get") {
            int key = 0;
            if (parser >> key) {
                int value = cache.get(key);
                if (value == -1) {
                    std::cout << "get " << key << " -> -1 (not found)\n";
                } else {
                    std::cout << "get " << key << " -> " << value << "\n";
                }
            } else {
                std::cout << "Usage: get key\n";
            }
        } else if (command == "show") {
            cache.show();
        } else if (command == "exit") {
            std::cout << "Bye.\n";
            break;
        } else if (command.empty()) {
            continue;
        } else {
            std::cout << "Unknown command: " << command << "\n";
            print_help();
        }
    }

    return 0;
}
