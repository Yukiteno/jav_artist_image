import requests

headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get('http://www.vgtime.com/topic/1147399.jhtml', headers=headers)
print(r.text)