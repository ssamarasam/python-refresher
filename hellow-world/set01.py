numbers = [1, 2, 3, 4, 5, 1]
first = set(numbers)
print("first: ", first)
second = {1, 6}
print("second: ", second)
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

# sets does not support indexing

if 1 in first:
    print("yes")
