import os 
from sys import platform
linuxthing = """cd files
echo test > info.txt"""
print(linuxthing)
y = True
def is_windows():
	return platform == "win32"
print("utool-shell setup")
prompt = input("Continue? (y/n) ")
if is_windows():
	if prompt == "y":
		os.system("mkdir files")
		os.system("setup2.bat")
		input("Done!")
	if prompt == "n":
		input("Cancalled... ")
else:
	if prompt == "y":
		os.system("mkdir files")
		os.system(linuxthing)
		input("Done!")
	if prompt == "n":
		input("Cancalled... ")