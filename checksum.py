#! /bin/env python
import subprocess
import sys


def choose_type(type):
    file = input("Enter the Checksum-file-name.")
    foo = subprocess.run([type, "-c", file], stdout=subprocess.PIPE)
    print(foo.stdout.decode("utf-8"))


def end():
    sys.exit(0)


def start():
    print("\n1. Check the input file with md5sum.")
    print("2. Check the input file with sha1sum.")
    print("3. Check the input file with sha224sum.")
    print("4. Check the input file with sha256sum.")
    print("5. Check the input file with sha384sum.")
    print("6. Check the input file with sha512sum.\n")
    print("99 quit this program")

    user_input = int(input("Choose a number: "))

    if user_input == 1:
        choose_type("md5sum")

    elif user_input == 2:
        choose_type("md5sum")

    elif user_input == 3:
        choose_type("sha1sum")

    elif user_input == 4:
        choose_type("sha256sum")

    elif user_input == 5:
        choose_type("sha384sum")

    elif user_input == 6:
        choose_type("sha512sum")

    elif user_input == 99:
        end()

    else:
        pass


if __name__ == "__main__":
    start()
