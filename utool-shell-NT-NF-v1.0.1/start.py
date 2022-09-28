import os
from sys import platform
def winq():
	return platform == "win32"
if winq():
	os.system("python loginphase.py")
	os.system("python main.py")
else:
	os.system("python3 loginphase.py")
	os.system("python3 loginphase.py")