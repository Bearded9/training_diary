import json
from datetime import datetime
import os

# функция для проверки ввода
def safe_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка! Введите число.")

# загрузка готовых программ из файла
with open("programs.json", "r", encoding="utf-8") as f:
    programs = json.load(f)

choosing_training_program = int(input("Выберите гоовую программу тренировок или создайте свою(введите '1' для создания своей программы или '2' для выбора готовой) "))

if choosing_training_program == 1:
    list_of_exercises = input("Введите название упражнения или 'нет' для выхода: ")# список упражнений
    with open ("training_log.txt", "a", encoding="utf-8") as file:
        file.write("--- Своя программа! --- \n")
    while list_of_exercises != "нет":
        weight = int(input("Введите рабочий вес: "))  # вес снаряда
        number_of_approaches = int(input("Введите количество подходов: "))  # подходы
        number_of_repetitions = int(input("Введите количество повторений: "))  # повторения

        # запись в файл
        with open("training_log.txt", "a", encoding="utf-8") as file:
            file.write(f"{list_of_exercises} - {weight}кг, {number_of_approaches} на {number_of_repetitions} \n")

        print("Упражение добавлено")
        list_of_exercises = input("Введите название упражнения или 'нет' для выхода: ")

    print("Тренировка сохранена")
if choosing_training_program == 2:
    print("\nДоступные программы тренировок:")
    for key, program in programs.items():
        print(f"{key}. {program['name']} ({', '.join(program['exercises'])})")

    choice = input("Выберите номер программы (или 'нет' для выхода): ")

    if choice == programs:
        print()

    if choice == "нет":
        print("До встречи!")
    elif choice not in programs:
        while choice not in programs:
            print("Неправильный номер программы. Попробуйте еще раз.")
            choice = input("Выберите номер программы (или 'нет' для выхода): ")
    else:
        selected_program = programs[choice]
        print(f"\nВы выбрали программу: {selected_program['name']}")

        with open ("training_log.txt", "a", encoding="utf-8") as file:
            file.write(f"\n--- {selected_program['name']} ---\n")

            for exercise in selected_program['exercises']:
                print(f"\n Упражнение: {exercise}")
                weight = safe_int_input("  Введите рабочий вес (кг): ")
                approaches = safe_int_input("  Введите количество подходов: ")
                repetitions = safe_int_input("  Введите количество повторений: ")

                file.write(f"{exercise} - {weight}кг, {approaches} на {repetitions}\n")
                print(f"{exercise} сохранено!")

        print("Тренировка сохранена в training_log.txt!")

