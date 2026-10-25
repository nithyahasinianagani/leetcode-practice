
import re

for _ in range(int(input())):
    s = input()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', s)))


re.match(...)
Checks whether the string matches the pattern, starting from the beginning.


r'...'
The r means raw string. It helps Python handle backslashes in regex patterns correctly.


^
The number must start here — at the beginning.


[-+]?
An optional minus or plus sign.
The ? means zero or one occurrence.

Examples: -2.5, +2.5, 2.5.


[0-9]*
Zero or more digits before the decimal point.
* means zero or more.


\.
A literal decimal point (.).
We use \. because a plain . in regex means any character.


[0-9]+
One or more digits after the decimal point.
+ means at least one.


$
The number must end here — no extra characters.


bool(...)
Converts the match result into True or False.