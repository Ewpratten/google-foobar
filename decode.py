from base64 import b64decode
import json

config_data = open('identity.json').read()
config = json.loads(config_data)

code = config["secret"]
key = config["uname"]

message = []
len = len(key)
for i, c in enumerate(b64decode(code)):
    message.append(chr(c ^ ord(key[i % len])))
message = ''.join(message)


print(message)