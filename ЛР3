import random
import math

# Функция для вычисления нижней границы S*
def calculate_S(P, V, T):
    return (V * T) / P

# Функция для расчета минимальной длины пароля L
def calculate_L(S, A):
    return math.ceil(math.log(S) / math.log(A))

# Функция для генерации пароля
def generate_password(length, alphabet):
    return ''.join(random.choice(alphabet) for _ in range(length))

# Основная программа
def main():
    # Ввод значений P, V, T
    P = float(input("Введите P (вероятность успешного взлома): "))
    V = float(input("Введите V (количество паролей в день): "))
    T = float(input("Введите T (количество дней): "))

    # Вычисление нижней границы S*
    S_star = calculate_S(P, V, T)
    print(f"Нижняя граница S* = {S_star}")

    # Определяем алфавит: английские буквы, цифры, специальные символы
    alphabet = (
            [chr(i) for i in range(65, 91)] +  # Заглавные буквы
            [chr(i) for i in range(97, 123)] +  # Строчные буквы
            [chr(i) for i in range(48, 58)] +  # Цифры
            ['!', '"', '#', '$', '%', '&', "'"]  # Специальные символы
    )

    # Мощность алфавита
    A = len(alphabet)
    print(f"Мощность алфавита A = {A}")

    # Вычисление минимальной длины пароля L
    L = calculate_L(S_star, A)

    # Принудительное увеличение длины пароля, если она меньше минимальной
    MIN_PASSWORD_LENGTH = 10
    if L < MIN_PASSWORD_LENGTH:
        L = MIN_PASSWORD_LENGTH

    print(f"Минимальная длина пароля L = {L}")

    # Генерация пароля
    password = generate_password(L, alphabet)
    print(f"Сгенерированный пароль: {password}")

# Запуск программы
if __name__ == "__main__":
    main()
