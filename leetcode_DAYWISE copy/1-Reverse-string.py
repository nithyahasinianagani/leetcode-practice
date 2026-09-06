# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]/
s = ["h","e","l","l","o"]

s.reverse()
print(s)

s[:] = s[::-1]
print(s)