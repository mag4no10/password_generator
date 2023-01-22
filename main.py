#!/usr/bin/python3

import random
import string
from subprocess import Popen,PIPE

def password_generator(length,spc_chars=False):
    if spc_chars == True:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits
    password = "".join(random.choice(characters) for i in range(length))
    return password

def out(password,length):
    for i in range(length+4):
        print("*", end="")
    print("\n* " + password + " *")
    for i in range(length+4):
        print("*", end="")
    print("")

def copy_clipboard(msg):
    with Popen(['xclip','-selection', 'clipboard'], stdin=PIPE) as pipe:
        pipe.communicate(input=msg.encode('utf-8'))

length = int(input("Insert password length: "))
special_characters = input("Want to add special characters? (Y/n) ")
acepted_affirmative = {"Y","y","Yes","yes"}

if special_characters in acepted_affirmative:
    password = password_generator(length,True)
else:
    password = password_generator(length)

out(password,length)

clipboard = input("Add password to clipboard? (Y/n) ")
if clipboard in acepted_affirmative:
    copy_clipboard(password)
    print("Password copied to clipboard")