from models.task import Task, get_all_tasks, get_task_by_id
from datetime import datetime
def menu_tasks():
    while True:
        print("\n=== Задачи ===")
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Изменить задачу")
        print("0. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            tasks = get_all_tasks()
            print("\nСписок задач:")
            for t in tasks:
                print(
                    f"{t.id}. {t.task_name} | "
                    f"Исполнитель ID: {t.users_id} | "
                    f"Создана: {t.create_date} | "
                    f"Срок: {t.deadline} | "
                    f"Статус ID: {t.status_id} | "
                    f"Приоритет ID: {t.priority_id}"
                    )
        elif choice == "2":
            task_name = input("Название задачи: ")
            users_id = int(input("ID исполнителя: "))
            deadline = input("Срок выполнения: ")
            status_id = int(input("ID статуса: "))
            priority_id = int(input("ID приоритета: "))
            create_date = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")
            task = Task(
            task_name=task_name,
            users_id=users_id,
            create_date=create_date,
            deadline=deadline,
            status_id=status_id,
            priority_id=priority_id)
            task.save()
            print("✅ Задача добавлена")
        elif choice == "3":
            task_id = int(input("Введите ID задачи: "))
            task = Task(id=task_id)
            task.delete()
            print("Задача удалена")
        elif choice == "4":
            task_id = int(input("Введите ID задачи: "))
            current_task = get_task_by_id(task_id)
            if not current_task:
                print("❌ Задача не найдена")
                continue
            task_name = input("Новое название: ")
            deadline = input("Новый срок: ")
            print("Оставьте поле пустым, если не хотите изменять значение")
            task = Task(
            id=task_id,
            task_name=task_name if task_name else current_task.task_name,
            users_id=current_task.users_id,
            create_date=current_task.create_date,
            deadline=deadline if deadline else current_task.deadline,
            status_id=current_task.status_id,
            priority_id=current_task.priority_id)
            task.save()
            print("✅ Задача обновлена")
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод")