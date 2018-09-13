import requests
import sentiment
import sys
import os
import datetime
import re

while (True):
	response = requests.post('http://queue:8080/memq/server/queues/bitcoin2/dequeue')
	if (response.status_code == 200):
		message_str = response.json()['body']
		print(message_str)
		filestr = re.escape(message_str)
		command_str = 'gsutil cp gs://isye-7406/' + filestr + '.csv .'
		os.system(command_str)
        	sentiment.analyze(message_str)
                command_str = 'gsutil cp ./' + filestr + '_nlp.csv gs://isye-7406/nlp/' + filestr + '_nlp.csv' 
		print(command_str)
                os.system(command_str)
	else:
		break
sys.exit(0)
