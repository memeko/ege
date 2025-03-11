import random

def generate_expression(depth=0):
    # Базовые переменные
    variables = ['w', 'x', 'y', 'z']
    
    # Если достигнута максимальная глубина, возвращаем переменную или её отрицание
    if depth > 2:
        return random.choice([random.choice(variables), f"¬{random.choice(variables)}"])
    
    # Случайно выбираем операцию
    operations = ['∧', '∨', '→', '↔']
    operation = random.choice(operations)
    
    # Рекурсивно генерируем левую и правую части выражения
    left = generate_expression(depth + 1)
    right = generate_expression(depth + 1)
    
    # Возвращаем выражение в скобках
    return f"({left} {operation} {right})"

def evaluate_expression(F, values):
    """Вычисляет значение логического выражения F для заданных значений переменных."""
    # Заменяем переменные в выражении на их значения
    expr = F
    for var, val in values.items():
        expr = expr.replace(var, str(val))
    # Заменяем отрицания
    expr = expr.replace("¬0", "1").replace("¬1", "0")
    # Вычисляем выражение
    return eval(expr.replace("∧", " and ").replace("∨", " or ").replace("→", " <= ").replace("↔", " == "))

def generate_task():
    # Список российских имён
    names = ["Саша", "Петя", "Ваня", "Коля", "Сергей", "Дима", "Андрей", "Игорь", "Миша", "Алексей"]
    name = random.choice(names)
    
    # Переменные и их случайное распределение по столбцам
    variables = ['w', 'x', 'y', 'z']
    random.shuffle(variables)
    cols = {var: i for i, var in enumerate(variables)}
    
    # Генерация случайной функции F
    F = generate_expression()
    
    # Генерация трёх уникальных строк таблицы
    rows = []
    for _ in range(3):
        values = {var: random.randint(0, 1) for var in variables}
        while any(row == values for row in rows):
            values = {var: random.randint(0, 1) for var in variables}
        rows.append(values)
    
    # Формирование таблицы с пропущенными значениями
    table = []
    for row in rows:
        table_row = [' '] * 4
        known_cols = random.sample(range(4), 3)  # Случайно выбираем 3 столбца для заполнения
        for col in known_cols:
            var = variables[col]
            table_row[col] = str(row[var])
        # Вычисляем значение F для данной строки
        F_value = evaluate_expression(F, row)
        table.append(table_row + [str(int(F_value))])  # Добавляем значение F
    
    # Перемешиваем строки таблицы для усложнения задачи
    random.shuffle(table)
    
    # Формируем текст задачи
    task = f"""

{name} заполнял таблицу истинности логической функции F = {F}, но успел заполнить лишь фрагмент из трёх различных её строк, даже не указав, какому столбцу таблицы соответствует каждая из переменных w, x, y, z.

Таблица:
_|_|_|_|F
"""
    for row in table:
        task += "|".join(row[:-1]) + "|" + row[-1] + "\n"
    
    task += """
Определите, какому столбцу таблицы соответствует каждая из переменных w, x, y, z.

В ответе напишите буквы w, x, y, z в том порядке, в котором идут соответствующие им столбцы (сначала буква, соответствующая первому столбцу; затем буква, соответствующая второму столбцу, и т.д.). Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.
"""
    
    # Ответ — порядок переменных и заполненная таблица истинности
    answer = f"Порядок переменных: {''.join(variables)}\n\n"
    answer += "Заполненная таблица истинности:\n"
    answer += "w|x|y|z|F\n"
    for row in rows:
        answer += "|".join(str(row[var]) for var in variables) + f"|{evaluate_expression(F, row)}\n"
    
    return task, answer

# Пример использования
task, answer = generate_task()
print(task)
print("Ответ:\n", answer)
