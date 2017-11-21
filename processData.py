import json
import csv
import os

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class Preprocessor:
    dataText = ""

    def readDataFile(self):
        directory_in_str = "data/"
        directory = os.fsencode(directory_in_str)
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".json"):
                print(filename)
                temp_string = filename[0:13]
                print(temp_string)
                process_file_name = "sentiments/" + temp_string + ".csv"
                with open(process_file_name, 'w') as csvfile:
                    fieldnames = ['neg', 'neu', 'pos', 'compound']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    with open(directory_in_str + filename, 'r') as f:
                        for line in f:
                            sentences = [line]
                            analyzer = SentimentIntensityAnalyzer()
                            for sentence in sentences:
                                vs = analyzer.polarity_scores(sentence)
                                writer.writerow({'neg': vs['neg'],
                                                 'neu': vs['neu'],
                                                 'pos': vs['pos'],
                                                 'compound': vs['compound']})
                continue
            else:
                continue

    # get histogram for whole tweets
    # def readDataFile(self):
    #     with open('tweet_score.csv', 'w') as csvfile:
    #         fieldnames = ['neg', 'neu', 'pos', 'compound']
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #         with open('data.json', 'r') as f:
    #             for line in f:
    #                 sentences = [line]
    #                 analyzer = SentimentIntensityAnalyzer()
    #                 for sentence in sentences:
    #                     vs = analyzer.polarity_scores(sentence)
    #                     writer.writerow({'neg': vs['neg'], 'neu': vs['neu'], 'pos': vs['pos'], 'compound': vs['compound']})


if __name__ == '__main__':
    p = Preprocessor()
    p.readDataFile()
