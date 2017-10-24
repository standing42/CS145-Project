import json
import csv


class Preprocessor():
    relatedWordsDict = {}
    keywordCountDict = {}
    dataText = ""

    def readKeywordFile(self):
        with open('related_keyword.csv', 'r') as f:
            reader = csv.DictReader(f)
            # for row in reader:
            #     print(row)

            for row in reader:
                for i in row:
                    if len(i) > 1:
                        self.keywordCountDict[i] = 0
                        self.relatedWordsDict[row[i]] = []
                        self.relatedWordsDict[row[i]] = i
                        # print(row[i], self.relatedWordsDict[row[i]])
            # print(self.relatedWordsDict)
            # print(self.keywordCountDict)

    def readDataFile(self):
        with open('data.json', 'r') as f:
            for line in f:
                tweet = json.loads(line)
                # print(json.dumps(tweet, indent=4))
                if 'text' in tweet:
                    # print(tweet['text'])
                    self.dataText += tweet['text']
        # print("data text is \n", self.dataText.replace('\n', ' '))
        self.dataText = self.dataText.replace('\n', ' ')
        self.dataText = self.dataText.split(' ')
        print(self.dataText)

    def countMatchingKeyword(self):
        for i in self.dataText:
            if i in self.relatedWordsDict:
                self.keywordCountDict[self.relatedWordsDict[i]] += 1

if __name__ == '__main__':
    p = Preprocessor()
    p.readKeywordFile()
    p.readDataFile()
