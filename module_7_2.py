
def custom_write(file_name: str, strings):
    strings_position = dict()
    with open(file_name, 'a+', encoding='utf-8') as file_:
        for line, string in enumerate(strings, 1):
            cursor = file_.tell()
            file_.write(f'{string}\n')
            strings_position[(line, cursor)] = string
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
