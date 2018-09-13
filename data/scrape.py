from twitterscraper import query_tweets
import csv
import sys
import unicodecsv as csv
import datetime as dt
#from dateutil import parser

def scrape_string(mystring):
	print('Scrape: ' + mystring + ' started')
	params = mystring.split()
	scrape(params[0],params[1],params[2])
	print('Scrape: ' + mystring + ' completed')

def scrape(query_text,start_date,end_date):
    start = dt.datetime.now()
    i = 0

    filename = query_text + '-' + start_date + '.csv' 
    with open(filename, 'wb') as csvfile:
        tweetwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='\"', quoting=csv.QUOTE_ALL, encoding='utf-8')
	attempts = 1
	while (attempts <= 20):
        	for tweet in query_tweets(query='"' + query_text + '"', begindate=dt.datetime.strptime(start_date,'%Y-%m-%d').date(),enddate=dt.datetime.strptime(end_date,'%Y-%m-%d').date(),lang='en',poolsize=1):
            		tweetwriter.writerow([tweet.id, tweet.timestamp, tweet.user, tweet.fullname, tweet.text, tweet.replies, tweet.retweets, tweet.likes])
            		i = i + 1
		#retry if there are too few tweets
		if (i >= 1000):
			break
		else:
			attempts = attempts + 1
			print ('RETRY - ATTEMPT ' + str(attempts) + ' ' + filename)

    end = dt.datetime.now()
    print('Saved ' + filename + 'containing ' + str(i) + ' tweets, load duration was ' + str(end - start) + ' seconds.')

if __name__ == '__main__':
        scrape(sys.argv[1], sys.argv[2], sys.argv[3])
