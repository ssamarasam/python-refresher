from pathlib import Path


path = Path("ecommerce/__init__.py")
print(path)
print(path.is_file())
print(path.exists())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path01 = path.with_name("file.txt")
print(path01)
print(path01.absolute())
path02 = path.with_suffix(".txt")
print(path02)
print(path02.absolute())
