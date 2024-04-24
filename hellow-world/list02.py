numbers = list(range(21))
print(numbers)
print(numbers[::2])
print(numbers[::-2])
chars = ['a', 'b', 'c']
first, second, third = chars
print(second)
one, two, *others, last = numbers
print(two)
print(others)
print(last)
print(enumerate(numbers))
for char in enumerate(chars):
    print(char)

for char in enumerate(chars):
    print(char[0], char[1])

for index, char in enumerate(chars):
    print(index, char)
