import nltk
from nltk import tokenize
from nltk.corpus import twitter_samples,stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
import matplotlib.pyplot as plt
import random,re,string

nltk.download('twitter_samples')

pos_tweet = twitter_samples.strings('positive_tweets.json')
neg_tweet = twitter_samples.strings('negative_tweets.json')

print('Number of +ve tweets', len(pos_tweet))
print('Number of -ve tweets',len(neg_tweet))
print('\nThe type of all_positive_tweets is: ', type(pos_tweet))
print('The type of a tweet entry is: ', type(neg_tweet[0])) 

fig = plt.figure(figsize=(5,5))
labels = 'positive_tweets','negative_tweets'
value_positive = len(pos_tweet)
value_negative = len(neg_tweet)
value_positive = 1000
value_negative = 2020
sizes = [value_positive,value_negative]
plt.pie(sizes,labels=labels,autopct='%.2f%%')
plt.axis('equal')
plt.show()
print('\033[95m' + pos_tweet[random.randint(0,5000)])
print('\033[91m' + neg_tweet[random.randint(0,5000)])
tweet = pos_tweet[2277]
print(tweet)
nltk.download('stopwords')
print(tweet) 

tweet2 = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet) 
print(tweet2)

tweet3 = re.sub(r'#', '', tweet2) 
print(tweet3)
stopwords_english = stopwords.words('english')
print(string.punctuation)
tokenizer = TweetTokenizer(preserve_case=False)
tweet_tokenize = tokenizer.tokenize(tweet3)
tweets_clean =[]
for word in tweet_tokenize: 
    if (word not in stopwords_english and word not in string.punctuation): 
        tweets_clean.append(word) 
print('removed stop words and punctuation:') 
print(tweets_clean) 
