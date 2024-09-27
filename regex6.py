"""
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.
"""

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    pattern = r"human"
    repl = r"computer"
    line = re.sub(pattern, repl, line)
    print(line)

# <CTRL-D>  or <CTRL-Z>
# Ctrl-D closes the standard input (stdin) by sending EOF.

"""
   
"""
