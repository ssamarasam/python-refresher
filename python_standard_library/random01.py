import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4, 5], k=3))
print(random.choices("abcdefghijklmnopqrstuvwxyz", k=8))
print(''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8)))
print(string.ascii_letters)
print(string.digits)
print(''.join(random.choices(string.ascii_letters + string.digits, k=8)))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print(numbers)
