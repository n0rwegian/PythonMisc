"""
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \\w.
"""

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\b(\w)(\w)(\w*)\b"
    repl = r"\2\1\3"
    line = re.sub(pattern, repl, line)

    print(line)

# <CTRL-D>  or <CTRL-Z>
# Ctrl-D closes the standard input (stdin) by sending EOF.

"""
   
"""
