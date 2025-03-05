file_path = r'C:\Users\Ерасыл\Desktop\НУ\lab6\example.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"Количество строк: {len(lines)}")
