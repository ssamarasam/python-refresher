from timeit import timeit
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return age / 10


try:
    calculate_xfactor(0)
except ValueError as error:
    pass

"""
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return age / 10



xfactor =  calculate_xfactor(0)
if xfactor == None:
    pass

"""

print("first: ", timeit(code1, number=10000))
print("second: ", timeit(code2, number=10000))
