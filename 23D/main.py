import sys
from time import sleep
from colorama import Fore
import os
import random

# Functions and Variables
default = Fore.WHITE
minimap = """
000010000
000010000
000010000
"""
objects = [
    "#########",
    "#########",
    "#########",
    "#########"
]
minLimit = 1
maxLimit = 9
sight = 5
pos = 2
camera = f"{sight}{objects[pos]}~"

def clear():
    os.system("clear")

def scrollTxt(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.03)

def err():
    scrollTxt(Fore.RED + "Not a valid option. Exiting...")
    sleep(1)
    sys.exit()

def help():
    clear()
    scrollTxt("""Add Object - Adds a random 3D object to the scene\n
0 - SPHERE\n1 - CUBE\n2 - PYRAMID\n3 - PRISM\nTurn L/R - turns your 2D plane of sight L/R\n
This action is shown by the Minimap\nMove F/B - Moves your plane of sight F/B to see multiple objects.""")
    sleep(2.5)
    while(True):
        game()

def game():
    # In need of serious optimisations. If you have any ideas
    # please comment on the error listed or commit on new branch
    # thx :)
    global pos
    global camera
    global sight
    global minimap
    clear()
    print(default + minimap)
    print(default + f"{objects[0]}\n{objects[1]}\n{objects[2]}\n{objects[3]}\n")
    print(default + camera)
    scrollTxt("Type \":h\" for help and \":q\" to quit.\n")
    action = input("[1] Left\n[2] Right\n[3] Add Object\n[4] Move Forward\n[5] Move Backward\n")
    if action == "1":
        if sight != minLimit:
            sight -= 1
        else:
            scrollTxt(Fore.RED + "Min limit reached." + default)
        if sight == 5:
            minimap = """
000010000
000010000
000010000
            """
        elif sight == 4:
            minimap = """
000100000
000010000
000001000
            """
        elif sight == 3:
            minimap = """
001000000
000010000
000000100
            """
        elif sight == 2:
            minimap = """
010000000
000010000
000000010
            """
        elif sight == 1:
            sight = minLimit
            minimap = """
100000000
000010000
000000001
            """

        if sight == 6:
            minimap = """
000001000
000010000
000100000
            """
        elif sight == 7:
            minimap = """
000000100
000010000
001000000
            """
        elif sight == 8:
            minimap = """
000000010
000010000
010000000
            """
        elif sight == 9:
            sight = maxLimit
            minimap = """
000000001
000010000
100000000
            """

        clear()
        print(default + minimap)
        camera = f"{sight}{objects[pos]}~"
    elif action == "2":
        if sight != maxLimit:
            sight += 1
        else:
            scrollTxt(Fore.RED + "Max limit reached." + default)
        if sight == 6:
            minimap = """
000001000
000010000
000100000
            """
        elif sight == 7:
            minimap = """
000000100
000010000
001000000
            """
        elif sight == 8:
            minimap = """
000000010
000010000
010000000
            """
        elif sight == 9:
            sight = maxLimit
            minimap = """
000000001
000010000
100000000
            """

        if sight == 5:
            minimap = """
000010000
000010000
000010000
            """
        elif sight == 4:
            minimap = """
000100000
000010000
000001000
            """
        elif sight == 3:
            minimap = """
001000000
000010000
000000100
            """
        elif sight == 2:
            minimap = """
010000000
000010000
000000010
            """
        elif sight == 1:
            sight = minLimit
            minimap = """
100000000
000010000
000000001
            """
        clear()
        print(default + minimap)
        camera = f"{sight}{objects[pos]}~"
    elif action == "3":
        foo = random.randint(0, 3)
        bar = f"####{foo}####"
        objects[foo] = bar
        camera = objects[pos]
    elif action == "4":
        if pos != 0:
            pos -= 1
            camera = f"{sight}{objects[pos]}~"
        else:
            scrollTxt(Fore.RED + "Max limit reached" + default)
    elif action == "5":
        if pos != 3:
            pos += 1
            camera = f"{sight}{objects[pos]}~"
        else:
            scrollTxt(Fore.RED + "Min limit reached" + default)
    elif action == ":h":
        help()
    elif action == ":q":
        sys.exit()
    else:
        err()

def credits():
    clear()
    scrollTxt("Created by Shaunak Ghosh.\n")
    scrollTxt("@horsesnacks\n")
    scrollTxt("shaunakg2011@gmail.com\n")
    scrollTxt("Thanks to Flatland by Edwin Abbott for the idea\n")
    scrollTxt(":)\n")
    sleep(2.5)
    while(True):
        game()

clear()
colour = input("Appearance of desktop\n[1] Light\n[2] Dark\n")
if (colour == "1"):
    default = Fore.BLACK
    clear()
elif (colour == "2"):
    default = Fore.WHITE
    clear()
else:
    err()

# Main Menu
def main():
    scrollTxt(default + "Imagine a life where you are a small 2D Object in a 3D World...")
    sleep(2.5)
    clear()
    print("\n"
        "██████  ██████  ██████  \n"
        "     ██      ██ ██   ██ \n"
        " █████   █████  ██   ██ \n"
        "██           ██ ██   ██ \n"
        "███████ ██████  ██████  \n")
    scrollTxt(default + "(Twenty-Three Dimensions)\n")
    scrollTxt("A simple test about flat things in not flat things.\n")
    opt = input("[1] Start\n[2] Credits\n")
    if opt == "1":
        while(True):
            game()
    elif opt == "2":
       credits()
    else:
        err()

main()
