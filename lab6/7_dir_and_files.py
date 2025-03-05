source_file = 'C:\Users\Ерасыл\Desktop\НУ\lab6\source.txt'
destination_file = 'C:\Users\Ерасыл\Desktop\НУ\lab6\destination.txt'

try:
    # Открываем исходный файл для чтения
    with open(source_file, 'r', encoding='utf-8') as src:
        # Читаем содержимое файла
        content = src.read()
    
    # Открываем целевой файл для записи
    with open(destination_file, 'w', encoding='utf-8') as dest:
        # Записываем содержимое в целевой файл
        dest.write(content)
    
    print(f"Содержимое из '{source_file}' успешно скопировано в '{destination_file}'.")
except FileNotFoundError:
    print(f"Файл '{source_file}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
