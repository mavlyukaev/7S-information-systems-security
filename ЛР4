import os
import subprocess

# Функция для получения текущего имени пользователя
def get_username():
    return os.getlogin()

# Функция для получения серийного номера диска
def get_disk_serial_number(drive_letter):
    try:
        # Выполняем команду 'vol' для получения серийного номера
        result = subprocess.check_output(f"vol {drive_letter}:", shell=True, text=True)
        # Серийный номер последнего пользователя
        serial_number = result.split()[-1]
        return serial_number
    except Exception as e:
        print(f"Ошибка при получении серийного номера диска: {e}")
        return None

# Функция для проверки компьютера по имени пользователя и серийному номеру диска
def check_computer(username_ref, serial_ref):
    # Получаем текущее имя пользователя
    current_username = get_username()
    # Получаем текущий серийный номер диска
    current_serial = get_disk_serial_number("C")

    # Сравниваем с эталонными значениями
    if current_username == username_ref and current_serial == serial_ref:
        print("Программа запущена на разрешенном компьютере.")
        return True
    else:
        print("Ошибка: Я вас не знаю.")
        return False

# Эталонные значения имени пользователя и серийного номера диска (их нужно сохранить при первой настройке)
username_reference = "s0163603"
serial_reference = "F4FD-11E3"

# Проверяем компьютер
if check_computer(username_reference, serial_reference):
    # Основная логика программы
    print("Доступ разрешен, программа выполняется...")
else:
    # Выход из программы
    print("Доступ запрещен.")
