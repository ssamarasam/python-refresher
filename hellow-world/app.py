import math
""" new code"""
print("hello world")
print("*" * 15)
y = 1


# string
course = " python programming "
print(len(course))
print(course[0])
print(course[0:3])
print(course[:4])
print(course[0:])
print(course[3:])
print(course[:])

# escape sequences
# \"
# \'
# \\
# \n
# \t

# formated strings
first = "Mosh"
last = "Hae"
full = f"{first} {last}"
print("fullname", full)

# string methods
print("-" * 15)
print(course.upper())
print(course.lower())
print(course.strip())
print(course.rstrip())
print(course.lstrip())
print(course.title())
print(course.find("Pro"))
print(course.find("pro"))
print(course.replace("p", "z"))
print("pro" in course)
print("sfift" not in course)

print("*" * 15)
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)

# working with numbers
print(math.ceil(2.1))
print(round(3.4))
print(abs(-3.1))

# type conversion

# x = input("x: ")
# print(type(x))
# print("x: ", x)
# y = int(x) + 1
# print("y: ", y)
# print(f"x: {x}, y: {y}")

# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy values
# ""
# 0
# None - value not available

# operators
print(ord("b"))

temperature = 21
if temperature > 29:
    print("its warm")
elif temperature > 20:
    print("its nice!")
else:
    print("its cold")
print("done")


# ternary operator
age = 12
if age >= 18:
    message = "eligible"
else:
    message = "not eligible"

print("message: ", message)

detail = "confirmed" if age >= 18 else "not confirmed"
print("detail: ", detail)
