from pathlib import Path

path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# print(path.iterdir())

for item in path.iterdir():
    print(item)

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# print(path.glob("*.py"))
py_files = [p for p in path.rglob("*.py")]
print("py_files: ", py_files)
