from models.status import TaskStatus, get_all_statuses
def menu_statuses():
    while True:
        print("=== Статусы задач ===")
        print("1. Показать статусы")
        print("2. Добавить статус")
        print("3. Удалить статус")
        print("0. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            statuses = get_all_statuses()
            for s in statuses:
                print(
                    f"{s.id}. Пользователь ID: {s.user_id} | "
                    f"Задача ID: {s.task_id} | "
                    f"Статус: {s.status_name}")
        elif choice == "2":
            status = TaskStatus(
            user_id=int(input("ID пользователя: ")),
            task_id=int(input("ID задачи: ")),
            status_name=input("Название статуса: "))
            status.save()
            print("✅ Статус добавлен")
        elif choice == "3":
            status = TaskStatus(id=int(input("Введите ID статуса: ")))
            status.delete()
            print("Статус удален")
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод")