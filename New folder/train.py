"""
Created on Mon Jan 16 01:30:40 2017

@author: mayank singh

sample-data is collection of offer ids and their descriptions(Harvested from OfferMaster.csv)
on which TF-IDF is run and their cosine similarities calculated and stored in redis.

sample-data length has been reduced considerabaly in order to compensate for low RAM




"""

from engines import content_engine
content_engine.train('sample-data.csv')