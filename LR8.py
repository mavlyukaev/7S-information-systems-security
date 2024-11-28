import hashlib
from tkinter import Tk, Label, Entry, Button, Text, END

# Функция для расчёта Y
def calculate_y(x, d, w):
    return (x % 100) * d + w

# Упрощённое шифрование сообщения (символы преобразуются по ключу)
def encrypt_message(message, key):
    encrypted = ''.join(chr(ord(char) + key) for char in message)
    return encrypted

# Упрощённое дешифрование сообщения
def decrypt_message(message, key):
    decrypted = ''.join(chr(ord(char) - key) for char in message)
    return decrypted

# Функция для создания подписи
def create_signature(message, key):
    hashed = hashlib.sha256((message.strip() + str(key)).encode()).hexdigest()
    print(f"[DEBUG] Созданная подпись: {hashed}")
    return hashed

# Функция для проверки подписи
def verify_signature(message, key, signature):
    expected_signature = hashlib.sha256((message.strip() + str(key)).encode()).hexdigest()
    print(f"[DEBUG] Ожидаемая подпись: {expected_signature}")
    print(f"[DEBUG] Предоставленная подпись: {signature}")
    return expected_signature == signature

# Интерфейс приложения
def run_app():
    def calculate():
        try:
            x = int(entry_x.get())
            d = int(entry_d.get())
            w = int(entry_w.get())
            y = calculate_y(x, d, w)
            label_y_result['text'] = f"Рассчитанное значение Y: {y}"
        except ValueError:
            label_y_result['text'] = "Ошибка: Проверьте входные данные!"

    def process_message():
        message = text_message.get("1.0", END).strip()
        try:
            key = int(entry_key.get())
            
            # Создаём подпись ДО шифрования
            signature = create_signature(message, key)
            entry_signature.delete(0, END)
            entry_signature.insert(END, signature)

            # Шифруем сообщение
            encrypted = encrypt_message(message, key)
            text_encrypted.delete("1.0", END)
            text_encrypted.insert(END, encrypted)

            print(f"[DEBUG] Исходное сообщение: {message}")
            print(f"[DEBUG] Зашифрованное сообщение: {encrypted}")
            print(f"[DEBUG] Ключ: {key}")

        except ValueError:
            label_verification['text'] = "Ошибка: Неверный ключ!"

    def verify_and_decrypt():
        encrypted = text_encrypted.get("1.0", END).strip()
        try:
            key = int(entry_key.get())
            signature = entry_signature.get()

            # Расшифровка сообщения
            message = decrypt_message(encrypted, key)
            print(f"[DEBUG] Расшифрованное сообщение: {message}")

            # Проверяем подпись
            is_valid = verify_signature(message, key, signature)
            label_verification['text'] = f"Подпись корректна: {is_valid}"

            # Отображаем результат
            if is_valid:
                text_decrypted.delete("1.0", END)
                text_decrypted.insert(END, message)
            else:
                text_decrypted.delete("1.0", END)
                text_decrypted.insert(END, "Подпись некорректна. Сообщение не может быть расшифровано.")
        except ValueError:
            label_verification['text'] = "Ошибка: Неверный ключ!"

    # Создание окна
    root = Tk()
    root.title("ЭЦП и Шифрование")

    # Ввод данных для расчёта Y
    Label(root, text="X (дата рождения):").grid(row=0, column=0)
    entry_x = Entry(root)
    entry_x.grid(row=0, column=1)

    Label(root, text="D (месяц рождения):").grid(row=1, column=0)
    entry_d = Entry(root)
    entry_d.grid(row=1, column=1)

    Label(root, text="W (день недели):").grid(row=2, column=0)
    entry_w = Entry(root)
    entry_w.grid(row=2, column=1)

    Button(root, text="Рассчитать Y", command=calculate).grid(row=3, column=0, columnspan=2)
    label_y_result = Label(root, text="")
    label_y_result.grid(row=4, column=0, columnspan=2)

    # Поля для шифрования и подписи
    Label(root, text="Сообщение:").grid(row=5, column=0)
    text_message = Text(root, height=4, width=40)
    text_message.grid(row=5, column=1)

    Label(root, text="Ключ:").grid(row=6, column=0)
    entry_key = Entry(root)
    entry_key.grid(row=6, column=1)

    Button(root, text="Шифровать и Подписать", command=process_message).grid(row=7, column=0, columnspan=2)

    Label(root, text="Зашифрованное сообщение:").grid(row=8, column=0)
    text_encrypted = Text(root, height=4, width=40)
    text_encrypted.grid(row=8, column=1)

    Label(root, text="Подпись:").grid(row=9, column=0)
    entry_signature = Entry(root, width=50)
    entry_signature.grid(row=9, column=1)

    # Проверка подписи и расшифровка
    Button(root, text="Проверить и Расшифровать", command=verify_and_decrypt).grid(row=10, column=0, columnspan=2)

    Label(root, text="Подтверждение подписи:").grid(row=11, column=0)
    label_verification = Label(root, text="")
    label_verification.grid(row=11, column=1)

    Label(root, text="Расшифрованное сообщение:").grid(row=12, column=0)
    text_decrypted = Text(root, height=4, width=40)
    text_decrypted.grid(row=12, column=1)

    # Запуск окна
    root.mainloop()

# Запуск приложения
if __name__ == "__main__":
    run_app()
