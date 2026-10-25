# main difference is: findall() gives you the matched text, while finditer() gives you match objects. 😊


import re

s = input()
matches = re.findall(r'(?<=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])[aeiouAEIOU]{2,}(?=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])', s)

if matches:
    print(*matches, sep='\n')
else:
    print(-1)

Pattern	Meaning
(?<=...)	Check what is immediately before the match
[bcdfghjklmnpqrstvwxyz...]	A consonant
[aeiouAEIOU]	Any vowel
{2,}	At least two vowels together
(?=...)	Check what is immediately after the match

The consonants are checked but not included in the output.
4. What do the Python functions do?
- re.findall() collects all matching groups into a list.
- if matches: checks whether the list contains any results.
- print(*matches, sep='\n') prints each result on a separate line.
- else: print(-1) handles the case where no matches are found.