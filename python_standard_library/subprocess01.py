import subprocess
import os

completed = subprocess.run(['dir'], shell=True,
                           capture_output=True,
                           text=True)
print(completed.args)
print(completed.returncode)
print(completed.stderr)
# print(completed.stdout)

try:

    another_process = subprocess.run(
        ['python', 'other.py'], capture_output=True, text=True, check=True)
    print(another_process.stdout)
    print(another_process.args)
    print(another_process.returncode)
    print(another_process.stderr)
    print(os.getcwd())
except subprocess.CalledProcessError as exception:
    print(exception)
