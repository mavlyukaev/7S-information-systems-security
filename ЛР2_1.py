# Функция для шифрования текста по методу двойной перестановки
def double_transposition_encrypt(text, key):
    print("Начало шифрования...")

    # Удаление пробелов и проверка длины ключа
    text = text.replace(' ', '')  # Удаляем пробелы из текста для корректной работы
    if len(key) > len(text):
        print("Ошибка: длина ключа больше длины текста!")
        return ""

    # Рассчитываем количество строк и столбцов
    columns = len(key)
    rows = len(text) // columns
    if len(text) % columns != 0:
        rows += 1

    print(f"Текст будет разбит на {rows} строк и {columns} столбцов.")

    # Формируем сетку для текста (добавляем пустые символы для завершения строк)
    grid = [''] * rows
    for i in range(len(text)):
        row = i // columns
        col = i % columns
        grid[row] += text[i]

    print("Сетка после первой перестановки строк:", grid)

    # Применение ключа (перестановка столбцов)
    transposed_grid = [''] * rows
    for row in range(rows):
        new_row = [''] * columns
        for i, col in enumerate(sorted(list(key))):
            key_index = key.index(col)
            if key_index < len(grid[row]):
                new_row[i] = grid[row][key_index]
        transposed_grid[row] = ''.join(new_row)

    print("Сетка после перестановки столбцов:", transposed_grid)

    # Собираем финальный зашифрованный текст
    encrypted_text = ''.join(transposed_grid)
    print("Зашифрованный текст (перед возвращением):", encrypted_text)

    return encrypted_text


# Ввод текста и ключа
def main():
    choice = input("1: Шифрование текста из файла\n2: Шифрование текста с клавиатуры\nВыберите опцию: ")

    if choice == '1':
        input_file = input("Введите имя файла для шифрования: ")
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    elif choice == '2':
        text = input("Введите текст для шифрования: ")
    else:
        print("Неправильный выбор!")
        return

    print("Текст для шифрования:", text)

    # Ввод ключа с использованием обычного input() вместо getpass.getpass()
    key = input("Введите ключ шифрования: ")

    if not key:
        print("Ключ не может быть пустым!")
        return

    print("Ключ для шифрования:", key)

    # Шифрование
    encrypted_text = double_transposition_encrypt(text, key)

    if encrypted_text:
        # Сохранение результата в файл
        output_file = input("Введите имя файла для сохранения зашифрованного текста: ")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encrypted_text)

        print(f"Текст успешно зашифрован и сохранен в файл: {output_file}")
    else:
        print("Произошла ошибка при шифровании!")


if __name__ == "__main__":
    main()
