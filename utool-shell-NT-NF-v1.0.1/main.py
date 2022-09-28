import os
import random
from os import system
from sys import platform
import time
loggedin = False
loginphase = """accloginp1 = "u32.asave"
accloginp11 = "p32.asave"
accloginp2 = open(accloginp1, "r")
accloginp22 = open(accloginp11, "r")
accloginf1 = accloginp2.read()
accloginf2 = accloginp22.read()"""

consoletag = "utool>"

acclogina = """cd isys
""" + loginphase + """
"""
muau = ""
muap = ""
mawin1 = "@echo off"
mawin2 = "cd isys"
ma32 = "echo " + muau + " > u32.asave"
ma2i32 = "echo " + muap + " > p32.asave"
try:
    imdumb = "qmuau.iasave"
    imdumb2 = open(imdumb, "r")
    imdumb3 = imdumb2.read()
    imvdumb = "qmuap.iasave"
    imvdumb2 = open(imvdumb, "r")
    imvdumb3 = imvdumb2.read()
    imdumb3 = imdumb3.strip()
    imvdumb3 = imvdumb3.strip()
except:
    print("Get a offline account by using makeaccount (ITS FREE)")
at = "@"

som1 = "backslash.txt"
som2 = open(som1, "r")
blackslash = som2.read()
print(blackslash) 
def is_windows():
    return platform == "win32"
def is_mac():
    return platform == "darwin"
def is_linux():
    return platform == "linux"
def is_freebsd():
    return platform == "freebsd7" or "freebsd8" or "freebsdN"
if is_windows():
    import tkinter as tk
    from tkinter import Text
log1 = False
log2 = False
log3 = False
daflinux = """cd files
rm *.*"""
dafwindows = """@echo off
cd files
del *.* /Q"""
def autoc():
    if is_windows():
        os.system("cls")
    else:
        os.system("clear")
def hs():
    time.sleep(0.25)
print("|")
hs()
autoc()
print("/")
hs()
autoc()
print("-")
hs()
autoc()
print("*******")


def valuetextset():
    try:
        valuetexttest = "valuetext.save"
        e = open(valuetexttest, "r")
        vtt = e.read()
    except:
        valuetextsetresult = False
# utool-shell
# at github Tarvey/utool-shell
# Do not copy this and mark it as your own.
randtext1 = random.randrange(1, 3)
if randtext1 == 1:
    randtext = "silverfish"
if randtext1 == 2:
    randtext = "window"
if randtext1 == 3:
    randtext = "laughing"
startdn = random.randrange(1, 223)
startdnc = "% s" % startdn
os.system("echo " + startdnc + " > debug.save")
try:
    addvalue = "value.save"
    f = open(addvalue, "r")
    thevaluetext = f.read()
    value = thevaluetext
except:
    novalue = True
try:
    addname = "name.save"
    q = open(addname, "r")
    thenametext = q.read()
    setaname = thenametext
except:
    noname = True
def clear_screen():
    if is_windows():
        system("cls")
    else:
        system("clear")
def startprint():
    if is_windows():
        print("Welcome to utool-shell")
        print("Type 'help' to see the list of commands")
        print("To see your version type 'version'")
        print("You use Windows, you can use windows-only commands.")
    else:
        print("Welcome to utool-shell")
        print("Type 'help' to see the list of commands")
        print("To see your version type 'version'")
        print("You use something Unix-based, you will not be able to use windows only commands.")
startprint()
while 1:
    inputthing = input(consoletag)
    if inputthing == "help":
        print("exit")
        print("say")
        print("setmyname")
        print("name (USE setmyname BEFORE EXECUTING)")
        print("version")
        print("notepad (windows only)")
        print("cl")
        print("calc (for windows only)")
        print("window")
        print("linux (for windows only, needs wsl installed (any linux wsl client))")
        print("readfile (use raaf to fix)")
        print("deletefile")
        print("makefile")
        print("renamefile (use raaf to fix)")
        print("raaf (use if you get 'File in use' text")
        print("setvalue")
        print("debugmode")
        print("deleteallfiles")
        print("readvalue")
        print("NT-NF 1.0.1")

    if inputthing == "exit":
        if is_windows():
            os.system("del debug.save")
            os.system("cls")
            os.system("del backup-debug.save")
            os.system("cls")
            break
        else:
            try:
                os.system("rm debug.save")
                os.system("clear")
                os.system("rm backup-debug.save")
                os.system("clear")
                break
            except:
                break
    if inputthing == "version":
        print("Canary 1.0.1-1")
    if inputthing == "say":
        saycommand = input("put something here: ")
        print(saycommand)
    if inputthing == "setmyname":
        setaname = input("Type your name here: ")
        print("I will call you " + setaname + " for this session!")
        os.system("echo " + setaname + " > name.save")
    if inputthing == "name":
        try:
            print("Your name is " + setaname)
        except:
            print("Error found, did you use 'setmyname' or if theres a file named name.save?")
    if inputthing == "cl":
        clear_screen()
    if inputthing == "calc":
        os.system("calc")
    if inputthing == "linux":
        if is_windows():
            os.system("wsl")
        else:
            print("You can not use this command")

    if inputthing == "notepad":
        os.system("notepad")
    if inputthing == "window":
        print("to keep using commands, please close the window.")
        window = tk.Tk()
        window.title("Window")
        window.geometry("300x300")
        hello = tk.Label(text="Text")
        hello.pack()
        button = tk.Button(text="Button")
        button.pack()
        
        tk.mainloop() 
    if inputthing == "t1":
        os.system("del som.txt")
    if inputthing == "readfile":
        filename = input("Put the file name\nIf it has a extension please add it too\n")
        os.system("copy files" + blackslash + filename + " " + filename)
        f = open(filename, "r")
        text = f.read()
        print(text)
        os.system("del " + filename)
    if inputthing == "makefile":
        mfcontent = input("""Enter the content:\n""")
        mffilename = input("Input the file name:\n")
        mfend = input("Enter the file extension with the .\n")
        os.system("echo " + mfcontent + " >" + mffilename + mfend)
        os.system("copy " + mffilename + mfend + " files" + blackslash + mffilename + mfend)
        os.system("del " + mffilename + mfend)
    if inputthing == "deletefile":
        if is_windows():
            errnum = random.randrange(1, 993574)
            errnumcon = "% s" % errnum
            debugfailure = startdnc
            print("This feature is not supported in windows yet.")
            print("Error found. Here is your error number:")
            errnumfi = "1rr0-" + errnumcon
            print(errnumfi)
            os.system("echo Error found at debug-" + "% s" % debugfailure + " (nl)Cache is being saved, for more info, heres your error number: " + errnumfi + " > error.utool-error")

        else:
            dffilename = input("Input the file with the extension:\n")
            os.system("rm " + dffilename)
    if inputthing == "renamefile":
        if is_windows:
            rncurrentname = input("Type the current name and the extension\n")
            rnnewname = input("Type the new name and the extension\n")
            os.system("ren " + rncurrentname + " " + rnnewname)
        else:
            rncurrentname = input("Type the current name and the extension\n")
            rnnewname = input("Type the new name and the extension\n")
            os.system("mv " + rncurrentname + " " + rnnewname)
    if inputthing == "raaf":
        os.system("runasadminfix.bat")
        os.system("exit")
        break
    if inputthing == "setvalue":
        setvalue = input("Set the value: ")
        value = setvalue
        print("Value set: " + value)
        try:
            os.system("echo " + value + " > value.save")
        except:
            errnum = random.randrange(1, 888364)
            errnumcon = "% s" % errnum
            debugfailure = random.randrange(1, 223)
            print("Error found. Here is your error number:")
            errnumfi = "155-" + errnumcon
            print(errnumfi)
            os.system("echo Error found at debug-" + "% s" % debugfailure + " (nl)Cache is being saved, for more info, heres your error number: " + errnumfi + " > error.utool-error")
    if inputthing == "readvalue":
        try:
            print(value)
        except:
            print("No value found")
    if inputthing == "debugmode":
        option1 = input("WINDOWS ONLY:Do you want to enter debugmode (y/n): ")
        if option1 == "y":
            print("Entering debugmode...")
            os.system("debugadmin.bat")
        if option1 == "n":
            print("Waiting for debug-" + startdnc)
    if inputthing == "deleteallfiles":
        really1 = input("DO YOU WANT TO DELETE ALL FILES? (y/n) ")
        if really1 == "y":
            really2 = input("ARE YOU SURE? type " + randtext + " ")
            if really2 == randtext:
                os.system("daf.bat")
            else:
                print("failed")
        else:
            print("failed")
    if inputthing == "makeaccount":
        muau = input("Type your username here: ")
        muap = input("Type your password here: ")
        os.system("echo " + muau + " > qmuau.iasave")
        os.system("echo " + muap + " > qmuap.iasave")
        print("Restart your client to login.")
    if inputthing == "login":
        loginpr1 = input("Input your username: ")
        if loginpr1 == imdumb3:
            usernametrue = True
            loginpr2 = input("Input your password: ")
        else:
            print("Wrong username")
            usernametrue = False
        if usernametrue == True:
            if loginpr2 == imvdumb3:
                print("Logged in as " + imdumb3)
                loggedin = True
                consoletag = imdumb3 + ":utool>"
            else:
                print("Wrong password")
    if inputthing == "whoami":
        print("\\>" + imdumb3)