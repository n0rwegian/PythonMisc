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
class Artist:
    def __init__(self, name, year):
        self.name = name
        self.year = year


class Artists:
    def __init__(self, ids, token):
        self.ids = ids
        self.artists = []
        self.token = token

    def _get_name_and_year(self):
        header = {"X-Xapp-Token": self.token}
        for artist_id in self.ids:
            artist_id = artist_id.strip()
            url = f"https://api.artsy.net/api/artists/{artist_id}"
            res = requests.get(url, headers=header)
            res = res.json()
            name, year = res["sortable_name"], res["birthday"]
            self.artists += [Artist(name, year)]

    def sort_artists_by_birthday(self):
        self._get_name_and_year()
        self.artists.sort(key=lambda artist: artist.year)
        for artist in self.artists:
            print(artist.name)


def get_token(id, secret):
    data = {
        "client_id": id,
        "client_secret": secret
    }
    r = requests.post("https://api.artsy.net/api/tokens/xapp_token", data)
    j = r.json()
    return j["token"]


def get_artist_ids(path):
    with open(path) as f:
        artist_ids = f.readlines()
        return artist_ids


token = get_token(client_id, client_secret)
ids = get_artist_ids(path)
artists = Artists(ids, token)
artists.sort_artists_by_birthday()
"""
