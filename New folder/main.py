"""
Created on Fri Jan 13 11:57:46 2017

@author: mayank singh
"""

#import numpy as np

# def train()
#from engines import content_engine
#content_engine.train('sample-data.csv')

def popular():
    popular_offer_list = [42593,26146,26298,26465,26626,45961,4620,30617,26000,43887,40322,45543,45932,38665]
    print("User Interaction Data insufficient, Showing Most Popular Offers")
    for i in range(0,5):
        print(popular_offer_list[i])

def predict(offer):
    from engines import content_engine
    num_predictions = 5
    offer_list=content_engine.predict(offer, num_predictions)
    print("Similar offers recommended for you:")
	for s in offer_list:
		print(*s)
    #print(offer_list)
    #r.get(offer)
    
    
# Generate random CustomerId 
# from random import randint
# or

cstid=2650

# Create dict with CustomerId and OfferId as key value Pair
# interaction latest contains user interaction data, customer id and offer id

import csv
with open('interaction latest.csv') as f:
    f.readline() # ignore first line (header)
    interactiondict = dict(csv.reader(f, delimiter=','))
    

# Use CustomerId from dict as key to get OfferId(value) and generate similar offer

offer=interactiondict[str(cstid)]
predict(offer)

#if cstid in interactiondict:
#    predict(interactiondict[cstid])
#else:
#    popular()