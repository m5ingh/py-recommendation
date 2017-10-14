Requirements: 
Development environment= Anaconda Spyder 3.0.2(Python version 3.5.2)
Installation of redis in Spyder
Redis server should be up and running and listening for connections on port 6379(defalut)

Execution order:
Train.py
Main.py

Deployment:
For greater accuracy of result it is recommended to use "sample data latest.csv" to train engine.
Since "sample data latest.csv" is quite a large file for training use a system with RAM(>=8gb) preferabally a server

If sample data latest is not being used to train engine in train.py 

Output is sometimes blank "Similar offers recommended for you:" 
then it means that offerid is not present in redis store due to trimming 
of sample data.csv, 

In such a case look for supplied cstid in interaction latest.csv
and find corresponding offerid, 

Then Edit any record in "sample data.csv" and replace the id field 
with offerid fetched earlier and run again.

"MONITOR" command can be used in redis-cli to obsereve ongoing operations on redis-server.



List of files and description:
sample data.csv		  : Collection of offerids and their descriptions(Harvested from OfferMaster.csv).
					    has been trimmed considerably in order to compensate for low RAM.

sample data latest.csv: Contains untrimmed dataset including all offerids,should be considered
					    for deployment on a system with a large(>=8Gb) RAM preferabally a server 

interaction latest.csv: Contains user interaction data, customer id and offer id extracted from events_data json file.

main.py				  : Acts as interface for train.py and engine.py. For a supplied custid if interaction data is found for a cstid/user prints similar offer
						else prints popular offer(extracted by calculating frequency of each offer in interaction latest)
						if user interaction data is insufficient 

train.py			  : Trains the engine on sample data/specified file. 

engines.py			  : Contains two funcs:
						Train:For each offer Calculates Term frequency,Inverse document frequency and cosine similarities(from desciption of each offer) 
						and stores on REDIS(for each offer stores similar offers along with their similarity scores)
						
						Predict:Simply fetches data stored(similar offers along with their similarity scores)in redis associated with an offerid and prints them.
						
						
