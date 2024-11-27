import re

def commands(command, array):
    # Проверка команды "Получить элемент по n индексу"
    match_single = re.match(r"Получить элемент по (\d+) индексу", command)
    if match_single:
        index = int(match_single.group(1))
        if 0 <= index < len(array):
            return array[index]
        else:
            return "Индекс вне диапазона массива."

    # Проверка команды "Получить элементы с n по b с шагом v"
    match_range = re.match(r"Получить элементы с (\d+) по (\d+) с шагом (\d+)", command)
    if match_range:
        start = int(match_range.group(1))
        end = int(match_range.group(2))
        step = int(match_range.group(3))
        if 0 <= start < len(array) and 0 <= end < len(array) and step > 0:
            return array[start:end:step]
        else:
            return "Диапазон или шаг вне допустимых значений."

    # Проверка команды "Получить n-ый элемент с конца массива"
    match_negative = re.match(r"Получить (\d+) элемент с конца массива", command)
    if match_negative:
        n = int(match_negative.group(1))
        if 1 <= n <= len(array):
            return array[-n]
        else:
            return "Индекс вне диапазона массива."
    return "Неизвестная команда."


someArray = [10, 20, 30, 40, 50, 60, 70]


# проверки
print(commands("Получить элемент по 2 индексу", someArray))  # 30
print(commands("Получить элементы с 1 по 6 с шагом 2", someArray))  # [20, 40, 60]
print(commands("Получить 2 элемент с конца массива", someArray))  # 60
print(commands("Получить элемент по 9 индексу", someArray)) #Индекс вне диапазона массива.
print(commands("Получить элементы с 1 по 6 с шагом 0", someArray)) #Диапазон или шаг вне допустимых значений.
print(commands("Получить 0 элемент с конца массива", someArray)) #индекс вне диапазона массива.
