import random

# Все доступные символы для генерации
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

# Запрос длины пароля у пользователя
length = int(input("Enter password length: "))

# Пустая строка, куда по очереди будут добавляться символы
password = ""

# Цикл повторяется столько раз, сколько указал пользователь
for i in range(length):
    password = password + random.choice(chars)

# Вывод готового результата
print("Your secure password:", password)
