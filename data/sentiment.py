import argparse
import csv
import sys
import time
import unicodecsv as csv

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


def analyze(filename):
      print('NLP begin on ' + filename)
      client = language.LanguageServiceClient()

      with open(filename + '.csv', 'rb') as csvreadfile:
        tweetreader = csv.reader(csvreadfile, delimiter=',',
                            quotechar='\"', quoting=csv.QUOTE_ALL, encoding='utf-8')
     	with open(filename + '_nlp.csv', 'wb') as csvwritefile:
        	tweetwriter = csv.writer(csvwritefile, delimiter=',',
                            quotechar='\"', quoting=csv.QUOTE_ALL, encoding='utf-8')

        	i = 0
        	for row in tweetreader:
#          		print(row)
          		content = row[4]
#          		print(content)
          		document = types.Document(
            			content=content,
            			type=enums.Document.Type.PLAIN_TEXT,language='en')
          		annotations = client.analyze_sentiment(document=document)

#          		print_result(annotations)
			row.append(annotations.document_sentiment.score)
			row.append(annotations.document_sentiment.magnitude)
			tweetwriter.writerow(row)
          		i = i + 1
      print('NLP complete on ' + filename)
#          		if (i % 100 == 0):
#            			print(i)
#          		if (i % 599 == 0):
#				time.sleep(60)
#				if (i == 1000):
#					break

if __name__ == '__main__':
        analyze(sys.argv[1])
