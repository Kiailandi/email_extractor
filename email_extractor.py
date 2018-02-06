import re

input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')
for line in input_file:
    match = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', line)
    for item in match:
        output_file.write(item + ';' + '\n')
input_file.close()
output_file.close()

