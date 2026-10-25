
import re

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

print(bool(re.match(regex_pattern, input())))



Box 1: Thousands
M{0,3}

Allows zero to three Ms: M, MM, MMM.


Box 2: Hundreds
(CM|CD|D?C{0,3})

Handles values such as 100, 400, 500 and 900.


Box 3: Tens
(XC|XL|L?X{0,3})

Handles values such as 10, 40, 50 and 90.


Box 4: Ones
(IX|IV|V?I{0,3})

Handles values such as 1, 4, 5 and 9.



^ — start of the string.
$ — end of the string.
| — OR. For example, CM|CD means CM or CD.
? — zero or one occurrence.
{0,3} — repeat between zero and three times.
() — groups parts of the pattern together