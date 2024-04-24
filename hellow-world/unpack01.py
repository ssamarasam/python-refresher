numbers = [1, 2, 3]
print(*numbers)
print(numbers)

values1 = list(range(5))
print("values1: ", values1)

values2 = [*range(5)]
print("values2: ", values2)

values3 = [*range(5), *"Hello"]
print("values3: ", values3)

values4 = [*values3, "a", *values1]
print("values4: ", values4)

first = {"x": 1}
second = {"x": 15, "y": 20}
combined = {**first, **second, "z": 25}
print(combined)
