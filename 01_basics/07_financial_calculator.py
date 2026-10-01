expenses = []
while True:
    user_input = int(input("Сумма расхода в долларах (или 0 для завершения): "))
    if user_input == 0:
        break
    # ЭТА СТРОКА ДОЛЖНА БЫТЬ ВНУТРИ ЦИКЛА (с отступом), чтобы сохранять каждую трату!
    expenses.append(user_input)

total_expenses = 0
for expense in expenses:
    total_expenses += expense

# ЭТОТ PRINT ДОЛЖЕН БЫТЬ ВНЕ ЦИКЛА FOR (без отступа), чтобы выполниться один раз в конце
print("Всего зафиксировано трат:", len(expenses), "На общую сумму:", total_expenses)

income = int(input("Введите грязный доход: "))

# ФИНАЛЬНЫЙ ШАГ: Считаем налог и чистую прибыль
tax = income * 0.06
clean_profit = income - total_expenses - tax

print("Налог (6%):", tax)
print("Чистая прибыль:", clean_profit)

# Твой любимый тернарный оператор для вердикта:
status = "Ты в плюсе! Работаем дальше." if clean_profit > 0 else "Твои подписки сжирают весь доход. Срочно ищи новые заказы!"
print(status)
