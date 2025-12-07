import os
from pathlib import Path

def show_desktop_items():
    """
    Возвращает текст для озвучивания объектов на рабочем столе.
    Вызывай voice.speaker(result) для голосового вывода.
    """
    desktop_path = Path.home() / "Desktop"
    
    speech_text = "Объекты на рабочем столе. "
    
    for item in sorted(desktop_path.iterdir()):
        if item.is_dir():
            speech_text += f"Папка {item.name}. "
        elif item.is_file():
            name_without_ext = item.stem
            speech_text += f"Файл {name_without_ext}. "
        else:
            speech_text += f"{item.name}. "
    
    print("Объекты на рабочем столе:")
    print("-" * 40)
    for item in sorted(desktop_path.iterdir()):
        if item.is_dir():
            print(f"📁 Папка: {item.name}")
        elif item.is_file():
            name_without_ext = item.stem
            print(f"📄 Файл: {name_without_ext}")
        else:
            print(f"🔗 {item.name}")
    
    return speech_text

# Пример использования с твоим voice.speaker
if __name__ == "__main__":
    result = show_desktop_items()
    # voice.speaker(result)  # Раскомментируй для озвучивания
    print("\nГотовый текст для voice.speaker:")
    print(result)
