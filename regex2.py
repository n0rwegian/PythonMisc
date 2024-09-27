"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

Примечание:
Для работы со словами используйте группы символов \\b и \\B.
"""

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\bcat\b"
    if re.search(pattern, line):
        print(line)

# <CTRL-D>  or <CTRL-Z>
# Ctrl-D closes the standard input (stdin) by sending EOF.
