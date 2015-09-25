def pulldate(tweet):
	pipeloc = tweet.find("|")
	pipeloc2 = tweet.find("|", pipeloc+1)
	pipecont = tweet [pipeloc+1:pipeloc2]
	#print pipecont
JalopnikDates = open("JalopnikTitles")
JDates = list(JalopnikDates)
for i in range(len(JDates)):
	pulldate(JDates[i])

def pulltitle(tweet2):
	titleloc = tweet2.find("|")
	titleloc2 = tweet2.find("|", titleloc+1)
	titleloc3 = tweet2.find("http")
	titlecont = tweet2[titleloc2+1:titleloc3]
	print titlecont
for i in range(len(JDates)):
	pulltitle(JDates[i])
JalopnikDates.close()



