import random
import string
from subprocess import Popen,PIPE

def password_generator(lenght,spc_chars=False):
    if spc_chars == True:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits
    password = "".join(random.choice(characters) for i in range(lenght))
    return password

def out(password,lenght):
    for i in range(lenght+4):
        print("*", end="")
    print("\n* " + password + " *")
    for i in range(lenght+4):
        print("*", end="")
    print("")

def copy_clipboard(msg):
    with Popen(['xclip','-selection', 'clipboard'], stdin=PIPE) as pipe:
        pipe.communicate(input=msg.encode('utf-8'))

lenght = int(input("Insert password lenght: "))
special_characters = input("Want to add special characters? (Y/n) ")
acepted_affirmative = {"Y","yes","y"}

if special_characters in acepted_affirmative:
    password = password_generator(lenght,True)
else:
    password = password_generator(lenght)

out(password,lenght)

clipboard = input("Add password to clipboard? (Y/n) ")
if clipboard in acepted_affirmative:
    copy_clipboard(password)
    print("Password copied to clipboard")