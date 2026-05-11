from models.priority import Priority, get_all_priorities
def menu_priorities():
    while True:
        print("=== Приоритеты ===")
        print("1. Показать приоритеты")
        print("2. Добавить приоритет")
        print("3. Удалить приоритет")
        print("0. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            priorities = get_all_priorities()
            for p in priorities:
                print(
                    f"{p.id}. Пользователь ID: {p.user_id} | "
                    f"Задача ID: {p.task_id} | "
                    f"Приоритет: {p.priority_name}")
        elif choice == "2":
            priority = Priority(
            user_id=int(input("ID пользователя: ")),
            task_id=int(input("ID задачи: ")),
            priority_name=input("Название приоритета: "))
            priority.save()
            print("✅ Приоритет добавлен")
        elif choice == "3":
            priority = Priority(id=int(input("Введите ID приоритета: ")))
            priority.delete()
            print("Приоритет удален")
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод")