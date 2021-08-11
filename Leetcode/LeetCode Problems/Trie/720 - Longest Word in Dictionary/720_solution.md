## I) Approach #1: Brute Force:
---

### 1. Intuition
For each word, check if all prefixes word[:k] are present. We can use a Set structure to check this quickly.

---

### 2. Algorithm

- Whenever our found word would be superior, we check if all it's prefixes are present, then replace our answer.

- Alternatively, we could have sorted the words beforehand, so that we know the word we are considering would be the answer if all it's prefixes are present.

---
### a) Python

> [Approach #1 - Python Solution](720_longest_word_in_dict_01.py)

#### *Alternatively:*

```python
class Solution(object):
    def longestWord(self, words):
        wordset = set(words)
        words.sort(key = lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in xrange(1, len(word))):
                return word

        return ""
```
---

### b) C++

> [Approach #1 - C++ Solution](720_longest_word_in_dict_01.cpp)

#### *Alternatively*:
```cpp
class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end());
        unordered_set<string> built;
        string res;
        for (string w : words) {
            if (w.size() == 1 || built.count(w.substr(0, w.size() - 1))) {
                res = w.size() > res.size() ? w : res;
                built.insert(w);
            }
        }
        return res;
    }
};
```

---

### c) Java

> [Approach #1 - Java Solution](720_longest_word_in_dict.java)

#### *Alternatively*
```java
class Solution {
    public String longestWord(String[] words) {
        Set<String> wordset = new HashSet();
        for (String word: words) wordset.add(word);
        Arrays.sort(words, (a, b) -> a.length() == b.length()
                    ? a.compareTo(b) : b.length() - a.length());
        for (String word: words) {
            boolean good = true;
            for (int k = 1; k < word.length(); ++k) {
                if (!wordset.contains(word.substring(0, k))) {
                    good = false;
                    break;
                }
            }
            if (good) return word;
        }

        return "";
    }
}
```

### 3. Complexity Analysis

- Time complexity :`O(∑w_i^2)`, where w_i is the length of words[i]. Checking whether all prefixes of words[i] are in the set is `O(∑w_i^2)`.

- Space complexity : `O(∑w_i^2)` to create the substrings.

----------------------------------------------------------------

## II) Approach #2: Trie + Depth-First Search
---

### 1. Intuition

As prefixes of strings are involved, this is usually a natural fit for a trie (a prefix tree.)

### 2. Algorithm

Put every word in a trie, then depth-first-search from the start of the trie, only searching nodes that ended a word. Every node found (except the root, which is a special case) then represents a word with all it's prefixes present. We take the best such word.

---

In Python, we showcase a method using defaultdict, while in Java, we stick to a more general object-oriented approach.

---
### a) Python:

[Approach #2 - Python Solution](720_longest_word_in_dict_02.py)

### b) C++:
[Approach #2 - C++ Solution](720_longest_word_in_dict_02.cpp)