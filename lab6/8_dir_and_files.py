import os

def delete_file(file_path):
    """Удаляет файл, если он существует и доступен."""
    try:
        # Проверяем, существует ли файл
        if not os.path.exists(file_path):
            print(f"Файл не найден: {file_path}")
            return
        
        # Проверяем доступ к файлу
        if not os.access(file_path, os.R_OK):
            print(f"Файл недоступен для чтения: {file_path}")
            return
        if not os.access(file_path, os.W_OK):
            print(f"Файл недоступен для удаления: {file_path}")
            return
        
        # Удаляем файл
        os.remove(file_path)
        print(f"Файл успешно удалён: {file_path}")
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример пути к файлу
file_path = r'C:\Users\Ерасыл\Desktop\НУ\lab6\example.txt'

# Удаление файла
delete_file(file_path)
