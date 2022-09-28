# DEBUG MODE, DO NOT EDIT
import random
import os
import sys
def is_windows():
	return platform == "win32"
randb = False
notconv = random.randrange(1, 223)
conv = "% s" % notconv
startnum = "debug.save"
e = open(startnum, "r")
num = e.read()
numconv = "% s" % num + ">"
while 1:
	inputthingdm = input("debug>")
	if inputthingdm == "crashdump":
		errnum = random.randrange(1, 993574)
		errnumcon = "% s" % errnum
		print("utool - crashdump")
		print("Error found. Here is your error number:")
		errnumfi = "?-" + errnumcon
		print(errnumfi)
		os.system("echo Error found at debug-" + "% s" % notconv + " (nl)Cache is being saved, for more info, heres your error number: " + errnumfi + " > error.utool-error")
	if inputthingdm == "debugnum":
		target = "debug.save"
		f = open(target, "r")
		text = f.read()
		textconv = "% s" % text
		print(textconv)
	if inputthingdm == "deletesettings":
		try:
			if is_windows():
				os.system("del name.save")
				os.system("del value.save")
			else:
				os.system("rm name.save")
				os.system("rm value.save")
		except:
			print("c-rr")
	if inputthingdm == "debug.change":
		if randb == True:
			dc = input("Type the str/int to change debug.save:\n")
			os.system("echo " + dc + " > debug.save")
		if randb == False:
			print("Run debug.backup before running!")
	if inputthingdm == "debug.backup":
		randb = True
		os.system("copy debug.save backup-debug.save")
		print("Done!")