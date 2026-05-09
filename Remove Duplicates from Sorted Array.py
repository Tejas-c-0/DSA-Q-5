s = ["h","e","l","l","o"]
def reverse(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
        
    return s
print(reverse(s)) 
