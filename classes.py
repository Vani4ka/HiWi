class User(object):
	
	def __init__(self, user):
		self.id_str = user["id_str"]
		self.created_at = user["created_at"]
		self.name = user["name"]
		self.screen_name = user["screen_name"]
		self.followers_count = user["followers_count"]
		self.friends_count = user["friends_count"]
		self.location = user["location"]
		self.time_zone = user["time_zone"]
		self.statuses_count = user["statuses_count"]

class Entities(object):
	
	def __init__(self, entities):
		self.hashtags = entities["hashtags"]
		if "media" in entities:
			self.media = entities["media"]
		else:
			self.media = None


class Media(object):
	
	def __init__(self, media):
		self.url = media["url"]


class Tweet(object):
	"""docstring for Tweet"""
	def __init__(self, name, bag_of_words, id_str):
		
		self.name = name
		self.bag_of_words = bag_of_words
		self.id_str = id_str

class Pair(object):
	"""docstring for Pair"""
	def __init__(self, tweet1, tweet2, jac):
		self.tweet1 = tweet1
		self.tweet2 = tweet2
		self.jac = jac

	def __eq__(self, other):
		return ((self.tweet1.id_str == other.tweet2.id_str) and (self.tweet2.id_str == other.tweet1.id_str)) #or ((self.tweet1.id_str == other.tweet1.id_str) and (self.tweet2.id_str == other.tweet2.id_str))