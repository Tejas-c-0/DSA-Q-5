# Remove Duplicates from Sorted Array

## Problem
Given a sorted array `nums`, remove duplicates in-place and return the number of unique elements.

---

## Approach
- Use two pointers:
  - `i` → position for unique elements
  - `j` → scans the array
- If `nums[j] != nums[i]`, move `i` forward and update value
- This overwrites duplicates with unique values

---

## Complexity
- Time: O(n)
- Space: O(1)

---

## Key Insight
Since the array is sorted, duplicates are adjacent.  
This allows us to detect and remove them efficiently using two pointers.

---

## Example
Input: [1,1,2,2,3]  
Output: 3 → nums becomes [1,2,3,_,_]

---

## Code
```python
def removeDuplicates(nums):
    if not nums:
        return 0

    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
