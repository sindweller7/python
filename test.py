import subprocess

completed = subprocess.run(['ls', '-al'])
print('returncode: ', completed.returncode)