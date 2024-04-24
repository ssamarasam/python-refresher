def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return age / 10


try:
    calculate_xfactor(10)
except ValueError as error:
    print(error)
