# List of imports
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

# Global variables
wordList = ["confidential", "authentication", "cybersecurity", "breached", "hacked"]
punctuations = '''!()-[]…–``{};:'"’\,“<>./?@#$%^&*_~'''
allowedChar = "abcdefghijklmnopqrstuvwxyz1234567890"
wordCloud = []

# Read in the JSON information
with open('tweets.json', 'r') as f:
    tweet_dict = json.load(f)

# Get the words for the word cloud, remove all extra parts
for tweet in tweet_dict:
    if tweet['lang'] == 'en' and any(word in tweet['text'] for word in wordList):
        tokenize = [word.lower() for word in word_tokenize(tweet['text'])] # Splits each word
        flag = 0
        # Removes all the "@" symbols
        userLessWords = []
        for word in tokenize:
            if '@' in word:
                flag = 1
            elif flag == 1:
                flag = 0
            else:
                userLessWords.append(word)
        
        # Remove all the stop words
        noStopWords = []
        for word in userLessWords:
            if word not in stopwords.words('english') and word != '\U0001f447' and word != '\U0001f603' and word != '\U0001f440' and word != 'rt':
                noStopWords.append(word)
        
        # Remove all punctuations
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
print("Begin: ", tweet_dict[-1]["created_at"])
print("End: ", tweet_dict[0]["created_at"])

# Number of unique English tweets you collected
tweetIDs = []
for tweet in tweet_dict:
    if tweet['lang'] == 'en' and any(word in tweet['text'] for word in wordList):
        tweetIDs.append(tweet['id_str'])
print ("Number of unique English tweets: \n", len(Counter(tweetIDs).keys()))
    
# Number of unique users
userIDs = []
for tweet in tweet_dict:
    if tweet['lang'] == 'en' and any(word in tweet['text'] for word in wordList):
        userIDs.append(tweet['user']['id'])
print ("Number of unique English users: \n", len(Counter(userIDs).keys()))

# 10 random tweets
randomTweets = []
for tweet in tweet_dict:
    if tweet['lang'] == 'en' and any(word in tweet['text'] for word in wordList):
        randomTweets.append(tweet)
print("List of 10 random tweets: \n", random.sample(randomTweets, 10));

# 50 random tweets
print("List of 50 random tweets: \n", random.sample(randomTweets, 50));
