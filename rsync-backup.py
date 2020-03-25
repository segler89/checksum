#! /bin/env python
import subprocess


def save_to_pi():
    subprocess.run(["rsync", "-a", "--delete", "--quiet", "-e", "ssh", "/home/ahab/", "pi@192.168.178.28:/home/pi/backup"])


def start():
    save_to_pi()


if __name__ == "__main__":
    start()
