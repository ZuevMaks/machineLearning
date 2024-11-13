def maximum(b, c):
    a = int(input("Введите число a: "))
    if a > 0:
        return max(a, b, c)
    else:
        return -1


result = maximum(7, 14)
print(result)
