from datetime import datetime
data = {}
with open('/Users/bazil/Desktop/diary.txt', 'r', encoding='utf-8') as input_file, open('/Users/bazil/Desktop/new_diary.txt', 'w', encoding='utf-8') as output_file:
    for line in input_file:
        if datetime.strptime(line, '%d.%m.%Y; %H:%M\n'):
            print(line)
        else:
            print('1')
