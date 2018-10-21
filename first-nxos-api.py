import requests
import json

url = 'http://10.10.10.25/ins'
https_header = {'content-type':'application/json-rpc'}

reqList = []
reqItem1 = {
    "jsonrpc":"2.0",
    "method":"cli",
    "params": {"cmd": "vlan 2", "version": 1},
    "id": 1
}
reqList.append(reqItem1)

reqItem2 = {
    "jsonrpc":"2.0",
    "method":"cli",
    "params": {"cmd":"interface vlan 2", "version": 1 },
    "id": 1
}
reqList.append(reqItem2)

reqItem3 = {
    "jsonrpc":"2.0",
    "method":"cli",
    "params": {"cmd":"ip address 200.200.200.254 255.255.255.0", "version": 1},
    "id": 1
}
reqList.append(reqItem3)

showItem1 = {
    "jsonrpc":"2.0",
    "method":"cli",
    "params": {"cmd":"show ip interface brief", "version": 1},
    "id": 1
}

https_payload = json.dumps(reqList)
resp = requests.post(url, data=https_payload, headers=https_header, auth=('admin' , 'password123'))
json_resp = resp.json()

http_resp = json.dumps(showItem1)
resp1 = requests.get(url, data=http_resp, headers=https_header ,  auth=('admin' , 'password123'))
#json_resp1 = resp1.json()
print(resp1)