#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
consumer_key = 'ngUiFH7BGoDjoeRYFp6J4CISz'
consumer_secret = 'sLGTulZAxLThdluHb7RyGTF08jpc75NowJkwj8DaNNG8P7zbeA'
access_key = '2387367300-CsyGg6vQeV7reiGsOzFoRToHi7Jdskyie4Rf3GO'
access_secret = 'J6ivsjOUFilDm7llUgvXe87Cwk8NEGZQyCS9wmgOanINU'

#method to get a user's last tweets
def get_tweets():

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want
	date_since = "2021-03-17"
	date_until = '2021-03-20'

	query = 'bitcoin -filter:retweets'
	max_tweets = 1000
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=query, lang="en").items(max_tweets)]
	#get tweets
	tweets_for_csv = []

	for tweet in searched_tweets:
        #create array of tweet information: username, tweet id, date/time, text
		tweets_for_csv.append([tweet.user.screen_name, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.retweet_count, tweet.user.favourites_count])

	#write to a new csv file from the array of tweets
	outfile = "bitcoin" + "_tweets.csv"
	print("writing to " + outfile)
	with open(outfile, 'a') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)

#if we're running this as a script
if __name__ == '__main__':
    get_tweets()
