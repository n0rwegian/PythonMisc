import csv
import requests


'''url = 'https://stepik.org/media/attachments/lesson/24473/Crimes.csv'

with requests.get(url, stream=True) as response:
    response.raise_for_status()
    with open('Crimes.csv', 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
        file.flush()
        file.close()

# print('Successfully downloaded')'''

crimes = {}

with open('Crimes.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2][6:10] == '2015':
            crimes[row[5]] = crimes.get(row[5], 0) + 1

print(crimes)
print(max(crimes, key=lambda x: crimes[x]))
