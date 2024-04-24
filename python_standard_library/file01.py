from pathlib import Path
from time import ctime

path = Path("ecommerce/test.py")
print(path.stat())
print(ctime(path.stat().st_ctime))
print(ctime(path.stat().st_birthtime))
# path.read_bytes()
print(path.read_text())
# with open("ecommerce/test.py", "r") as file:
#     print(file.readline())

path.write_text("#new text from path.write method")
