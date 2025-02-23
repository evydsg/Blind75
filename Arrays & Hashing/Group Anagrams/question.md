
# **Group Anagrams**

**Solved** ✅

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.

An **anagram** is a string that contains the exact same characters as another string, but the order of the characters can be different.

## **Example 1:**
```plaintext
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```

## **Example 2:**
```plaintext
Input: strs = ["x"]
Output: [["x"]]
```

## **Example 3:**
```plaintext
Input: strs = [""]
Output: [[""]]
```

## **Constraints:**
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.
