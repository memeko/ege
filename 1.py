import random
from itertools import product

def generate_task():
    # Буквы вершин графа
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    # Случайное сопоставление букв с цифрами 1-7
    nums = random.sample(range(1, 8), 7)
    letter_to_num = {letter: num for letter, num in zip(letters, nums)}
    num_to_letter = {num: letter for letter, num in letter_to_num.items()}
    
    # Генерация графа с случайными связями и длинами
    graph = {letter: [] for letter in letters}
    road_lengths = {}
    
    for u, v in product(letters, repeat=2):
        if u == v:
            continue
        # 40% вероятность создания дороги
        if random.random() < 0.4:
            length = random.randint(1, 100)
            graph[u].append(v)
            road_lengths[(u, v)] = length
    
    # Создание таблицы
    table = []
    # Шапка таблицы
    header = ['_'] + list(map(str, range(1, 8)))
    table.append(header)
    
    for i in range(1, 8):
        row = [str(i)]
        current_letter = num_to_letter[i]
        for j in range(1, 8):
            if i == j:
                row.append('х')
                continue
            target_letter = num_to_letter[j]
            if (current_letter, target_letter) in road_lengths:
                row.append(str(road_lengths[(current_letter, target_letter)]))
            else:
                row.append(' ')
        table.append(row)
    
    # Генерация случайного вопроса
    pairs = random.sample(list(product(letters, repeat=2)), 2)
    while pairs[0][0] == pairs[0][1] or pairs[1][0] == pairs[1][1]:
        pairs = random.sample(list(product(letters, repeat=2)), 2)
    
    # Форматирование вывода
    task = "На рисунке схема дорог N-ского района изображена в виде графа, в таблице содержатся сведения о протяжённости каждой из этих дорог (в километрах).Таблица протяжённостей:\n"
    for row in table:
        task += " |".join(row) + "\n"
    
    task += "\nГраф (связи вершин):\n"
    for letter in letters:
        connections = graph[letter]
        if connections:
            task += f"{letter} -> {','.join(connections)}\n"
    
    question = (
        f"\nОпределите, какова сумма протяжённостей дорог из пункта {pairs[0][0]} в пункт {pairs[0][1]} "
        f"и из пункта {pairs[1][0]} в пункт {pairs[1][1]}.\n"
        "В ответе запишите целое число."
    )
    
    # Вычисление правильного ответа
    total = 0
    for (start, end) in pairs:
        num_start = letter_to_num[start]
        num_end = letter_to_num[end]
        value = table[num_start][num_end]
        if value.isdigit():
            total += int(value)
    
    return task + question, total

# Пример использования
task, answer = generate_task()
print(task)
print("\nОтвет:", answer)
