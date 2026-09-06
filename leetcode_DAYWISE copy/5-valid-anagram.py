# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
s = "anagram"
t = "nagaram"
print(sorted(s) == sorted(t))