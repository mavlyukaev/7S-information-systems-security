# Функция для создания таблицы Трисемуса
def create_trisemus_table(key):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    table = []
    used_chars = set()

    # Добавляем уникальные символы из ключа
    for char in key:
        if char not in used_chars:
            table.append(char)
            used_chars.add(char)

    # Добавляем оставшиеся символы алфавита
    for char in alphabet:
        if char not in used_chars:
            table.append(char)

    # Возвращаем таблицу 6x6 для русского алфавита
    return [table[i:i + 6] for i in range(0, len(table), 6)]


# Функция для шифрования текста с использованием таблицы Трисемуса
def trisemus_encrypt(text, table):
    encrypted_text = ""
    for char in text:
        for row in table:
            if char in row:
                index = row.index(char)
                encrypted_text += row[(index + 1) % len(row)]  # Сдвиг вниз по таблице
                break
        else:
            encrypted_text += char  # Символы, которых нет в таблице, не меняются
    return encrypted_text


# Функция для расшифровки текста с использованием таблицы Трисемуса
def trisemus_decrypt(text, table):
    decrypted_text = ""
    for char in text:
        for row in table:
            if char in row:
                index = row.index(char)
                decrypted_text += row[(index - 1) % len(row)]  # Сдвиг вверх по таблице
                break
        else:
            decrypted_text += char  # Символы, которых нет в таблице, не меняются
    return decrypted_text


# Функция для чтения текста из файла
def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


# Функция для записи текста в файл
def write_text_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)


# Основная программа
def main():
    option = input(
        "Выберите опцию:\n1: Шифрование текста из файла\n2: Шифрование текста с клавиатуры\n3: Расшифровка текста из файла\n")

    if option == '1':
        input_file = input("Введите имя файла с текстом для шифрования: ")
        text = read_text_from_file(input_file)
    elif option == '2':
        text = input("Введите текст для шифрования: ")
    elif option == '3':
        input_file = input("Введите имя файла с текстом для расшифровки: ")
        text = read_text_from_file(input_file)
    else:
        print("Неправильная опция!")
        return

    # Ввод ключа для шифрования/расшифрования
    key = input("Введите ключ для шифрования/расшифрования (он будет отображаться): ").lower()

    if not key:
        print("Ключ не может быть пустым!")
        return

    # Создание таблицы Трисемуса на основе ключа
    table = create_trisemus_table(key)

    if option in ['1', '2']:
        # Шифрование текста
        encrypted_text = trisemus_encrypt(text, table)
        output_file = input("Введите имя файла для сохранения зашифрованного текста: ")
        write_text_to_file(output_file, encrypted_text)
        print(f"Текст успешно зашифрован и сохранен в файл: {output_file}")

    elif option == '3':
        # Расшифровка текста
        decrypted_text = trisemus_decrypt(text, table)
        print("Расшифрованный текст:", decrypted_text)


if __name__ == "__main__":
    main()
