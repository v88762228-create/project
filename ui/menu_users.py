from models.user import User, get_all_users
def menu_users():
    while True:
        print("=== Пользователи ===")
        print("1. Показать пользователей")
        print("2. Добавить пользователя")
        print("3. Удалить пользователя")
        print("0. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            users = get_all_users()
            for u in users:
                print(
                    f"{u.id}. {u.last_name} {u.name} | "
                    f"Логин: {u.login} | "
                    f"Email: {u.email}")
        elif choice == "2":
            user = User(
            last_name=input("Фамилия: "),
            name=input("Имя: "),
            middle_name=input("Отчество: "),
            email=input("Email: "),
            password=input("Пароль: "),
            phone=input("Телефон: "),
            login=input("Логин: "),
            role_id=int(input("RoleID: ")))
            user.save()
            print("✅ Пользователь добавлен")
        elif choice == "3":
            user = User(id=int(input("Введите ID: ")))
            user.delete()
            print("Пользователь удален")
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод")