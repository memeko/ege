import random
from math import comb

def digit_to_char(digit):
    """Преобразует цифру в символ (A для 10, B для 11 и т.д.)."""
    if digit < 10:
        return str(digit)
    return chr(ord('A') + digit - 10)

def char_to_digit(char):
    """Преобразует символ в цифру (A -> 10, B -> 11 и т.д.)."""
    if char.isdigit():
        return int(char)
    return ord(char) - ord('A') + 10

def count_valid_numbers(base, length, target_digit, target_count, max_high_digits, high_digit_threshold):
    """Подсчитывает количество чисел, удовлетворяющих условиям задачи."""
    def backtrack(pos, has_zero, count_target, count_high, current_num):
        if pos == length:  # Если число полностью сгенерировано
            return 1 if count_target == target_count and count_high <= max_high_digits else 0
        total = 0
        for d in range(0, base):  # Перебор всех возможных цифр
            if pos == 0 and d == 0:  # Первая цифра не может быть 0
                continue
            new_count_target = count_target + (1 if d == target_digit else 0)
            new_count_high = count_high + (1 if d > high_digit_threshold else 0)
            if new_count_target > target_count or new_count_high > max_high_digits:  # Проверка ограничений
                continue
            total += backtrack(pos + 1, has_zero or (d == 0), new_count_target, new_count_high, current_num * base + d)
        return total
    return backtrack(0, False, 0, 0, 0)

def generate_task_with_answer():
    # Параметры задачи
    base = random.choice([8, 10, 12, 16])  # Основание системы счисления
    length = random.randint(4, 6)  # Длина числа
    target_digit = random.randint(0, base - 1)  # Цифра, которая должна встречаться определённое количество раз
    target_count = random.randint(1, 2)  # Количество целевых цифр
    max_high_digits = random.randint(1, 3)  # Максимальное количество цифр, превышающих определённое значение
    high_digit_threshold = random.randint(base // 2, base - 2)  # Порог для "высоких" цифр

    # Преобразуем цифры в символы, если основание > 10
    target_digit_str = digit_to_char(target_digit)
    high_digit_threshold_str = digit_to_char(high_digit_threshold)

    # Формулировка задачи
    task = (
        f"Определите количество {base}-ричных {length}-значных чисел, в записи которых:\n"
        f"- Ровно {target_count} цифр {target_digit_str};\n"
        f"- Не более {max_high_digits} цифр с числовым значением, превышающим {high_digit_threshold_str};\n"
    )

    # Генерация ответа
    answer = count_valid_numbers(base, length, target_digit, target_count, max_high_digits, high_digit_threshold)
    return task, answer
    
def generate_multiple_tasks_with_answers(num_tasks):
    for i in range(num_tasks):
        print(f"Задание {i + 1}:")
        task, answer = generate_task_with_answer()
        print(task)
        print(f"Ответ: {answer}")
        print()

# Генерация и вывод задания с ответом
tasks = int(input("Введите необходимое количество задач: "))
generate_multiple_tasks_with_answers(tasks)
