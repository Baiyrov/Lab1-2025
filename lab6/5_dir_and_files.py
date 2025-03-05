# Specify the file name
file_path = r'C:\Users\Ерасыл\Desktop\НУ\lab6\output.txt'

# Define the list
data = ['Python', 'is', 'fun!', 'Write', 'this', 'list', 'to', 'a', 'file.']

# Write the list to the file
try:
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"{item}\n")  # Write each item on a new line
    print(f"List has been written to '{file_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")
