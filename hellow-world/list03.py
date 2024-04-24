letters = ['a', 'b', 'c']

# add
letters.append("d")
print(letters)
letters.insert(1, '+')
print(letters)

# remove at end
letters.pop()
print(letters)

# remove en element of first occurance
letters.remove("a")
print(letters)

# remove at position
letters.pop(0)
print(letters)

numbers = list(range(15))
print(numbers)
del numbers[0]
print(numbers)
del numbers[0:3]
print(numbers)
numbers.clear()
print(numbers)


print(letters)
if "b" in letters:
    print(letters.index("b"))
    print(letters.count("b"))

counts = [51, 6, 17, 13, 1, 2, 4, 3]
# counts.sort()
print(counts)
# counts.sort(reverse=True)
print(sorted(counts))
print(sorted(counts, reverse=True))
# print(counts)


items = [
    ("product1", 9),
    ("product2", 3),
    ("product3", 4)
]


# def sort_item(item):
#     return item[1]


items.sort(key=lambda item: item[1])
print(items)

prices = []

for item in items:
    prices.append(item[1])

print("prices: ", prices)

# returns iterable object
x = map(lambda item: item[1], items)
print("x: ", x)
x1 = [item[1] for item in items]
print("x1: ", x1)

y = list(x)
print("y: ", y)

z = filter(lambda item: item[1] < 8, items)
zlist = list(z)
print("zlist: ", zlist)

# list comprehension [expression for item in items]
z1 = [item for item in items if item[1] < 8]
print("z1: ", z1)

list1 = [1, 2, 3]
list2 = [10, 20, 30]
list3 = list(zip(list1, list2))
print("list 3: ", list3)
list4 = list(zip("abc", list1, list2))
print("list4: ", list4)
