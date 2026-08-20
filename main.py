import json
import sys
from datetime import datetime
import os

# функция для проверки ввода
def safe_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка! Введите число.")

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # получение текущей даты и времени

file_name_training_program = f"training_{timestamp}.txt"

# загрузка готовых программ из файла
with open("programs.json", "r", encoding="utf-8") as f:
    programs = json.load(f)

choosing_training_program = safe_int_input("Выберите гоовую программу тренировок или создайте свою(введите '1' для создания своей программы или '2' для выбора готовой) ")
while choosing_training_program != 1 and choosing_training_program != 2:
    print("Введите '1' или '2'")
    choosing_training_program = safe_int_input("Выберите гоовую программу тренировок или создайте свою(введите '1' для создания своей программы или '2' для выбора готовой) ")

if choosing_training_program == 1:
    list_of_exercises = input("Введите название упражнения или 'нет' для выхода: ")
    with open (file_name_training_program, "a", encoding="utf-8") as file:
        file.write("--- Своя программа! --- \n")
    while list_of_exercises != "нет":
        weight = safe_int_input("Введите рабочий вес: ")  # вес снаряда
        number_of_approaches = safe_int_input("Введите количество подходов: ")  # подходы
        number_of_repetitions = safe_int_input("Введите количество повторений: ")  # повторения

        # запись в файл
        with open(file_name_training_program, "a", encoding="utf-8") as file:
            file.write(f"{list_of_exercises} - {weight}кг, {number_of_approaches} на {number_of_repetitions} \n")

        print("Упражение добавлено")
        list_of_exercises = input("Введите название упражнения или 'нет' для выхода: ")

    print("Тренировка сохранена")

if choosing_training_program == 2:
    print("\nДоступные программы тренировок:")
    for key, program in programs.items(): # чтение готовых программ тренировок
        print(f"{key}. {program['name']} ({', '.join(program['exercises'])})")

    choice = input("Выберите номер программы (или 'нет' для выхода): ")

    while choice not in programs:
        if choice == "нет":
            print("До встречи!")
            sys.exit(0)
        print("Неправильный номер программы. Попробуйте еще раз.")
        choice = input("Выберите номер программы (или 'нет' для выхода): ")

    selected_program = programs[choice]
    print(f"\nВы выбрали программу: {selected_program['name']}")

    with open (file_name_training_program, "a", encoding="utf-8") as file:
        file.write(f"--- {selected_program['name']} ---\n")
        for exercise in selected_program['exercises']:
            print(f"\n Упражнение: {exercise}")
            weight = safe_int_input("  Введите рабочий вес (кг): ")
            approaches = safe_int_input("  Введите количество подходов: ")
            repetitions = safe_int_input("  Введите количество повторений: ")
            file.write(f"{exercise} - {weight}кг, {approaches} на {repetitions}\n")
            print(f"{exercise} сохранено!")
    print("Тренировка сохранена!")