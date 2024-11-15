import random
import time


array = [random.randint(0, 1000000) for _ in range(100000)]
def insertion_sort(array): #сортировка вставками
    start_time = time.time() # Запоминаем время начала сортировки
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i - 1
        while j >= 0 and array[j] > item_to_insert:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item_to_insert
    end_time = time.time() # Запоминаем время окончания сортировки
    elapsed_time = end_time - start_time # Вычисляем время сортировки
    print(f"Сортировка вставками заняла {elapsed_time:.4f} секунд.") # Выводим время сортировки
    return array


def bubble_sort_ascending(array):
    start_time = time.time()
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Сортировка пузырьком заняла {elapsed_time:.4f} секунд.")
    return array


sorted_array = insertion_sort(array.copy()) # Используем копию массива, чтобы не изменять исходный
sorted_array = bubble_sort_ascending(array.copy())
