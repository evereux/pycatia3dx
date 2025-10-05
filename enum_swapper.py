import os
from pathlib import Path

source_folder = Path(os.getcwd(), 'pycatia3dx', 'sma_spa_structural')

def look_up(string, list_of_words):
    string = string.replace(':', '')
    string = string.replace('(', ' ')
    string = string.replace(')', ' ')
    return ','.join(j for j in string.split() if j in list_of_words)

if not source_folder.is_dir():
    raise NotADirectoryError('directory does not exist')

print(source_folder)

enum_file = Path(source_folder, 'enums.py')

if not enum_file.is_file():
    raise FileNotFoundError('file does not exist')

enum_contents = enum_file.read_text()
enums = []
for line in enum_contents.splitlines():
    if line[0].isalpha():
        name = line.split(' =')[0]
        enums.append(name)

files = source_folder.glob('*.py')
for file in files:
    print(f'working on {file}')
    if file.name == '__init__.py' or file.name == 'enums.py':
        continue

    with open(file, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    for line in lines:
        r = look_up(line, enums)
        if r:
            not_replaced = True
            if ':param' in line or '    def' in line:
                print(line)
                modified_lines.append(line.replace(r, 'int'))
                not_replaced = False
            if '        return' in line:
                new_line = line.replace(r + '(', '')
                new_line = new_line.rstrip()[:-1]
                new_line = new_line + '\n'
                modified_lines.append(new_line)
                not_replaced = False
            if not_replaced:
                modified_lines.append(line)
        else:
            modified_lines.append(line)

    with open(file, 'w') as f:
        f.writelines(modified_lines)