import sys
import datetime
import requests

if __name__ == '__main__':
	
	start_dt = datetime.datetime.strptime(sys.argv[2],'%Y-%m-%d').date()
	end_dt = datetime.datetime.strptime(sys.argv[3],'%Y-%m-%d').date()
	days = (end_dt - start_dt).days
	for i in range(days):
		new_sd = start_dt + datetime.timedelta(days=i)
		nw_sd_str = datetime.datetime.strftime(new_sd,'%Y-%m-%d')
		msg_str = sys.argv[1] + '-' + nw_sd_str
		print(msg_str) 
		url = 'http://localhost:8080/memq/server/queues/bitcoin2/enqueue'
                r = requests.post(url, data=msg_str)
