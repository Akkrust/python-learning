filename = "secret_password_list.txt"
extension = filename[-3:]
new_password = filename.replace("secret", "hiden")

# Создаем переменные для финальных имен
new_filename = filename
new_file = new_password

# Проверяем длину: если имя РЕАЛЬНО длинное, только тогда обрезаем его
if len(filename) > 15:
    new_filename = filename[:10] + "..."

if len(new_password) > 15:
    new_file = new_password[:10] + "..."

print(filename, extension, new_password, new_filename, sep="\n")
