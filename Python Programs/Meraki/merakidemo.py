import requests
import json

url = "https://dashboard.meraki.com/api/v0/organizations"

headers = {
    'X-Cisco-Meraki-API-Key': "6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
    'User-Agent': "PostmanRuntime/7.16.3",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "67a3f4c9-bcb4-43a5-bcde-c05ec3e976af,b27f7dd9-3ebc-4d17-a0a8-d62ab5cafb99",
    'Accept-Encoding': "gzip, deflate",
    'Referer': "https://api.meraki.com/api/v0/organizations",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.get(url, headers=headers)
meraki_api_data=response.json()

#print(json.dumps(response, indent=2, sort_keys=True))

for response_org in meraki_api_data:
    if response_org['name'] == 'DevNet Sandbox':
        orgId = response_org['id']

# print(orgId)

net_url = f'{url}/{orgId}/networks'

networks = requests.get(net_url, headers=headers)
meraki_networks = networks.json()
print(json.dumps(meraki_networks, indent=2, sort_keys=True))
for network in meraki_networks:
    if network['name'] == 'DNSMB2':
        netId = network['id']


dev_url = f'https://dashboard.meraki.com/api/v0/networks/{netId}/devices'
devices = requests.get(dev_url, headers=headers)
meraki_devices=devices.json()
print('*' * 50)
print(json.dumps(meraki_devices, indent=2, sort_keys=True))
print('*' * 50)
print(' ')
cli_url = f'https://dashboard.meraki.com/api/v0/networks/{netId}/clients'
clients = requests.get(cli_url, headers=headers)
meraki_clients=clients.json()
print('*' * 50)
print(json.dumps(meraki_clients, indent=2, sort_keys=True))
print('*' * 50)
print(' ')