# P3: Write a table from 2 to 20 and store all in different folders

import os

def generateTable(n):
    table = ""

    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    # Ensure the directory exists before writing the file
    folder_path = "P3"
    os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist

    file_path = os.path.join(folder_path, f"table_{n}.txt")  # Correct path format

    with open(file_path, 'w') as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)
