from pathlib import Path
import shutil

source = Path("ecommerce/test.py")
target = Path() / "test20.py"

shutil.copy(source, target)
