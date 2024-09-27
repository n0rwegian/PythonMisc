"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
"""

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    pattern = r"cat"
    if len(re.findall(pattern, line)) >= 2:
        print(line)

# <CTRL-D>  or <CTRL-Z>
# Ctrl-D closes the standard input (stdin) by sending EOF.

"""
    pattern = r'.*cat.*cat+.*'
    result = re.search(pattern, line)
    if result:
        print(line)
"""

"""
re.search(r"cat.*cat", line)
"""