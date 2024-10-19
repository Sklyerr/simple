# Словарь для хранения списка задач
tasks = []

# Функция для вывода меню
def print_menu():
    print("\nЕжедневные задачи:")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Отметить задачу как выполненную")
    print("4. Очистить список задач")
    print("5. Выйти")

# Функция для показа задач
def show_tasks():
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Текущие задачи:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Функция для добавления задачи
def add_task():
    new_task = input("Введите новую задачу: ")
    tasks.append(new_task)
    print("Задача добавлена.")

# Функция для отметки задачи как выполненной
def complete_task():
    show_tasks()
    if tasks:
        task_idx = int(input("Введите номер задачи для отметки выполненной: ")) - 1
        if 0 <= task_idx < len(tasks):
            print(f"Задача '{tasks[task_idx]}' отмечена как выполненная.")
            del tasks[task_idx]
        else:
            print("Неверный номер задачи.")
    else:
        print("Список задач пуст.")

# Основной цикл программы
while True:
    print_menu()
    choice = input("Выберите действие (1-5): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        tasks = []
        print("Список задач очищен.")
    elif choice == '5':
        print("Выход из программы.")
        break
    else:
        print("Неверный ввод. Попробуйте еще раз.")
