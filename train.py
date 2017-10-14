"""
Created on Mon Jan 16 01:30:40 2017

@author: mayank singh

sample-data is collection of offer ids and their descriptions(Harvested from OfferMaster.csv)
on which TF-IDF is run and their cosine similarities calculated and stored in redis.

sample-data has been trimmed considerably in order to compensate for low RAM.

sample-data latest contains untrimmed dataset including all offerids,should be considered
for deployment on a system with a large(>=8Gb) RAM preferabally a server 

train.py is having only two lines of code but has a separate file
as it ensures server resources are not being over-utilized by running 
training every time a recommendation is required to be made. 
Train once and Predict multiple times.  

"""

from engines import content_engine
content_engine.train('sample-data.csv')
