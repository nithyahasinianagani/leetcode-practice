# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
s = "A man, a plan, a canal: Panama"
s = ''.join(c.lower() for c in s if c.isalnum())
print(s == s[::-1])