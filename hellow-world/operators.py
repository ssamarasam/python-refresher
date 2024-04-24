# age = 22
# if age >= 18 and age < 65:
#     print("Eligible")

# if 18 >= age < 65:
#     print("eligible")
# for num in range(start, end - 1, incrementor)
for num in range(10):
    print(num)

print("*" * 20)
for num in range(5, 10):
    print(num)

print("*" * 20)
for num in range(0, 10, 2):
    print(num)

print("---" * 15)

successfull = False
for num in range(10):
    print("Attempt")
    if successfull:
        print("Successfull")
        break
else:
    print("Attempted 10 times and failed")
