# `twitter_search.py` data-mining Python 3 script

[My blog post](https://galeascience.wordpress.com/2016/03/18/collecting-twitter-data-with-python/) gives a thorough explanation of how to set up the code (including the dependancies), what it's doing, and an example how to use the resulting tweet data.  I've also included the basics below.

This program will search for tweets and save them to a .JSON formatted file. Twitter limits the amount of tweets that can be downloaded per 15 minutes; as such, when an exception is raised (i.e., the maximum allowed number of tweets has been reached) the script will pause for 15 minutes and then continue.


### Dependencies

To access the Twitter API I used Tweepy 3.5.0.  I also imported the libaraies: json, datetime, time, os and sys.

In addition, you'll need a personal [Twitter "data-mining" application](https://apps.twitter.com/) (which is very easy to set up). I used [this guide] (http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/#Register_Your_App) to register my app. You will need to register your own in order to generate a consumer key, consumer secret, access token, and access secret; these are required to authenticate the script in order to access the Twitter API.


### Running the script

1) Save the python file or download/clone the repository to your local machine.  Make sure you have the dependencies.

2) Open the `twitter_search.py` file and then find the `load_api()` function (at the top) and add your consumer key, consumer secret, access token, and access secret.  For example:
```
consumer_key = '189YcjF4IUzF156RGNGNucDD8'
consumer_secret = 'd7HY36s4pSh03HxjDg782HupUjmzdOOSDd98hd'
access_token = '2543812-cpaIuwndjvbdjaDDp5izzndhsD7figa9gb'
access_secret = '4hdyfnas7d988ddjf87sJdj3Dxn4d5CcNpwe'
```

3) Go to the `main()` function and edit the search criteria. Namely, you should enter a search phrase, the maximum time limit for the script to run, and the date range for the search (relative to today). For example:
```
search_phrase = '#makedonalddrumpfagain'
time_limit = 1.0 # runtime limit in hours
min_days_old, max_days_old = 1, 2 # search limits

# e.g. min_days_old, max_days_old = 7, 8
# gives the current weekday from last week,
# min_days_old=0 will search from right now
```

4) Open the terminal/command line to the file location and type: 
```
python twitter_search.py
```
The script will run until all tweets within your search criteria have been found.


#### Copyright (c) 2016 Alexander Galea 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
