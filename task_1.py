# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.


import os
import json
import csv
import pickle


def get_directory_size(directory):
    total_size = 0
    for path, dirs, files in os.walk(directory):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return total_size


def traverse_directory(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            dir_path = os.path.join(root, d)
            size = get_directory_size(dir_path)
            result.append({
                'path': dir_path,
                'type': 'directory',
                'size': size
            })
        for f in files:
            file_path = os.path.join(root, f)
            size = os.path.getsize(file_path)
            result.append({
                'path': file_path,
                'type': 'file',
                'size': size
            })
    return result


def save_as_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def save_as_csv(data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['path', 'type', 'size'])
        for item in data:
            writer.writerow([item['path'], item['type'], item['size']])


def save_as_pickle(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

# Замените 'directory_path' на путь к вашей директории
directory_path = 'C:\\Users\\kzhes\\OneDrive\\Рабочий стол\\Программирование\\GB\\Погружение в Python'

# Обход директории и сохранение результатов
result = traverse_directory(directory_path)

# Сохранение в файлы JSON, CSV и pickle
save_as_json(result, 'result.json')
save_as_csv(result, 'result.csv')
save_as_pickle(result, 'result.pickle')
