execution order
execute train.py
execute main.py
 
requires installation of redis server.Redis cli in MONITOR mode shows similar items are calculated and stored during training, it also shows predict function being executed(see attached image). 
however the same is not being printed in main.py predict function

def predict(offer):
    from engines import content_engine
    num_predictions = 5
    offer_list=content_engine.predict(offer, num_predictions)
    print("Similar offers recommended for you:")
	for s in offer_list:
		print(*s)
