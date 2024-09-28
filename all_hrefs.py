"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов,
на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов,
 которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть,
 за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.
"""
import re
import requests


link = requests.get(input().strip())
pattern = r"(?:<a\s.*href=[\"|\'])+(?:[^/>]*//)?([\w\d]+[\w\.\d-]+)"
possible_links = re.findall(pattern, link.text)
print(*sorted(set(possible_links)), sep='\n')

"""
link_test1 = requests.get("http://pastebin.com/raw/2mie4QYa")
link_test2 = requests.get("http://pastebin.com/raw/hfMThaGb")
link_test3 = requests.get("https://pastebin.com/raw/7543p0ns")
"""