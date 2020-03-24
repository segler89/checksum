#! /bin/env python

# Please note: This sript cannot make a individuell save-location for the image, it will always be the folder in which you currently are.
# In the same way this script can only be executed in this folder, where the image is in.

import subprocess
import sys


def save_img_sda():
    subprocess.run(["sudo", "dd", "if=/dev/sda", "|", "gzip", ">", "backup.img.gz"], stdout=subprocess.PIPE)


def write_on_sda():
    subprocess.run(["sudo", "cat", "backup.img.gz", "|", "gunzip", "|", "dd", "of=/dev/sda"], stdout=subprocess.PIPE)


def save_img_sdb():
    subprocess.run(["sudo", "dd", "if=/dev/sdb", "|", "gzip", ">", "backup.img.gz"], stdout=subprocess.PIPE)


def write_on_sdb():
    subprocess.run(["sudo", "cat", "backup.img.gz", "|", "gunzip", "|", "dd", "of=/dev/sdb"], stdout=subprocess.PIPE)


def save_img_sdc():
    subprocess.run(["sudo", "dd", "if=/dev/sdc", "|", "gzip", ">", "backup.img.gz"], stdout=subprocess.PIPE)


def write_on_sdc():
    subprocess.run(["sudo", "cat", "backup.img.gz", "|", "gunzip", "|", "dd", "of=/dev/sdc"], stdout=subprocess.PIPE)


def lsblk():
    print("Take a short look where your sd-card is:")
    print((subprocess.run(["lsblk"], stdout=subprocess.PIPE)).stdout.decode("utf-8"))


def end():
    sys.exit(0)


def start():    
    print("What do you want? Save or write?")
    print("1. Save image")
    print("2. Write image")
    print("99. Quit")
    user_input1 = int(input("Choose a number: "))
    print()

    if user_input1 == 1:
        lsblk()
        print()
        print("Where to save? Prompt: <sdX> Choose a Buchstabe for X, like a.")
        user_input2 = input("a-c, q for quit.")
        print()
        if user_input2 == a:
            save_img_sda()

        elif user_input2 == b:
            save_img_sdb()
        
        elif user_input2 == c:
            save_img_sdc()

        elif user_input2 == q:
            end()
        
        else:
            pass

    elif user_input1 == 2:
        lsblk()
        print()
        print("Where to write? Promt: <sdX> Choose a Buchstabe for X, like a.")
        user_input3 = input("a-c, q for quit.")
        print()
        if user_input3 == a:
            write_on_sda()

        elif user_input3 == b:
            write_on_sdb()
        
        elif user_input3 == c:
            write_on_sdc()
            
        elif user_input2 == q:
            end()
        
        else:
            pass

    elif user_input1 == 99:
        end()

    else:
        pass


if __name__ == "__main__":
    start()
