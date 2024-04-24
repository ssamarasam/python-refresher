# i = 0
# while i < 10:
#     print(i)
#     i += 1


# number = 100
# while number > 0:
#     print(number)
#     number = number // 2


# command = ""
# while command.lower() != "quit":
#     command = input("enter > ")
#     print("Echo", command)


while True:
    command = input("> ")
    print("ECHO", command)
    if command.lower() == "quit":
        break
