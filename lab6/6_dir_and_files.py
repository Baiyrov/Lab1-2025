import string

# Генерация 26 текстовых файлов с именами A.txt до Z.txt
for letter in string.ascii_uppercase:  # Цикл по буквам от 'A' до 'Z'
    file_name = f"{letter}.txt"  # Создаём имя файла
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"Это файл {file_name}\n")  # Записываем текст в файл
        print(f"Создан файл: {file_name}")
    except Exception as e:
        print(f"Ошибка при создании файла {file_name}: {e}")
