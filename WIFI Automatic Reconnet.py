# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 2/27/2025 - 4:43AM
# Script Purpose : WiFi Auto Reconnect
# Description    : This script monitors your WiFi connection and automatically reconnects
#                  to a specified SSID if the connection drops. It ensures a stable
#                  and continuous connection to the desired WiFi network.
# Features       : - Monitor WiFi connection status
#                  - Automatically reconnect to specified SSID
#                  - Run in the background and check connection every 5 seconds
# Requirements   : - Python 3.x
#                  - Windows OS
#                  - netsh command line utility
#                  - Replace the SSID and PASSWORD fields with your WiFi network details
# ===================================================================================
import subprocess
import time

SSID = "Your_SSID" 
PASSWORD = "Your_Password"

def connect_wifi(ssid, password):
    result = subprocess.run(["netsh", "wlan", "connect", f"ssid={ssid}", f"name={ssid}"], capture_output=True, text=True)
    if "Successfully" in result.stdout:
        print(f"Connected To {ssid}")
    else:
        print(f"Failed To Connect To {ssid}")

def check_connection(ssid):
    result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
    connected = False
    for line in result.stdout.splitlines():
        if f"SSID                   : {ssid}" in line:
            connected = True
            break
    return connected

def monitor_connection():
    while True:
        if not check_connection(SSID):
            print("Disconnected! Attempting To Reconnect...")
            connect_wifi(SSID, PASSWORD)
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    connect_wifi(SSID, PASSWORD)
    monitor_connection()
