README


Sergiy V. Bokhnyak's submission for Insight Data Engineering Coding Challenge

Code written in Python 3 (I'm not sure if it runs for Python 2, I think you'd need to change all my ranges to xranges).

No dependencies other than standard Python libraries, including json, datetime, time, and sys. 


To run using run.sh file:

'''bash

coding-challenge$ bash run.sh

or

coding-challenge$ ./run.sh


To run it from command line:

''' bash

coding-challenge$ python ./src/driver.py [INPUT JSON TWEET FILE] [OUTPUT TXT FILE]

e.g.

coding-challenge$ python ./src/driver.py ./input_tweets/tweets.txt ./output_tweets/output.txt