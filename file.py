import requests
import json
f = requests.get('http://localhost:5000/api').json()
print(f['downClientLink'])
