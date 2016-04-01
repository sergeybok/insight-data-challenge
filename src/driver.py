import json, sys, time, Graph
from datetime import datetime

# Input: Filename of txt file with JSON Tweets
# Output: tweets = [tweet_dict, tweet_dict, ...]
def get_tweets(filename):
	tweets = []
	txt = open(filename,"r")
	for line in txt:
		tweets.append(json.loads(line))
	txt.close()
	return tweets

# Input: String in the form provided by twitter's created_at
#	 e.g. "Wed Aug 27 13:08:45 +0000 2008"
# Output: pyton's DATETIME object corresponding to inputted date and time
def date_parser(dt):
        tm = time.strptime(dt, "%a %b %d %H:%M:%S +0000 %Y")
        return datetime.fromtimestamp(time.mktime(tm))

# Input: List of hashtag_dictionaries
# Output: List of the hashtags as strings
def hashtag_parser(l):
	tags = []
	for d in l:
		tags.append(d['text'])
	return tags


# Main method
def main():
	# Init Graph_Util object from Graph.py
	graph = Graph.Graph_Util()

	#
	# Get args from command line
	in_file = sys.argv[1]
	out_file = sys.argv[2]
	out = ""

	# Getting tweets
	tweets = get_tweets(in_file)


	for i in range(0, len(tweets)): # Iterate through tweets
		tags =[]
		try:
			tags = hashtag_parser(tweets[i]['entities']['hashtags'])
		except KeyError: 
			# Limit, not tweeet, skip
			continue

		if (len(tags) < 2): # Case: tweet has <2 tags, so can't add edges
			# Still need to update time though	
			graph.update_graph(date_parser(tweets[i]['created_at']))
			out += format(graph.get_avg_degree(), '.2f') + '\n'

		else : # Case: add tweet and update graph
			graph.add_tweet(tags,date_parser(tweets[i]['created_at']))
			out += format(graph.get_avg_degree(),'.2f') + '\n'

	#Write to out file
	f = open(out_file,"w")
	f.write(out)
	f.close()

#END

	

# Guard
if __name__=="__main__":
	main()

