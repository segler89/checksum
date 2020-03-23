#! /bin/env python
import subprocess
import sys


def md5sum():
    file = input("Enter the Checksum-file-name.")
    foo = subprocess.run(["md5sum", "-c", file], stdout=subprocess.PIPE)
    print(foo.stdout.decode("utf-8"))


def sha1sum():
    file = input("Enter the Checksum-file-name.")
    foo = subprocess.run(["sha1sum", "-c", file], stdout=subprocess.PIPE)
    print(foo.stdout.decode("utf-8"))


def sha224sum():
    file = input("Enter the Checksum-file-name.")
    foo = subprocess.run(["sha224sum", "-c", file], stdout=subprocess.PIPE)
    print(foo.stdout.decode("utf-8"))


def sha256sum():
    file = input("Enter the Checksum-file-name: ")
    foo = subprocess.run(["sha256sum", "-c", file], stdout=subprocess.PIPE)
    print(foo.stdout.decode("utf-8"))


def sha384sum():
    file = input("Enter the Checksum-file-name.")
    foo = subprocess.run(["sha384sum", "-c", file], stdout=subprocess.PIPE)
    print(foo.stdout.decode("utf-8"))


def sha512sum():
    file = input("Enter the Checksum-file-name.")
    foo = subprocess.run(["sha512sum", "-c", file], stdout=subprocess.PIPE)
    print(foo.stdout.decode("utf-8"))


def end():
    sys.exit(0)


def start():
    print()
    print("1. Check the input file with md5sum.")
    print("2. Check the input file with sha1sum.")
    print("3. Check the input file with sha224sum.")
    print("4. Check the input file with sha256sum.")
    print("5. Check the input file with sha384sum.")
    print("6. Check the input file with sha512sum.")

    print()
    print("99 quit this programm")

    user_input = int(input("Choose a number: "))

    if user_input == 1:
        md5sum()

    elif user_input == 2:
        sha1sum()

    elif user_input == 3:
        sha224sum()

    elif user_input == 4:
        sha256sum()

    elif user_input == 5:
        sha384sum()

    elif user_input == 6:
        sha512sum()

    elif user_input == 99:
        end()

    else:
        pass


if __name__ == "__main__":
    start()
