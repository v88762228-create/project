from models.comment import Comment, get_comments_by_task
from datetime import datetime
def menu_comments():
    while True:
        print("=== Комментарии ===")
        print("1. Показать комментарии задачи")
        print("2. Добавить комментарий")
        print("0. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            task_id = int(input("Введите ID задачи: "))
            comments = get_comments_by_task(task_id)
            for c in comments:
                print(
                    f"{c.id}. Пользователь ID: {c.user_id} | "
                    f"{c.comment_text}")
        elif choice == "2":
            comment = Comment(
            user_id=int(input("ID пользователя: ")),
            create_date=datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"),
            task_id=int(input("ID задачи: ")),
            comment_text=input("Текст комментария: "))
            comment.save()
            print("✅ Комментарий добавлен")
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод")