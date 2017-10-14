"""
Created on Fri Jan 13 11:57:46 2017
@author: mayank singh

If sample data latest is not being used to train engine in train.py 

Output is sometimes blank "Similar offers recommended for you:" 
then it means that offerid is not present in redis store due to trimming 
of sample data.csv, 

In such a case look for supplied cstid in interaction latest.csv
and find corresponding offerid, 

Then Edit any record in "sample data.csv" and replace the id feild 
with offerid fetched earlier.


"""

def popular():
    print("User Interaction Data insufficient, Showing Most Popular Offers with frequency")
    # Prints popular offers with their frequiencies
    for i in most_pop_offerlist[:5]:
        print(i[0], i[1])


def predict(offer):
    from engines import content_engine
    num_predictions = 5
    print("Similar offers recommended for you:")
    similar_offer_list=content_engine.predict(offer, num_predictions)
    # prints similar offers along with their similarity score
    for s in similar_offer_list:
        print(int(s[0]),s[1])
    
    
    
    
# Generate random CustomerId 
# from random import randint
# cstid=randint(2,4268)
# or supply specific cstid 
cstid=100


# Create dict with CustomerId and OfferId as key value Pair
# interaction latest contains user interaction data, customer id and offer id
# extracted from events_data json 
import csv
with open('interaction latest.csv') as f:
    f.readline() # ignore first line (header)
    interactiondict = dict(csv.reader(f, delimiter=','))


# create a nested list of offers with their frequency in interactiondict (most popular offers)
# along with their frequency sorted in decending order    
    
from collections import Counter
most_pop_offerlist=Counter(interactiondict.values()).most_common()    

# Use CustomerId from dict as key to get OfferId(value) and generate similar offer

cstid=str(cstid)

if cstid in interactiondict:
    predict(interactiondict[cstid])
else:
    popular()