from random import random, randint
from typing import Optional


def give_int(input_string: str,
             min_num: Optional[int] = None) -> int:
 

    while True:
        try:
            num = int(input(input_string))
            if min_num and num <= min_num:
                print(f'Введите число больше, чем {min_num}!')
                continue
            return num
        except ValueError:
            print("Это не нутуральное число.")


def random_list(list_len: int) -> list:


    data_list = list()
    for i in range(list_len):
        data_list.append(randint(-10, 10))
    return data_list


def random_list_float(list_len: int) -> list:


    data_list = list()
    for i in range(list_len):
        data_list.append(round(random() - randint(-10, 10), 4))
    return data_list


from os import path


def create_file() -> None:

    amount = give_int('Введите кол-во студентов: ', 1)
    with open('students.txt', 'w', encoding='UTF8') as file:
        for _ in range(amount):
            name = input("Введите имя студента: ")
            file.write(f'{name} ')
            while True:
                grade = input(f"Средний балл {name}: ")
                if grade.isdigit() and 0 < int(grade) <= 5:
                    file.write(f'{grade}\n')
                    break
                else:
                    print('Введите число от 1 до 5')
                    continue
    return print("Success!\nYou have created students.txt\n")


def edit_file(file_name: str, grade: int) -> None:

    with open(file_name, 'r', encoding='UTF8') as file:
        lines_data = []
        for line in file.readlines():
            data_string = line.strip('\n')
            try:
                student_grade = int(data_string[-1])
            except ValueError:
                exit(f"Error: 0x80002020 Student's grade is missing.\n"
                     f"Try to edit {file_name} manually or contact your system administrator.")
            if student_grade >= grade:
                lines_data.append(data_string.upper() + '\n')
            else:
                lines_data.append(data_string + '\n')
    with open(file_name, 'w', encoding='UTF8') as file:
        for i in lines_data:
            file.write(i)
    return print("Success!\nYou have edited students.txt\n")


def menu_input():
 
    while True:
        print('Выберите "1" для нового файла')
        print('Выберите "2" для редактирования существующего файла')
        print('Выберите "0" для выхода')
        num = input('Какую команду выполнить?: ')
        if num == '1':
            create_file()
        elif num == '2':
            if path.exists(fr'.\students.txt'):
                edit_file('students.txt', 4)
            else:
                print('Файл students.txt не существует.')
                print("Хотите создать файл? (Y/N)")
                if input().lower() in ('y', 'ye', 'yes'):
                    create_file()
                else:
                    print("Создайте папку student.txt\n")
        elif num == '0':
            return exit(print("До встречи."))
        else:
            print("Неверное значение, повторите попытку!")


menu_input()