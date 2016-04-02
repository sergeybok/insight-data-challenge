README


Sergiy V. Bokhnyak's submission for Insight Data Engineering Coding Challenge

Code written in Python 3 (I'm not sure if it runs for Python 2, I think you'd need to change all my ranges to xranges).

No dependencies other than standard Python libraries, including json, datetime, time, and sys. 

Two files: Graph.py and driver.py.
Graph.py: Has a class called Graph_Util that has a function that allows you to add tweets, inputting their tweets and creation times, a function that allows you to take out tags and edges that are older than 59 seconds after most recent tweet, and a function that calculates the average number of edges per node (hashtag).
driver.py that takes 2 args, an input text file which is a bunch of tweets in JSON form, and processes them as described by the coding challenge README, i.e. outputs the average number of edges per node for every 60 second window of tweets.


To run using run.sh file:

'''bash

insight-data-challenge$ bash run.sh

or

insight-data-challenge$ ./run.sh


To run it from command line:

''' bash

insight-data-challenge$ python ./src/driver.py [INPUT JSON TWEET FILE] [OUTPUT TXT FILE]

e.g.

insight-data-challenge$ python ./src/driver.py ./input_tweets/tweets.txt ./output_tweets/output.txt
