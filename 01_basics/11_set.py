# Словарь пользователей.
# Ключ — имя пользователя.
# Значение — отдельный словарь с навыками и ролями пользователя.
users = {
    "rustam": {
        "skills": {"Python", "SQL", "Git"},
        "roles": {"developer", "admin"}
    },
    "alex": {
        "skills": {"Python", "HTML"},
        "roles": {"developer"}
    },
    "dima": {
        "skills": {"Python", "SQL", "Docker"},
        "roles": {"developer"}
    },
    "max": {
        "skills": {"Python", "SQL"},
        "roles": {"tester"}
    }
}

# Неизменяемое множество заблокированных пользователей.
# frozenset нельзя изменить после создания.
blocked_users = frozenset({"alex"})

# Навыки, которые обязательны для участия в проекте.
required_skills = {"Python", "SQL"}

# Обязательная роль для участия в проекте.
required_role = "developer"


# Получаем множество всех пользователей из словаря users.
# set(users) берёт ключи словаря:
# {"rustam", "alex", "dima", "max"}
#
# Затем с помощью разности множеств (-)
# убираем всех заблокированных пользователей.
active_users = set(users) - blocked_users


# Перебираем всех активных пользователей.
for username in active_users:

    # Получаем данные текущего пользователя
    # из словаря users.
    user = users[username]

    # Проверяем сразу два условия:
    #
    # 1. Все обязательные навыки есть у пользователя.
    #    <= проверяет, является ли required_skills
    #    подмножеством user["skills"].
    #
    # 2. У пользователя есть необходимая роль.
    if required_skills <= user["skills"] and required_role in user["roles"]:
        print(username, "может участвовать в проекте")

    # Если обязательные навыки есть,
    # но нужной роли нет.
    elif required_skills <= user["skills"]:
        print(username, "имеет нужные навыки, но не подходит по роли")

    # Если не хватает хотя бы одного обязательного навыка.
    else:

        # Находим, каких именно навыков не хватает.
        # Разность множеств возвращает элементы,
        # которые есть в required_skills,
        # но отсутствуют в user["skills"].
        missing = required_skills - user["skills"]

        print(username, "не хватает навыков:", missing)


# Создаём пустое множество.
# Сюда позже соберём все навыки активных пользователей.
project_skills = set()


# Перебираем всех активных пользователей.
for username in active_users:

    # Объединяем уже собранные навыки
    # с навыками текущего пользователя.
    #
    # |= означает:
    # project_skills = project_skills | users[username]["skills"]
    #
    # Благодаря set одинаковые навыки
    # автоматически не дублируются.
    project_skills |= users[username]["skills"]


# Выводим все уникальные навыки активных пользователей.
print("Навыки проекта:", project_skills)