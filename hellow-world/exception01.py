try:
    with open("app.py") as file:
        print("file opened.")

    age = int(input("enter age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("Enter valid value.")
    # print("error: ", error)
    # print(type(error))
except ZeroDivisionError:
    print("Age cannot be zeror")
else:
    print("no exceptions")
# finally:
#     file.close()
