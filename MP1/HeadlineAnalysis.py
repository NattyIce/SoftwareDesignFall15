import collections
from pattern.en import *

# this function is never actually being called so probably not necessary
def pulldate(tweet): #This function pulls the date from the JalopnikTitles file by locating the two pipes (|), and printing what is between them
	pipeloc = tweet.find("|")
	pipeloc2 = tweet.find("|", pipeloc+1)
	pipecont = tweet [pipeloc+1:pipeloc2]
	print pipecont
		
# because the tweet2 argument is a local variable within this function, you don't actually need to call it tweet2 (which you
# presumably did to distinguish from the "tweet" variable in the pulldate function). you can still just call it tweet if you want
def pulltitle(tweet2): #This function pulls the title by again locating the pipes, and then priting the text between the second pipe and the string ("http")
	titleloc = tweet2.find("|")
	titleloc2 = tweet2.find("|", titleloc+1)
	titleloc3 = tweet2.find("http")
	titlecont = tweet2[titleloc+1:titleloc3]
	return titlecont



JalopnikDates = open("JalopnikTitles")
JDates = list(JalopnikDates) #This list prints all the dates and titles from JalopnikTitles
# careful - the above comment is incorrect.  the list() function doesn't print all the dates and titles, it creates a list
# from the file you five it as an argument
# the for loop you wrote right below here actuall prints the dates and titles 
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

	# these if statements are a fantastic example of where functions are a good idea.  whenever you find yourself
	# copying and pasting the same code over and over, that's a good indicator you should be using a function instead
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

# your code here works fine, but as you might have noticed it's a little repetitive
# I wouldn't expect you to know this (I just learned a few weeks ago) but there's a cool way that python does what you're doing here for you
# the python function locals() returns a dictionary of every variable name in your code, with the string variable name as the key and the
# variable values as the value
# basically, exactly the same as what you do in making your matched_tweets dictionary here, but with extra variables you don't want
# so what you could do is to filter through the dictionary returned by locals and add the only the ones you want (the ones with car names in them)
# to your matched_tweets dictionary

# the following commented code would do this
# let me know if you don't understand - have questions
# again - this is not a bad thing about your code, just a fun way to do things with less coding work

# all_variables_dict = locals()
# for variable_name in all_variables_dict.keys():
# 	# each variable_name is a string that contains the name of one of the variables in your program
# 	# this is everything from the matched_dates dictionary and the JalopnikDates file to the names of your lists
# 	if "ferrari" in variable_name or "bmw" in variable_name or "audi" in variable_name or "lamborghini" in variable_name or "mercedes" in variable_name or "mclaren" in variable_name:
# 		# if the variable name contains a car name, it's one of our lists
# 		# the value of all_variables_dict at the key variable_name is just the list variable
# 		matched_tweets[variable_name] = all_variables_dict[variable_name]

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
			# this shows what the pattern sentiment analyzer thinks about tweets you /already/ flagged as positive or negative
			# but it would also be cool to see how mant tweets that you /didn't/ flag as positive or negative that pattern thinks are pos/neg
		else: 
			print tweet

# it would be a cool way to wrap up your project to have shown me not just the contents of the lists but also their lengths
# so then I could see through numbers (instead of scrolling through all the printed output) to see whether ferrari is more negative than audi or not

# nit-picky but you have a lot of blank lines at the end of your file that are unnecessary






