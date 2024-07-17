# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

def get_directory_size(directory):
    """Calculate the total size of the directory, including all subdirectories and files."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def scan_directory(directory):
    """Recursively scan the directory and collect information about files and subdirectories."""
    results = []
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            dir_path = os.path.join(root, name)
            results.append({
                "path": dir_path,
                "parent": root,
                "type": "directory",
                "size": get_directory_size(dir_path)
            })
        for name in files:
            file_path = os.path.join(root, name)
            results.append({
                "path": file_path,
                "parent": root,
                "type": "file",
                "size": os.path.getsize(file_path)
            })
    return results

def save_results(results, json_file, csv_file, pickle_file):
    """Save the results to JSON, CSV, and Pickle files."""
    # Save to JSON
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    # Save to CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["path", "parent", "type", "size"])
        writer.writeheader()
        for row in results:
            writer.writerow(row)

    # Save to Pickle
    with open(pickle_file, 'wb') as f:
        pickle.dump(results, f)

# Пример использования
directory_to_scan = r'G:\_Disk\gb.ru\Разработчик - DataEngineer\Погружение в Python\HW8\maindir'
json_output = 'results.json'
csv_output = 'results.csv'
pickle_output = 'results.pkl'

results = scan_directory(directory_to_scan)
save_results(results, json_output, csv_output, pickle_output)