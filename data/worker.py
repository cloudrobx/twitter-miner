import requests
import scrape
import sys
import datetime

while (True):
	response = requests.post('http://queue:8080/memq/server/queues/bitcoin/dequeue')
	if (response.status_code == 200):

		print(response.json()['body'])
        	scrape.scrape_string(response.json()['body'])
	else:
		break
sys.exit(0)
