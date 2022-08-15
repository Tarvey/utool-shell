import os
from os import system
import tkinter as tk
from tkinter import Text
from sys import platform

# utool-shell BASE
# at github Tarvey/utool-shell
# You can use this, but type at the end of your README.md file:
# Copied from utool-shell BASE, Tarvey/utool-shell
def is_windows():
    return platform == "win32"


def clear_screen():
    if is_windows():
        system("cls")
    else:
        system("clear")
def startprint():
    if is_windows():
        print("Welcome to utool-shell BASE")
        print("Type 'help' to see the list of commands")
        print("To see your version type 'version'")
        print("You use Windows, you can use windows-only commands.")
    else:
        print("Welcome to utool-shell BASE")
        print("Type 'help' to see the list of commands")
        print("To see your version type 'version'")
        print("You use something Unix-based, you will not be able to use windows only commands.")
startprint()
while 1:
    inputthing = input("utoolBASE> ")
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
        print("readfile")
        print("deletefile")
        print("makefile")
        print("renamefile")
        print("BASE Version")
    if inputthing == "exit":
        break
    if inputthing == "version":
        print("Release 1.0.0")
    if inputthing == "say":
        saycommand = input("put something here: ")
        print(saycommand)
    if inputthing == "setmyname":
        setaname = input("Type your name here: ")
        print("I will call you " + setaname + " for this session!")
    if inputthing == "name":
        print("Your name is " + setaname)
    if inputthing == "cl":
        clear_screen()
    if inputthing == "calc":
        os.system("calc")

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

    if inputthing == "readfile":
        filename = input("Put the file name\nIf it has a extension please add it too\n")
        f = open(filename, "r")
        text = f.read()
        print(text)
    if inputthing == "makefile":
        mfcontent = input("""Enter the content:\n""")
        mffilename = input("Input the file name:\n")
        mfend = input("Enter the file extension with the .\n")
        os.system("echo " + mfcontent + " >" + mffilename + mfend)
    if inputthing == "deletefile":
        if is_windows:
            dffilename = input("Input the file with the extension:\n")
            os.system("del " + dffilename)
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
    if inputthing == "relaunch":
        break
        os.system("python main.py")
