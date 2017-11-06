from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

consumer_key = "v7PBrhQmnQAnMNkfFYwKRZZ3t"
consumer_secret = "3HO5D8WJqszD6jXvUmLMXQk44zu8vXiQM2eo3QikYcrMC4IkDe"
access_token = "2360536770-fwFoH2gcoxD8aX8gJCdHXHMpfFH1cRUpgqoMZud"
access_token_secret = "c9iT2FJlfe6vv01Tn8xQJQIZkyXEzUfJJaky8J4uPRBjo"


class stdOutListener(StreamListener):
    lineCount = 0
    def on_data(self, data):
        tweet = json.loads(data)

        if 'text' in tweet and 'retweeted' in tweet:
            if not tweet['retweeted'] and \
                            'RT @' not in tweet['text'] and \
                            tweet['lang'] == "en":
                print(tweet['text'], '\n')
                print(self.lineCount)
                print("=============================")

                sentences = [tweet['text']]
                analyzer = SentimentIntensityAnalyzer()
                for sentence in sentences:
                    vs = analyzer.polarity_scores(sentence)
                    print("{:-<65} {}".format(sentence, str(vs)))

                with open('data.json', 'a') as f:
                    f.write(tweet['text'] + '\n')
                    # f.write(data)
                    self.lineCount += 1
                    if self.lineCount == 200:
                        return False
                    return True

    def on_error(self, status):
        print('status', status)

if __name__ == '__main__':
    l = stdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    stream = Stream(auth, l)
    stream.filter(track=["alphabet inc",
                         "artificial intelligence",
                         "machine learning",
                         "Google cloud platform",
                         "computer vision",
                         "deep learning"], async=True)



    # sentences = ["UCLA CSE sucks",
    #             "UCLA is the best!!"]
    # analyzer = SentimentIntensityAnalyzer()
    # for sentence in sentences:
    #     vs = analyzer.polarity_scores(sentence)
    #     print("{:-<65} {}".format(sentence, str(vs)))





