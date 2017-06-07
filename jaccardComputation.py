import os
import json
import re
import utils
import classes

rootdir = '/home/vanya/HiWi/filteredTweets/'

def computeJaccard(tweet1, tweet2):
	if(tweet1.id_str != tweet2.id_str):
		bow1 = tweet1.bag_of_words.keys()
		bow2 = tweet2.bag_of_words.keys()

		intersect = list(set(bow1) & set(bow2))
		union = list(set(bow1) | set(bow2))
		j = float(len(intersect))/ len(union)
		jac = round(j,2)

	else:
		jac = round(1,2)
	
	return jac
			
		
def extractTweets(json_data):
	full = json.load(json_data)
	user = classes.User(full["user"])

	tweet = classes.Tweet(user.name, full["bag_of_words"], full["id_str"])
	tweets.append(tweet)	

def extractUsers(json_data):
	full = json.load(json_data)
	

	user = classes.User(full["user"])
	name = user.name
	if name not in names:
		names.append(name)


names = []
tweets = []
pairs = []
coefficients = []

def main():

	#  fillst the lists with the tweets and user names
	utils.traverseFiles(extractUsers, rootdir)
	utils.traverseFiles(extractTweets, rootdir)


	# creates list with pairs of tweets

	# i=1;

	tweetslist = list(tweets)
	print("Number of tweets: " + str(len(tweetslist)))

	for tweet1 in tweets:
		for tweet2 in tweetslist:
			jac = computeJaccard(tweet1, tweet2)
			pair = classes.Pair(tweet1, tweet2, jac)
			pairs.append(pair)

			# i+=1
			# if(i%5000==0):
			# 	print(i)

		tweetslist.pop(0)

	for j in pairs:
		if j.jac not in coefficients:
			coefficients.append(j.jac)

	print("News sources: ")
	print(names)
	print("Number news sources: ")
	print(len(names))
	print("Different Jaccard coefficients (rounded to 2 digits after the comma): ")
	print(coefficients)
	print("Number different jaccard coefficients: " + str(len(coefficients)))

	print("Number pairs of tweets: " + str(len(pairs)))

if __name__ == '__main__':
	main()