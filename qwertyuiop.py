# открывает нужную папку

import os
import subprocess
from pathlib import Path

def open_path_by_name(base_folder: str, name: str):
    base_path = Path(base_folder)
    if not base_path.exists() or not base_path.is_dir():
        print(f"Путь {base_folder} не существует или не является папкой.")
        return

    # Поиск объекта по имени в указанной папке (без учета регистра)
    for item in base_path.iterdir():
        if item.name.lower() == name.lower():
            # Открытие файла или папки средствами ОС Windows
            try:
                if item.is_dir():
                    os.startfile(str(item))  # Открыть папку
                elif item.is_file():
                    os.startfile(str(item))  # Открыть файл с ассоциированной программой
                else:
                    print("Объект найден, но тип не поддерживается для открытия.")
                print(f"Открыт объект: {item}")
            except Exception as e:
                print(f"Ошибка при открытии: {e}")
            return

    print(f"Объект с именем '{name}' не найден в папке {base_folder}")

# Пример использования:
folder = input("Введите путь к папке, где искать объект: ")
filename = input("Введите имя файла или папки для открытия: ")

open_path_by_name(folder, filename)