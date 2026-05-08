# 前缀型动态规划
- [139.单词拆分](https://leetcode.cn/problems/word-break/description/)
  - 本题是前缀型动态规划。设 dp[i] 表示字符串 s 的前 i 个字符是否可以由字典中的单词拼接而成。
  - 初始化 dp[0] = true，表示空字符串可以合法拆分。
  - 对于每个 i，枚举切分点 j，如果 dp[j] 为 true，且子串 s[j...i-1] 在字典中，则说明前 i 个字符可以拆分，即 dp[i] = true。
  - 最终答案为 dp[s.size()]。
    - 为了提高查找效率，通常先将 wordDict 从 vector<string> 转换成 unordered_set<string>。哈希集合是一种适合快速判断元素是否存在的容器。转换语法为：unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
    - s.substr(j, i-j) 表示从字符串 s 的下标 j 开始，截取长度为 i-j 的子串，也就是区间 s[j...i-1]。
    - wordSet.find(word) != wordSet.end() 表示在哈希集合中找到了 word，也就是 word 在字典中。
  <img width="1279" height="1715" alt="2a50c957a0c8308040dcba06c15bcf45" src="https://github.com/user-attachments/assets/db653fcc-4d92-4336-8cc4-fba7410d8645" />
