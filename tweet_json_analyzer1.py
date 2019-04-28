#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:20:10 2019

@author: monica
"""

import json
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

tweets_data_path = 'NFLREST_SEC_Tweets3.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    tweet=json.loads(line)
    tweets_data.append(tweet);
    
tweets_file.close()  

hashtags = []

for i in tweets_data:
    if 'entities' in i:
        hashtags.extend(i['entities']['hashtags'])
        
hashtags = [tag['text'] for tag in hashtags]

hashtags_lower = [item.lower() for item in hashtags]

hashtag_count = Counter(hashtags_lower)

wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(hashtag_count)

plt.figure(figsize=(10, 10))
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.savefig('firstroundsecwordcloud.png', bbox_inches='tight')
plt.close()
