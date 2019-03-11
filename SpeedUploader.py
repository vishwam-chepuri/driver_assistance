import httplib2, urllib.parse import KeyListener
key = 'RW65GNES6TPWVO13'


def uploader(): while True:
params = urllib.parse.urlencode({'field2': KeyListener.Speed, 'key':key }) headers = {"Content-typZZe": "application/x-www-form-urlencoded", "Accept":
"text/plain"}
conn = httplib2.HTTPConnectionWithTimeout("api.thingspeak.com",80) try:
conn.request("POST", "/update", params, headers) response = conn.getresponse()
data = response.read() conn.close()
except:
print("connection failed") break
