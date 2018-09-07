from requests.auth import HTTPBasicAuth
import requests

def takePhoto(nameForPhoto):
	r = requests.get('http://192.168.0.100/snapshot.cgi', auth=HTTPBasicAuth('foscam', 'FCm3l45ud4'))
	if r.status_code == 200:
		with open(nameForPhoto, 'wb') as f:
			f.write(r.content)
	r.connection.close()
