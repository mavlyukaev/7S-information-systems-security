import tkinter as tk
from tkinter import filedialog, messagebox
import random
from math import gcd
import os


# RSA вспомогательные функции
def mod_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2, x1 = x1, x
        d, y1 = y1, y

    if temp_phi == 1:
        return d + phi


def is_prime(num):
    if num < 2:
        return False
    for _ in range(5):
        a = random.randint(2, num - 1)
        if gcd(a, num) != 1 or pow(a, num - 1, num) != 1:
            return False
    return True


def generate_prime_candidate(length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length=8):
    p = 4
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p


def generate_keys():
    prime_length = 8
    p = generate_prime_number(prime_length)
    q = generate_prime_number(prime_length)

    while p == q:
        q = generate_prime_number(prime_length)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))


def encrypt_block(block, public_key):
    e, n = public_key
    return pow(block, e, n)


def decrypt_block(block, private_key):
    d, n = private_key
    return pow(block, d, n)


# UI Функции
def generate_keys_ui():
    global public_key, private_key
    public_key, private_key = generate_keys()
    pub_key_label.config(text=f"Публичный ключ: {public_key}")
    priv_key_label.config(text=f"Приватный ключ: {private_key}")
    messagebox.showinfo("Успех", "Ключи успешно сгенерированы!")


def encrypt_text_ui():
    global public_key
    if not public_key:
        messagebox.showerror("Ошибка", "Сначала сгенерируйте ключи!")
        return

    plaintext = plaintext_entry.get("1.0", tk.END).strip()
    if not plaintext:
        messagebox.showerror("Ошибка", "Введите текст для шифрования!")
        return

    ciphertext = [encrypt_block(ord(char), public_key) for char in plaintext]
    ciphertext_entry.delete("1.0", tk.END)
    ciphertext_entry.insert(tk.END, str(ciphertext))
    messagebox.showinfo("Успех", "Текст успешно зашифрован!")


def decrypt_text_ui():
    global private_key
    if not private_key:
        messagebox.showerror("Ошибка", "Сначала сгенерируйте ключи!")
        return

    ciphertext = ciphertext_entry.get("1.0", tk.END).strip()
    if not ciphertext:
        messagebox.showerror("Ошибка", "Введите зашифрованный текст для дешифрования!")
        return

    try:
        ciphertext = list(map(int, ciphertext.strip("[]").split(",")))
        plaintext = ''.join(chr(decrypt_block(char, private_key)) for char in ciphertext)
        plaintext_entry.delete("1.0", tk.END)
        plaintext_entry.insert(tk.END, plaintext)
        messagebox.showinfo("Успех", "Текст успешно расшифрован!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось расшифровать текст: {e}")


def encrypt_image_ui():
    global public_key
    if not public_key:
        messagebox.showerror("Ошибка", "Сначала сгенерируйте ключи!")
        return

    file_path = filedialog.askopenfilename(title="Выберите изображение", filetypes=[("Изображения", "*.png;*.jpg;*.bmp")])
    if not file_path:
        return

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted_data = [encrypt_block(byte, public_key) for byte in data]

    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "w") as f:
        f.write(",".join(map(str, encrypted_data)))

    messagebox.showinfo("Успех", f"Файл зашифрован и сохранён как: {encrypted_file_path}")


def decrypt_image_ui():
    global private_key
    if not private_key:
        messagebox.showerror("Ошибка", "Сначала сгенерируйте ключи!")
        return

    file_path = filedialog.askopenfilename(title="Выберите зашифрованный файл", filetypes=[("Зашифрованные файлы", "*.enc")])
    if not file_path:
        return

    with open(file_path, "r") as f:
        encrypted_data = list(map(int, f.read().split(",")))

    decrypted_data = bytearray([decrypt_block(byte, private_key) for byte in encrypted_data])

    original_file_path = file_path.replace(".enc", ".decrypted")
    with open(original_file_path, "wb") as f:
        f.write(decrypted_data)

    messagebox.showinfo("Успех", f"Файл расшифрован и сохранён как: {original_file_path}")


# Интерфейс tkinter
root = tk.Tk()
root.title("RSA Encryptor/Decryptor")
root.geometry("600x600")

# Кнопка для генерации ключей
generate_button = tk.Button(root, text="Сгенерировать ключи", command=generate_keys_ui)
generate_button.pack(pady=10)

# Отображение ключей
pub_key_label = tk.Label(root, text="Публичный ключ: (None)")
pub_key_label.pack()
priv_key_label = tk.Label(root, text="Приватный ключ: (None)")
priv_key_label.pack()

# Шифрование и дешифрование текста
tk.Label(root, text="Шифрование текста").pack(pady=5)
plaintext_entry = tk.Text(root, height=5, width=60)
plaintext_entry.pack(pady=5)

encrypt_text_button = tk.Button(root, text="Зашифровать текст", command=encrypt_text_ui)
encrypt_text_button.pack(pady=5)

ciphertext_entry = tk.Text(root, height=5, width=60)
ciphertext_entry.pack(pady=5)

decrypt_text_button = tk.Button(root, text="Расшифровать текст", command=decrypt_text_ui)
decrypt_text_button.pack(pady=5)

# Шифрование и дешифрование изображений
tk.Label(root, text="Шифрование изображений").pack(pady=10)
encrypt_image_button = tk.Button(root, text="Зашифровать изображение", command=encrypt_image_ui)
encrypt_image_button.pack(pady=5)

decrypt_image_button = tk.Button(root, text="Расшифровать изображение", command=decrypt_image_ui)
decrypt_image_button.pack(pady=5)

# Запуск окна
root.mainloop()
