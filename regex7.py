"""
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен),
на слово "argh".

Примечание:
Обратите внимание на параметр count у функции sub.
"""

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\ba+\b"
    repl = r"argh"
    line = re.sub(pattern, repl, line, count=1, flags=re.IGNORECASE)
    print(line)

# <CTRL-D>  or <CTRL-Z>
# Ctrl-D closes the standard input (stdin) by sending EOF.

"""
   
"""
