
import re

S = input()
k = input()

matches = re.finditer(f'(?={re.escape(k)})', S)

found = False

for match in matches:
    start = match.start()
    end = start + len(k) - 1
    print((start, end))
    found = True

if not found:
    print((-1, -1))
