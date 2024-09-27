"""
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
"""

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\b(\w+)\1\b"
    match_p = re.match(pattern, line)
    if match_p:
        print(line)

# <CTRL-D>  or <CTRL-Z>
# Ctrl-D closes the standard input (stdin) by sending EOF.

"""
   
"""
