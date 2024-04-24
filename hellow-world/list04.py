values1 = []
for x in range(5):
    values1.append(x * 2)
print(values1)

# values2 = [expression for item in items]
values2 = [x * 2 for x in range(5)]
print("values2: ", values2)

# create a set

values3 = {x * 2 for x in range(10)}
print(type(values3), values3)
