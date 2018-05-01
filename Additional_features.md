Following the code samples from the agalea91 blog post might lead you to believe there is only a few features we can extract from the tweets. Fortunately there is actually  ~60 features recorded per tweet we can use!

Once you import the .json files using the code snippet by agelea91. You extract a single tweet and view all the feature stored regarding that tweet. 

    tweet_files = ['something.json']
    tweets = []
    for file in tweet_files:
    	with open(file, 'r') as f:
        	for line in f.readlines():
          	  tweets.append(json.loads(line))
    
    #View features for the second tweet
    tweets[2]
    
You can then build more complex and customized dataframes with the information you need.  

Here's an example.. 

    df = pd.DataFrame()
    def populate_tweet_df(tweets):
        df = pd.DataFrame()
     
        df['text'] = list(map(lambda tweet: tweet['text'], tweets))
         
        #df['possibly_sensitive'] = list(map(lambda tweet: tweet['possibly_sensitive'], tweets))
        
        df['retweet_count'] = list(map(lambda tweet: tweet['retweet_count'], tweets))
        
        df['favorite_count'] = list(map(lambda tweet: tweet['favorite_count'], tweets))
    
        df['retweeted']  = list(map(lambda tweet: tweet['retweeted'], tweets))
        
        df['favorite_count'] =  list(map(lambda tweet: tweet['favorite_count'], tweets))
        
        df['followers_count'] = list(map(lambda tweet: tweet['user']['followers_count'], tweets))
        
        df['screen_name']= list(map(lambda tweet: tweet['user']['screen_name'], tweets))
        
        df['verified']= list(map(lambda tweet: tweet['user']['verified'], tweets))
                if tweet['coordinates'] != None else 'NaN', tweets))
     
        return df
If your trying to extract a child feature, such as 'followers_count' , you need to first provide the parent feature 'user'