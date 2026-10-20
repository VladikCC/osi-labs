# A4: наибольшее из двух чисел без ветвлений и циклов
a = int(input())
b = int(input())
# False -> индекс 0 (a), True -> индекс 1 (b)
print([a, b][a <= b])
