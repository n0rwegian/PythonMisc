"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
"""

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    pattern = r"z.{3}z"
    if re.search(pattern, line):
        print(line)

# <CTRL-D>  or <CTRL-Z>
# Ctrl-D closes the standard input (stdin) by sending EOF.

"""
   
"""
