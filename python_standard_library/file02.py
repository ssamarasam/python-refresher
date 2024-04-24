from pathlib import Path

source = Path("ecommerce/test.py")
target = Path() / "test1.py"

target.write_text(source.read_text())
