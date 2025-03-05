import os

def list_directories(path):
    """Возвращает список только папок в указанном пути."""
    return [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]

def list_files(path):
    """Возвращает список только файлов в указанном пути."""
    return [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))]

def list_all(path):
    """Возвращает список всех элементов (папок и файлов) в указанном пути."""
    return os.listdir(path)

# Указание пути к рабочему столу
path = r"C:\Users\Ерасыл\Desktop"

try:
    # Изменение текущей директории
    os.chdir(path)
    print(f"Текущая директория изменена на: {os.getcwd()}\n")

    print("Папки:")
    print(list_directories(path))

    print("\nФайлы:")
    print(list_files(path))

    print("\nВсе элементы:")
    print(list_all(path))

except FileNotFoundError:
    print("Указанный путь не существует.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
