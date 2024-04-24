from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip", "r") as zip:
    print(zip.namelist())
    print(zip.getinfo("ecommerce/test.py"))
    zip.extractall("extract")
