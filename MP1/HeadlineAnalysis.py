import collections
from pattern.en import *

def pulldate(tweet): #This function pulls the date from the JalopnikTitles file by locating the two pipes (|), and printing what is between them
	pipeloc = tweet.find("|")
	pipeloc2 = tweet.find("|", pipeloc+1)
	pipecont = tweet [pipeloc+1:pipeloc2]
	print pipecont
		

def pulltitle(tweet2): #This function pulls the title by again locating the pipes, and then priting the text between the second pipe and the string ("http")
	titleloc = tweet2.find("|")
	titleloc2 = tweet2.find("|", titleloc+1)
	titleloc3 = tweet2.find("http")
	titlecont = tweet2[titleloc+1:titleloc3]
	return titlecont



JalopnikDates = open("JalopnikTitles")
JDates = list(JalopnikDates) #This list prints all the dates and titles from JalopnikTitles
for i in range(len(JDates)):
	print pulltitle(JDates[i])


matched_tweets = {} #This is my dictionary that matches headlies to automaker names that appear in them. Following are the lists for each manufacturer.

ferrari = []
bmw = []
audi = []
lamborghini = []
mercedes = []
mclaren = []

ferrari_pos = []
ferrari_neg = []
bmw_pos = []
bmw_neg = []
audi_pos = []
audi_neg = []
lamborghini_pos = []
lamborghini_neg = []
mercedes_pos = []
mercedes_neg = []
mclaren_pos = []
mclaren_neg = []



for tweet in JDates: #This loop defines positive and negative terms for each list.
	tweet = tweet.lower()
	tweet = pulltitle(tweet)
	if "ferrari" in tweet:
		ferrari.append(tweet)
		if "best" in tweet or "good" in tweet or "cool" in tweet or "awesome" in tweet or "amazing" in tweet or "fast" in tweet:
			ferrari_pos.append(tweet)
		if "slow" in tweet or "worst" in tweet or "bad" in tweet or "break" in tweet or "crash" in tweet or "fire" in tweet or "crap" in tweet or "destroy" in tweet or "wreck" in tweet or "asshat" in tweet:
			ferrari_neg.append(tweet)
	elif "bmw" in tweet:
		bmw.append(tweet)
		if "best" in tweet or "good" in tweet or "cool" in tweet or "awesome" in tweet or "amazing" in tweet or "fast" in tweet:
			bmw_pos.append(tweet)
		if "slow" in tweet or "worst" in tweet or "bad" in tweet or "break" in tweet or "crash" in tweet or "fire" in tweet or "crap" in tweet or "destroy" in tweet or "wreck" in tweet or "asshat" in tweet:
			bmw_neg.append(tweet)
	elif "audi" in tweet:
		audi.append(tweet)
		if "best" in tweet or "good" in tweet or "cool" in tweet or "awesome" in tweet or "amazing" in tweet or "fast" in tweet:
			audi_pos.append(tweet)
		if "slow" in tweet or "worst" in tweet or "bad" in tweet or "break" in tweet or "crash" in tweet or "fire" in tweet or "crap" in tweet or "destroy" in tweet or "wreck" in tweet or "asshat" in tweet:
			audi_neg.append(tweet)
	elif "lamborghini" in tweet:
		lamborghini.append(tweet)
		if "best" in tweet or "good" in tweet or "cool" in tweet or "awesome" in tweet or "amazing" in tweet or "fast" in tweet:
			lamborghini_pos.append(tweet)
		if "slow" in tweet or "worst" in tweet or "bad" in tweet or "break" in tweet or "crash" in tweet or "fire" in tweet or "crap" in tweet or "destroy" in tweet or "wreck" in tweet or "asshat" in tweet:
			lamborghini_neg.append(tweet)	
	elif "mercedes" in tweet:
		mercedes.append(tweet)
		if "best" in tweet or "good" in tweet or "cool" in tweet or "awesome" in tweet or "amazing" in tweet or "fast" in tweet:
			mercedes_pos.append(tweet)
		if "slow" in tweet or "worst" in tweet or "bad" in tweet or "break" in tweet or "crash" in tweet or "fire" in tweet or "crap" in tweet or "destroy" in tweet or "wreck" in tweet or "asshat" in tweet:
			mercedes_neg.append(tweet)
	elif "mclaren" in tweet:
		mclaren.append(tweet)
		if "best" in tweet or "good" in tweet or "cool" in tweet or "awesome" in tweet or "amazing" in tweet or "fast" in tweet:
			mclaren_pos.append(tweet)
		if "slow" in tweet or "worst" in tweet or "bad" in tweet or "break" in tweet or "crash" in tweet or "fire" in tweet or "crap" in tweet or "destroy" in tweet or "wreck" in tweet or "asshat" in tweet:
			mclaren_neg.append(tweet)


matched_tweets["ferrari"] = ferrari
matched_tweets["ferrari_pos"] = ferrari_pos
matched_tweets["ferrari_neg"] = ferrari_neg

matched_tweets["bmw"] = bmw
matched_tweets["bmw_pos"] = bmw_pos
matched_tweets["bmw_neg"] = bmw_neg

matched_tweets["audi"] = audi
matched_tweets["audi_pos"] = audi_pos
matched_tweets["audi_neg"] =audi_neg

matched_tweets["lamborghini"] = lamborghini
matched_tweets["lamborghini_pos"] = lamborghini_pos
matched_tweets["lamborghini_neg"] = lamborghini_neg

matched_tweets["mercedes"] = mercedes
matched_tweets["mercedes_pos"] = mercedes_pos
matched_tweets["mercedes_neg"] = mercedes_neg

matched_tweets["mclaren"] = mclaren
matched_tweets["mclaren_pos"] = mclaren_pos
matched_tweets["mclaren_neg"] = mclaren_neg


matched_tweets = collections.OrderedDict(sorted(matched_tweets.items())) #This sorts my output by manufacturer.

JalopnikDates.close()

#print(matched_tweets)
for key in matched_tweets.keys(): #This loop matches lists to string keys and includes the sentiment analysis portion.
	print "\n"
	print key
	for tweet in matched_tweets[key]:
		if "_pos" in key or "_neg" in key:
			print tweet
			print sentiment(tweet)[0]

		else: 
			print tweet








