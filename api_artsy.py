"""
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию об имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
выведите их имена в лексикографическом порядке.
"""
import requests
import json


"""
client_id = "<-- artsy settings"
client_secret = "<-- artsy settings"

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# print(j)

# достаем токен
token = j["token"]

# print(token)
"""
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}
artists_info = []

# artist = '4d8b92b34eb68a1b2c0003f4'
with open("dataset_24476_4.txt", "r") as f_in:
    artists = [line.strip() for line in f_in.readlines()]

for artist in artists:
    # инициируем запрос с заголовком
    r = requests.get(f"https://api.artsy.net/api/artists/{artist}", headers=headers)

    # разбираем ответ сервера
    j = json.loads(r.text)

    # print(j)
    artists_info.append((j['sortable_name'], j['birthday']))

with open("output.txt", "w", encoding='utf-8') as f_out:
    f_out.writelines(('\n'.join(elem[0] for elem in sorted(artists_info, key=lambda x: (x[1], x[0])))))


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

"""