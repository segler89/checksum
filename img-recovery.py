#! /bin/env python

"""After the ./ you have to type in the save/write path. For example /home/USER/FOLDER/NAME.img.gz"""

import subprocess
import sys


def save_img_sdX(literal, image_path):
    subprocess.run(["sudo", "dd", f"if=/dev/sd{literal}", "|", "gzip", ">", image_path], stdout=subprocess.PIPE)


def write_on_sdX(literal, image_path):
    subprocess.run(["sudo", "cat", image_path, "|", "gunzip", "|", "dd", f"of=/dev/sd{literal}"])


def lsblk():
    print("Take a short look where your sd-card is:")
    print((subprocess.run(["lsblk"], stdout=subprocess.PIPE)).stdout.decode("utf-8"))


def end():
    sys.exit(0)


def start():
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        print("No image-path given, program will end.\n", __doc__)
        end()
        return

    print("What do you want? Save or write?\n")
    print("1. Save image")
    print("2. Write image\n")
    print("99. Quit")
    user_input1 = int(input("Choose a number: "))

    if user_input1 == 1:
        lsblk()
        print("\nWhere to save? Prompt: <sdX> Choose a literal for X, like a.")
        user_input2 = input("a-z, q for quit.")
        print()
        if user_input2 == 'q':
            end()

        else:
            save_img_sdX(user_input2, image_path)

    elif user_input1 == 2:
        lsblk()
        print()
        print("Where to write? Prompt: <sdX> Choose a literal for X, like a.")
        user_input3 = input("a-z, q for quit.")
        print()
        if user_input3 == 'q':
            end()

        else:
            write_on_sdX(user_input3, image_path)

    elif user_input1 == 99:
        end()


if __name__ == "__main__":
    start()
