import sys
print(sys.argv)

if len(sys.argv) == 1:
    print("Please enter in this format: python app.py <password>")
else:
    password = sys.argv[1]
    print("password: ", password)
