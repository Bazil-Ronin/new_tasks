import sys
from io import StringIO

with open("new_tasks 0.2.py", "r", encoding="utf-8") as file :
    data = file.read()
    try :
        exec(data)
    except :
        e = sys.exc_info()[1]
        print('-------------------------------')
        print(f'Error: {e.args[0]}')
        print('-------------------------------')

with open("input.txt", "r", encoding="utf-8") as file, open('output.txt', 'r', encoding='utf-8') as fileout :
    data, tests, tests_out = [], {}, {}
    input_data = file.readlines()[1 :]
    output_data = fileout.readlines()[1 :]

    for i in input_data :
        if i != "\n" :
            data.append(i.rstrip())

    for i in data :
        if i.startswith("# TEST") :
            number_tests = i[2 :-1]
            tests.setdefault(number_tests, [])
        else :
            tests[number_tests].append(i)

    for k, v in tests.items() :
        tests[k] = "\n".join(v)

    data = []
    for i in output_data :
        if i != "\n" :
            data.append(i.rstrip())

    for i in data :
        if i.startswith("# TEST") :
            number_tests = i[2 :-1]
            tests_out.setdefault(number_tests, [])
        else :
            tests_out[number_tests].append(i)

    for k, v in tests_out.items() :
        tests_out[k] = "\n".join(v)

for k, v in tests.items() :
    stdout = sys.stdout
    sys.stdout = StringIO()
    try :
        exec(v)
        captured_output = sys.stdout.getvalue().strip()
        if captured_output == tests_out[k] :
            sys.stdout = stdout
            print(f'{k} done!✅')
        else :
            sys.stdout = stdout
            print(f'Error in {k}❗️')
    except :
        sys.stdout = stdout
        e = sys.exc_info()
        print('-------------------------------')
        print(f'Error in {k}❗️')
        print(f'{e}')
        print('-------------------------------')