# 🚀 Day 19 – Contains Duplicate II

## 📌 Problem

Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that:

```python
nums[i] == nums[j]
```

and

```python
abs(i - j) <= k
```

Otherwise, return `false`.

---

# 💡 Approach

A brute force solution would compare every nearby pair, resulting in `O(n²)` complexity.

Instead, we use a hash map to store the latest index of each element.

### Steps:

* Traverse the array
* If the element already exists in the hash map:

  * check the distance between indices
* If distance ≤ `k`, return `True`
* Otherwise, update the latest index

This reduces lookup time efficiently.

---

# ⚙️ Python Solution

```python
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True

            seen[nums[i]] = i

        return False
```

---

# 🧠 Dry Run

Input:

```python
nums = [1,2,3,1]
k = 3
```

| Index | Element | Seen Map                | Condition    |
| ----- | ------- | ----------------------- | ------------ |
| 0     | 1       | {1:0}                   | continue     |
| 1     | 2       | {1:0, 2:1}              | continue     |
| 2     | 3       | {1:0, 2:1, 3:2}         | continue     |
| 3     | 1       | already seen at index 0 | 3 - 0 <= 3 ✅ |

Final Answer:

```python
True
```

---

# ⏱️ Complexity Analysis

| Complexity       | Value |
| ---------------- | ----- |
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

---

# 🧠 Key Learning

This problem teaches:

* Efficient lookup using hashing
* Tracking indices with hash maps
* Optimizing brute force solutions

Hash maps are extremely useful for reducing repeated search operations from `O(n)` to `O(1)` average time.

---

# ⚠️ Important Insight

The latest index should always be updated because a newer duplicate may satisfy the distance condition better.

---

# 🔗 LeetCode

Contains Duplicate II – LeetCode #219

---

