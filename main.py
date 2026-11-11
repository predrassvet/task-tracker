from db import init_db, get_all_tasks, add_task_to_db, mark_done, delete_task
    
init_db()   # создание базы данных и таблицы при запуске программы

def add_task_menu():
    user_task = input("Введите задачу:")
    user_deadline = input("Введите дедлайн:")
    add_task_to_db(user_task, user_deadline)
    print("Задача добавлена!")

def show_task_menu():
    tasks = get_all_tasks()
    for task_id, task_name, deadline, done in tasks:
        print(f"task_id: {task_id} Task - {task_name}, Deadline: {deadline}, Done: {'[x]' if done == 1  else '[]'}")

def choose_task_menu():
    tasks = get_all_tasks()
    list_id = []
    for task in tasks:
        list_id.append(task[0])
    while True:
        try:
            user_get = int(user_input())
            if user_get in list_id:
                return user_get
            else:
                print("Нет такого номера!")
        except (ValueError,TypeError) as e:
            print(f'Error: {e}')
            continue

def delete_task_menu(number):
    delete_task(number)
    print("Готово!")

def task_done_menu(number):
    mark_done(number)
    print("Готово!")

def user_input(text="Ввод: "):
    return input(text)

def print_menu():
    print("     Меню выбора    ")
    print("1. Добавить задачу.")
    print("2. Показать все задачи.")
    print("3. Выбрать задачу.")
    print("0. Выход.")

def print_menu_choice():
    print("Что хотите сделать с выбранной задачей?")
    print("1. Отметить задачу выполненной.")
    print("2. Удалить задачу.")
    print("0. Выход с меню выбора.")

def main():
    while True:
        print_menu()
        user = user_input()
        if  user == "1":                                     
            while True:
                add_task_menu()
                print("Хотите добавить еще задачу?  \n")
                if user_input("[да|нет]: ").lower() == "да":
                    continue
                else:
                    break
        elif user == "2":
            if len(get_all_tasks()) == 0:
                print("Нет задач")
            else:
                show_task_menu()
                input("Нажмите Enter для выхода")
        elif user == "3":
            while True:
                try:
                    tasks = get_all_tasks()
                    if len(tasks) == 0:
                        print("Нет задач")
                        break
                    show_task_menu()
                    number = choose_task_menu()
                    print_menu_choice()
                    user = user_input()
                    if user == "1":
                        task_done_menu(number)
                    elif user == "2":
                        delete_task_menu(number)
                    elif user == "0":
                        break
                    else:
                        print("Нет такого номера")
                except (ValueError, TypeError) as e:
                    print(f'Error {e}')
                    break
                print("Выбрать еще задачу? \n")
                if user_input("[да|нет]: ").lower() == "да":
                    continue
                else:
                    break
        elif user == "0":
            print("До новых встреч!")
            break
        else:
            print("Такого номера нет!")
            continue

if __name__ == "__main__":
    main()
