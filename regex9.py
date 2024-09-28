"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \\w.
"""

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    pattern = r"(\w)\1+"
    repl = r"\1"
    line = re.sub(pattern, repl, line)

    print(line)

# <CTRL-D>  or <CTRL-Z>
# Ctrl-D closes the standard input (stdin) by sending EOF.

"""
   
"""
