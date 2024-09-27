'''
Вам дана в архиве (main) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
'''
import os
from os import walk


result = []
for cur_dir, _, files in os.walk("main"):
    if any(file.endswith(".py") for file in files):
        result.append(cur_dir)

with open("output.txt", "w") as f_out:
    f_out.writelines('\n'.join(sorted(result)))


'''
import zipfile, os

pydirs = list()

with zipfile.ZipFile('main.zip', 'r') as zip:
    for zip_path in zip.namelist():
        if  os.path.dirname(zip_path) not in pydirs and os.path.basename(zip_path).endswith('.py'):
            pydirs.append(os.path.dirname(zip_path))

print('\n'.join(sorted(pydirs)))
'''