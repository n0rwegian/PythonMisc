"""
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать,
    существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
"""
import requests


with open('dataset_24476_3.txt', "r") as f_in:
    numbers = [int(line) for line in f_in.readlines()]

request_params = {
    "default": "Boring"
}

with open("output.txt", 'w') as f_out:
    for number in numbers:
        ans = requests.get(f'http://numbersapi.com/{number}/math',params=request_params)
        # print(ans.status_code)
        # print(ans.headers["Content-Type"]) -->text/html
        f_out.writelines(["Interesting", "Boring"][ans.text == "Boring"] + '\n')


"""
import requests

headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
params = {'json':'text', 'default':'Boring'}
with open('dataset_24476_3.txt','r') as f:
    df = f.read().replace('\n',',')[:-1]

response = requests.get(f'http://numbersapi.com/{df}/math', headers=headers, params=params)
data = response.json()
for key,value in data.items():
    if 'Boring' in value:
        print(key, 'Boring')
    else:
        print(key, 'Interesting')
"""

"""
import requests
import json

def is_interesting(x):
    url = "http://numbersapi.com/"; + str(x) + "/math?json=true"
    resp = requests.get(url).text
    js = json.loads(resp)
    return js["found"]

with open("input.txt") as fi:
    for line in fi:
        print("Interesting" if is_interesting(line.rstrip()) else "Boring")
"""