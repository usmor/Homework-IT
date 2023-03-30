# Данные для кодирования
cyr_code_morse = {'а': '·-', 'б': '-···', 'в': '·--', 'г': '--·', 'д': '-··', 'е': '·', 'ж': '···-',
                  'з': '--··', 'и': '··', 'й': '·---', 'к': '-·-', 'л': '·-··', 'м': '--', 'н': '-·',
                  'о': '---', 'п': '·--·', 'р': '·-·', 'с': '···', 'т': '-', 'у': '··-', 'ф': '··-·',
                  'х': '····', 'ц': '-·-·', 'ч': '---·', 'ш': '----', 'щ': '--·-', 'ъ': '·--·-·', 'ы': '-·--',
                  'ь': '-··-', 'э': '··-··', 'ю': '··--', 'я': '·-·-'}

lat_code_morse = {'a': '·-', 'b': '-···', 'c': '-·-·', 'd': '-··', 'e': '·', 'f': '··-·', 'g': '--·',
                  'h': '····', 'i': '··', 'j': '·---', 'k': '--·--', 'l': '·-··', 'm': '--', 'n': '-·',
                  'o': '---', 'p': '·--·', 'q': '--·-', 'r': '·-·', 's': '···', 't': '-', 'u': '··-',
                  'v': '···-', 'w': '·--', 'x': '-··-', 'y': '-·--', 'z': '--··'}

num_and_other_sym = {'0': '-----', '1': '·----', '2': '··---', '3': '···--', '4': '····-', '5': '·····',
                     '6': '-····', '7': '--···', '8': '---··', '9': '----·', '·': '·-·-·-', ',': '--··--',
                     '?': '··--··', "'": '·----·', '!': '-·-·--', '/': '-··-·', '(': '-·--·', ')': '-·--·-',
                     '&': '·-···', ':': '---···', ';': '-·-·-·', '=': '-···-', '+': '·-·-·', '-': '-····-',
                     '_': '··--·-', '"': '·-··-·', '$': '···-··-', '@': '·--·-·', '¿': '··-·-', '¡': '--···-',
                     '×': '-··-', '%': '----- -··-· -----', }


def get_cyr_symbols():
    cyr_code_morse_reverse = dict(zip(cyr_code_morse.values(), cyr_code_morse.keys()))
    for symbol in range(0, len(message)):
        if message[symbol] not in cyr_code_morse_reverse.keys():
            continue
        message[symbol] = cyr_code_morse_reverse[message[symbol]]
    return get_other_symbols()


def get_lat_symbols():
    lat_code_morse_reverse = dict(zip(lat_code_morse.values(), lat_code_morse.keys()))
    for symbol in range(0, len(message)):
        if message[symbol] not in lat_code_morse_reverse.keys():
            continue
        message[symbol] = lat_code_morse_reverse[message[symbol]]
    return get_other_symbols()


def get_other_symbols():
    num_and_other_sym_reverse = dict(zip(num_and_other_sym.values(), num_and_other_sym.keys()))
    for symbol in range(0, len(message)):
        if message[symbol] not in num_and_other_sym_reverse.keys():
            continue
        message[symbol] = num_and_other_sym_reverse[message[symbol]]
    return message


function = input("Выберите режим работы: кодировать/раскодировать.\n").lower()

if function == 'кодировать':
    message = input("Введите сообщение: \n").lower().replace("ё", "е")

elif function == 'раскодировать':
    message = input("Введите сообщение. Допустимые символы: точка и дефис.\n"
                    "Слова должны быть разделены табуляцией, символы -- пробелами.\n"
                    "Убедитесь в правильности вашего сообщения.\nТе последовательности, которые не соотвествуют "
                    "символам азбуки Морза не будут переведены. \n").replace('.', '·')

    while not set(message) <= {'.', '-', ' ', '\t', '·'}:
        print("Ваше сообщение содержит недопустимые символы.")
        message = input("Введите сообщение. Допустимые символы: точка и дефис.\n"
                        "Слова должны быть разделены табуляцией, символы -- пробелами.\n"
                        "Убедитесь в правильности вашего сообщения.\nТе последовательности, которые не соотвествуют "
                        "символам азбуки Морза не будут переведены. \n").replace('.', '·')

    message = message.split(' ')
    for element in range(0, len(message)):
        if message[element] != '':
            continue
        else:
            message[element] = ' '

    language = input("Выберите алфавит для дальнейшей записи: кириллица/латиница.\n").lower()
    if language == 'латиница':
        get_lat_symbols()
    elif language == 'кириллица':
        get_cyr_symbols()

    print(''.join(message))
