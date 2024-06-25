with open('requirements.txt', 'r') as file:
    lines = file.readlines()

processed_lines = [line.split(' @ ')[0] + '\n' for line in lines]

with open('requirements.txt', 'w') as file:
    file.writelines(processed_lines)