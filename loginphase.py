import os
test1 = """cd ..
python main.py"""
accloginp1 = "u32.asave"
accloginp11 = "p32.asave"
accloginp2 = open(accloginp1, "r")
accloginp22 = open(accloginp11, "r")
accloginf1 = accloginp2.read()
accloginf2 = accloginp22.read()
os.system("echo " + accloginf1 + " > uslol.temp")
os.system("echo " + accloginf2 + " > pslol.temp")
os.system(test1)