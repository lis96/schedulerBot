import requests
import json

BOT_TOKEN = '1056372053:AAEIn-HB0uTRZEPZQRL-DakPppdcNh5ucmU'
BASE_URL = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'

proxy = {
	'ip': '192.3.228.146',
	'port': '7384',
	'login': 'usa3090712',
	'password': 'rL3LBVUMLi'
}

"""
	getMe
	getUpdates
"""

r = requests.post(
	url=f'{BASE_URL}sendMessage',
	data={
		'chat_id':658118892,
		'text':'All right'
	},
	proxies={
		'http': 'http://{login}:{password}@{ip}:{port}'.format(
			ip=proxy['ip'],
			port=proxy['port'],
			login=proxy['login'],
			password=proxy['password']
		),
		'https': 'http://{login}:{password}@{ip}:{port}'.format(
			ip=proxy['ip'],
			port=proxy['port'],
			login=proxy['login'],
			password=proxy['password']
		)
	}
)

print(r)
print(json.dumps(r.json(), indent=4))

r = requests.get(
	url=f'{BASE_URL}getUpdates',
	proxies={
		'http': 'http://{login}:{password}@{ip}:{port}'.format(
			ip=proxy['ip'],
			port=proxy['port'],
			login=proxy['login'],
			password=proxy['password']
		),
		'https': 'http://{login}:{password}@{ip}:{port}'.format(
			ip=proxy['ip'],
			port=proxy['port'],
			login=proxy['login'],
			password=proxy['password']
		)
	}
)

print(r)
print(json.dumps(r.json(), indent=4))