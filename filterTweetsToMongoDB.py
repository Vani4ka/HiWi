import os
import json
import re
import nltk
from nltk.corpus import stopwords #using the stopwords from the python nltk library
import classes

rootdir = '/home/vanya/HiWi/webis-cbc-16/problems'
filtereddir = '/home/vanya/HiWi/filteredTweets/'
		
		
def jdefault(o):
	return o.__dict__

#filter the fields to be in the new json
def filterTweets(json_data, name):
	full = json.load(json_data)
	filtered = {}

	filtered["id_str"] = full["id_str"]
	filtered["created_at"] = full["created_at"]
	filtered["retweet_count"] = full["retweet_count"]
	filtered["favorite_count"] = full["favorite_count"]
	filtered["text"] = full["text"]

	words = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",full["text"].lower()).split()

	bagOfWords = {}

	for word in words:
		if word not in stopwords.words("english") and word !="rt":
			if word in bagOfWords:
				bagOfWords[word] +=1;
			else:
				bagOfWords[word] = 1;


	filtered["bag_of_words"] = bagOfWords
			
	entities = classes.Entities(full["entities"])
	filtered["entities"] = entities

	user = classes.User(full["user"])
	filtered["user"] = user

	output = open(filtereddir + "filtered" + name, "w+")
	json.dump(filtered, output, default = jdefault)


# filter the original tweets
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
    	if file.endswith(".json"):
    		read = os.path.join(subdir, file)
    		filterTweets(open(read), file)


# save the filtered tweets in mongoDB
# for subdir, dirs, files in os.walk(filtereddir):
#     for file in files:
#     	if file.endswith(".json"):
#     		os.system("mongoimport --db tweetsDB --collection filteredTweets --type json --file " + os.path.join(subdir, file))