import json
import string
import nltk
from nltk import word_tokenize 
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
import re
import random
from random import sample
from collections import Counter

wordList = ["confidential", "authentication", "cybersecurity", "breached", "hacked"]
punctuations = '''!()-[]…–``{};:'"’\,“<>./?@#$%^&*_~'''
allowedChar = "abcdefghijklmnopqrstuvwxyz1234567890"
wordCloud = []
wordCloud2 = []

# Read in the JSON information
with open('tweets.json', 'r') as f:
    tweet_dict = json.load(f)

# Get the words for the word cloud, remove all extra parts
for tweet in tweet_dict:
    if tweet['lang'] == 'en' and any(word in tweet['text'] for word in wordList):
        tokenize = [word.lower() for word in word_tokenize(tweet['text'])]
        flag = 0
        userLessWords = []
        for word in tokenize:
            if '@' in word:
                flag = 1
            elif flag == 1:
                flag = 0
            else:
                userLessWords.append(word)
                
        noStopWords = []
        for word in userLessWords:
            if word not in stopwords.words('english') and word != '\U0001f447' and word != '\U0001f603' and word != '\U0001f440' and word != 'rt':
                noStopWords.append(word)
        
        noPuncWords = []
        count = 0
        for word in noStopWords:
            count = 0
            for c in punctuations:
                if c not in word:
                    count = count + 1
                if count == len(punctuations):
                    noPuncWords.append(word)
                
        wordCloud.append(noPuncWords)        

with open('cloud.txt', "w") as output:
    output.write(str(wordCloud))
    
#-------------------------------------------------------------------------------

# Time of tweet collection    
# print("Begin: ", tweet_dict[-1]["created_at"])
# print("End: ", tweet_dict[0]["created_at"])

# Number of unique English tweets you collected
tweetIDs = []
for tweet in tweet_dict:
    if tweet['lang'] == 'en' and any(word in tweet['text'] for word in wordList):
        tweetIDs.append(tweet['id_str'])
# print ("Number of unique English tweets: ", len(Counter(tweetIDs).keys()))
    
# Number of unique users
userIDs = []
for tweet in tweet_dict:
    if tweet['lang'] == 'en' and any(word in tweet['text'] for word in wordList):
        userIDs.append(tweet['user']['id'])
# print ("Number of unique English users: ", len(Counter(userIDs).keys()))

# 10 random tweets
randomTweets = []
for tweet in tweet_dict:
    if tweet['lang'] == 'en' and any(word in tweet['text'] for word in wordList):
        randomTweets.append(tweet)
# print(random.sample(randomTweets, 10));

# print(random.sample(randomTweets, 50));
