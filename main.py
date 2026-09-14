import json
import sys
from datetime import datetime
import messages
import os

def safe_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка! Введите число.")

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

file_name_training_program = f"saved_training_programs/training_{timestamp}.txt"

with open("programs.json", "r", encoding="utf-8") as f:
    programs = json.load(f)

choosing_training_program = safe_int_input(messages.text_ready_training_program())

while choosing_training_program != 1 and choosing_training_program != 2:
    print("Введите '1' или '2'")
    choosing_training_program = safe_int_input(messages.text_ready_training_program())

if choosing_training_program == 1:
    list_of_exercises = input(messages.text_name_exercise())

    exercises_list = []

    with open(file_name_training_program, "a", encoding="utf-8") as file:
        file.write("--- Своя программа! --- \n")

    while list_of_exercises != "нет":
        exercises_list.append(list_of_exercises)

        weight = safe_int_input("Введите рабочий вес: ")
        number_of_approaches = safe_int_input("Введите количество подходов: ")
        number_of_repetitions = safe_int_input("Введите количество повторений: ")

        with open(file_name_training_program, "a", encoding="utf-8") as file:
            file.write(f"{list_of_exercises} - {weight}кг, {number_of_approaches} на {number_of_repetitions} \n")

        print("Упражнение добавлено")
        list_of_exercises = input(messages.text_name_exercise())

    save_my_program = input("Хотите сохранить свою программу тренировок в готовые? да/нет ")
    if save_my_program.lower() == "да":
        program_name = input("Введите название программы: ")

        new_program = {
            "name": program_name,
            "exercises": exercises_list
        }

        with open("programs.json", "r", encoding="utf-8") as file:
            all_programs = json.load(file)

        existing_keys = list(all_programs.keys())
        if existing_keys:
            new_key = str(max(map(int, existing_keys)) + 1)
        else:
            new_key = "1"

        all_programs[new_key] = new_program

        with open("programs.json", "w", encoding="utf-8") as file:
            json.dump(all_programs, file, indent=4, ensure_ascii=False)

        print(f"Программа '{program_name}' добавлена в список готовых!")
    else:
        print("Тренировка не сохранена")

    print("Тренировка сохранена")

if choosing_training_program == 2:
    print("\nДоступные программы тренировок:")
    for key, program in programs.items():
        print(f"{key}. {program['name']} ({', '.join(program['exercises'])})")

    choice = input(messages.text_number_program())

    while choice not in programs:
        if choice == "нет":
            print("До встречи!")
            sys.exit(0)
        print("Неправильный номер программы. Попробуйте еще раз.")
        choice = input(messages.text_number_program())

    selected_program = programs[choice]
    print(f"\nВы выбрали программу: {selected_program['name']}")

    with open(file_name_training_program, "a", encoding="utf-8") as file:
        file.write(f"--- {selected_program['name']} ---\n")
        for exercise in selected_program['exercises']:
            print(f"\n Упражнение: {exercise}")
            weight = safe_int_input("  Введите рабочий вес (кг): ")
            approaches = safe_int_input("  Введите количество подходов: ")
            repetitions = safe_int_input("  Введите количество повторений: ")
            file.write(f"{exercise} - {weight}кг, {approaches} на {repetitions}\n")
            print(f"{exercise} сохранено!")
    print("Тренировка сохранена!")
