from database.db_manager import initialize_db
from ui.menu import show_main_menu
from ui.menu_tasks import menu_tasks
from ui.menu_users import menu_users
from ui.menu_comments import menu_comments
from ui.menu_statuses import menu_statuses
from ui.menu_priorities import menu_priorities
def main():
    initialize_db()
    while True:
        user_choice = show_main_menu()
        if user_choice == "1":
            menu_tasks()
        elif user_choice == "2":
            menu_users()
        elif user_choice == "3":
            menu_comments()
        elif user_choice == "4":
            menu_statuses()
        elif user_choice == "5":
            menu_priorities()
        elif user_choice == "0":
            print("Выход из программы")
            break
        else:
            print("❌ Неверный ввод")
if __name__ == "__main__":
    main()