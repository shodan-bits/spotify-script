import time
import os
import psutil
import pygetwindow as gw
import subprocess
from win10toast import ToastNotifier

toaster = ToastNotifier()

def is_spotify_running():
    return any("Spotify.exe" in p.name() for p in psutil.process_iter())

def close_spotify():
    for p in psutil.process_iter():
        if "Spotify.exe" in p.name():
            p.kill()

def relaunch_spotify():
    spotify_path = r"C:\Users\YOUR_USERNAME\AppData\Roaming\Spotify\Spotify.exe"
    subprocess.Popen(spotify_path)

def is_ad_playing():
    try:
        win = gw.getWindowsWithTitle("Spotify")[0]
        title = win.title.lower()
        if "spotify" == title.strip():  
            return True
        return False
    except IndexError:
        return False

toaster.show_toast("Script Spotify lancé",
                   "Le script tourne en arrière-plan et surveille les pubs.",
                   threaded=True,
                   duration=5)

while True:
    if is_spotify_running() and is_ad_playing():
        toaster.show_toast("Pub détectée",
                           "Redémarrage de Spotify...",
                           threaded=True,
                           duration=5)
        close_spotify()
        time.sleep(3)
        relaunch_spotify()
        time.sleep(10)
    time.sleep(5)
