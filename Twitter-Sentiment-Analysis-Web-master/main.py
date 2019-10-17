from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'LbU0zXo7k2alGJFB5WHab6Zi0'
consumer_secret = 'WyeYP3aMjcvgPiEY7ZE7GUGj5u7p5i6Axc5pJFijcZZrELbIRE'

access_token = '1062320024864473088-TwatEO1uRDTdn7VBT3RmKep8dXPU15 '
access_token_secret = 'bbv7nuQlR2DQF7G27Orfc8iixEqCb4cKPZ0B0Y9pIXQTn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()