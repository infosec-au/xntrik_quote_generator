import random
import requests
import json

def grab_random_tweet():
	# xntrik twitter feed every 30 mins
	r = requests.get("https://www.kimonolabs.com/api/6vpcqy4m?apikey=D8j6OeleId1EB8GbMHj9Fx3F3Wzfyxu0")
	xntrik_api = json.loads(r.text)
	xntrik_tweets = []
	for i in xntrik_api['results']['collection1']:
		author = i['property3']
		tweet = i['tweet_content']['text']
		if author['href'] == "https://twitter.com/xntrik" and tweet.encode('ascii', 'ignore') != "":
			xntrik_tweets.append(tweet.encode('ascii', 'ignore'))
	random_tweet = random.choice(xntrik_tweets)
	return random_tweet

def random_quote():
	wisdom_quotes = ["How do I add hipster to the cloud",
					 "You know my browser can see your browser yeah bro?",
					 "people call me big daddy for a reason",
					 "I miss my beard",
					 "Oi, who told me it was a good idea to get rid of my beard omg",
					 "I eat XSS daily bro you got nothin on me",
					 "Did you know I have a book?????? <http://www.amazon.com/Browser-Hackers-Handbook-Wade-Alcorn/dp/1118662091>",
					 "I will out-drum you any day, kiddo",
					]
	return random.choice(wisdom_quotes)

def random_bios():
	bios = ["Javascript overlord",
			"Browser Hogger",
			"proff js executor (I kill js daily)",
			"console.log('sickest drummer in WA');",
			"dark rider",
			"Hipster",
			"cfro",
			"big daddy",
			"Ruby overlord",
			"christian fricHOT",
			"1=1 expert",
			"i co-authored a book you know",
			"Professional Box Popper",
			"bearded gate keeper"
			]
	return random.choice(bios)

quote = random.choice([grab_random_tweet, random_quote])()

print quote + " - Christian Frichot	, " + random_bios() + "."