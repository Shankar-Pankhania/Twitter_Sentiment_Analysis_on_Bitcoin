import sys
import csv
import tweepy

#Get the Twitter API credentials
consumer_key = 'ngUiFH7BGoDjoeRYFp6J4CISz'
consumer_secret = 'sLGTulZAxLThdluHb7RyGTF08jpc75NowJkwj8DaNNG8P7zbeA'
access_key = '2387367300-CsyGg6vQeV7reiGsOzFoRToHi7Jdskyie4Rf3GO'
access_secret = 'J6ivsjOUFilDm7llUgvXe87Cwk8NEGZQyCS9wmgOanINU'

#method to get a user's last tweets
def get_tweets():
        
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)


	query = 'bitcoin -filter:retweets'
	max_tweets = 1000
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=query, lang="en").items(max_tweets)]

	#get tweets
	tweets_for_csv = []

	for tweet in searched_tweets:
                #create array of tweet information: username, tweet id, date/time, text
		tweets_for_csv.append([tweet.user.screen_name, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.retweet_count, tweet.user.favourites_count])

	#appends to the csv file from the array of tweets
	outfile = "bitcoin" + "_tweets.csv"
	print("writing to " + outfile)
	with open(outfile, 'a') as file:
                writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)

if __name__ == '__main__':
    get_tweets()
