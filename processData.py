import json
import csv

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Preprocessor:
    dataText = ""

    # get histogram for whole tweets
    def readDataFile(self):
        with open('tweet_score.csv', 'w') as csvfile:
            fieldnames = ['neg', 'neu', 'pos', 'compound']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            with open('data.json', 'r') as f:
                for line in f:
                    sentences = [line]
                    analyzer = SentimentIntensityAnalyzer()
                    for sentence in sentences:
                        vs = analyzer.polarity_scores(sentence)
                        writer.writerow({'neg': vs['neg'], 'neu': vs['neu'], 'pos': vs['pos'], 'compound': vs['compound']})


if __name__ == '__main__':
    p = Preprocessor()
    p.readDataFile()
