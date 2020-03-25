#! /bin/env python
import subprocess
import sys


def schoeneberge():
    # foo = subprocess.run(["ls", "/bin"], stdout=subprocess.PIPE)
    # print(foo)
    bar = subprocess.run(["nmcli", "connection", "up", "SchoeneBerge"])
    print(bar)


def pequod_mobil_hs():
    bar = subprocess.run(["nmcli", "connection", "up", "pequod_mobil"])
    print(bar)


def connect_vpn():
    foo = subprocess.run(["sudo", "vpnc", "/etc/vpnc/pequod.conf", "--gateway", "dominicb.ddns.net"])
    # foo = subprocess.run(["nmcli", "connection", "up", "'VPN connection 1'", "--ask"])
    print(foo)


def disconnect_vpn():
    foo = subprocess.run(["sudo", "vpnc-disconnect"])
    print(foo)


def pequod_mobil_hs_vpn():
    pequod_mobil_hs()
    connect_vpn()


def funk_aus():
    foo = subprocess.run(["nmcli", "radio", "wifi", "off"])
    print(foo)


def funk_an():
    foo = subprocess.run(["nmcli", "radio", "wifi", "on"])
    print(foo)


def ende():
    sys.exit(0)


def start():
    print()
    print("1. Verbinden mit WLAN SchoeneBerge")
    print("2. Verbinden mit pequod_mobil_hs")
    print()
    print("3. Verbinden mit VPN")
    print("4. Trennen von VPN")
    print("5. Verbinden mit pequod_mobil_hs mit vpn")
    print()
    print("6. Funkverbindung anschalten")
    print("7. Funkverbindung ausschalten")
    print()
    print("99 beendet das Programm")

    user_input = int(input("Bitte waehle eine Zahl: "))

    if user_input == 1:
        schoeneberge()

    elif user_input == 2:
        pequod_mobil_hs()

    elif user_input == 3:
        connect_vpn()

    elif user_input == 4:
        disconnect_vpn()

    elif user_input == 5:
        pequod_mobil_hs_vpn()

    elif user_input == 6:
        funk_an()

    elif user_input == 7:
        funk_aus()

    elif user_input == 99:
        ende()

    else:
        pass


if __name__ == "__main__":
    start()
