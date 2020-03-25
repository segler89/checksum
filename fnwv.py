#! /bin/env python
import subprocess
import sys

PEQUOD_SSID = "pequod_mobil"
SCHOENEBERGE_SSID = "SchoeneBerge"


# def schoeneberge():
#     bar = subprocess.run(["nmcli", "connection", "up", "SchoeneBerge"])
#     print(bar)


def connect_wlan(ssid):
    bar = subprocess.run(["nmcli", "connection", "up", ssid])
    print(bar)


# def pequod_mobil_hs():
#     bar = subprocess.run(["nmcli", "connection", "up", "pequod_mobil"])
#     print(bar)


def connect_vpn():
    foo = subprocess.run(["sudo", "vpnc", "/etc/vpnc/pequod.conf", "--gateway", "dominicb.ddns.net"])
#   foo = subprocess.run(["nmcli", "connection", "up", "'VPN connection 1'", "--ask"])
    print(foo)


def disconnect_vpn():
    foo = subprocess.run(["sudo", "vpnc-disconnect"])
    print(foo)


def pequod_mobil_hs_vpn():
    connect_wlan(PEQUOD_SSID)
    connect_vpn()


def toggle_funk(enabled):
    foo = subprocess.run(["nmcli", "radio", "wifi", "on" if enabled else "off"])
    print(foo)


# def funk_aus():
#   foo = subprocess.run(["nmcli", "radio", "wifi", "off"])
#   print(foo)


# def funk_an():
#    foo = subprocess.run(["nmcli", "radio", "wifi", "on"])
#    print(foo)


def ende():
    sys.exit(0)


def start():
    print("\n1. Verbinden mit WLAN SchoeneBerge")
    print("2. Verbinden mit pequod_mobil_hs\n")
    print("3. Verbinden mit VPN")
    print("4. Trennen von VPN")
    print("5. Verbinden mit pequod_mobil_hs mit vpn\n")
    print("6. Funkverbindung anschalten")
    print("7. Funkverbindung ausschalten\n")
    print("99 beendet das Programm")

    user_input = int(input("Bitte waehle eine Zahl: "))

    if user_input == 1:
        connect_wlan(SCHOENEBERGE_SSID)

    elif user_input == 2:
        connect_wlan(PEQUOD_SSID)

    elif user_input == 3:
        connect_vpn()

    elif user_input == 4:
        disconnect_vpn()

    elif user_input == 5:
        pequod_mobil_hs_vpn()

    elif user_input == 6:
        toggle_funk(True)

    elif user_input == 7:
        toggle_funk(False)

    elif user_input == 99:
        ende()

    else:
        pass


if __name__ == "__main__":
    start()
