"""
Created on Thu Jan 12 14:30:51 2017

@author: mayank singh
"""
import pandas as pd
import time
import redis
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# host='http://127.0.0.1:6379' default or make env variable or add from_url in srtictredis
# if redis is being run on a server host param should contain ip address of the server port no(default 6379) 

class ContentEngine(object):

    SIMKEY = 'p:smlr:%s'

    def __init__(self):
        # if redis is being run on a server
        # self._r = redis.StrictRedis(host='server ip', port=port on which server is listening for connection (default 6379) , db=0)
        # if redis is being run locally
        self._r = redis.StrictRedis.from_url('http://127.0.0.1:6379')

    def train(self, data_source):
        start = time.time()
        ds = pd.read_csv(data_source)
        print("Training data ingested in %s seconds." % (time.time() - start))

        # Flush the stale training data from redis
        self._r.flushdb()

        start = time.time()
        self._train(ds)
        print("Engine trained in %s seconds." % (time.time() - start))

    def _train(self, ds):
        """
        Train the engine.

        Creates a TF-IDF matrix of unigrams, bigrams, and trigrams
        for each offer. The 'stop_words' param tells the TF-IDF
        module to ignore common english words like 'the', etc.

        Then compute similarity between all products using
        SciKit Leanr's linear_kernel (which in this case is
        equivalent to cosine similarity).

        Iterate through each item's similar items and store the
        10 most-similar. 

        Similarities and their scores are stored in redis as a
        Sorted Set, with one set for each item.

        :param ds: A pandas dataset containing two fields: description & id
        :return: Nothing
        """
        print("Training Engine...")
        tf = TfidfVectorizer(analyzer='word',
                             ngram_range=(1, 3),
                             min_df=0,
                             stop_words='english')
        tfidf_matrix = tf.fit_transform(ds['description'])

        cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

        for idx, row in ds.iterrows():
            similar_indices = cosine_similarities[idx].argsort()[:-10:-1]
            similar_items = [(cosine_similarities[idx][i], ds['id'][i])
                             for i in similar_indices]

            # First item is the item itself, so remove it.
            # This 'sum' turns a list of tuples into a single tuple:
            # [(1,2), (3,4)] -> (1,2,3,4)
            flattened = sum(similar_items[1:], ())
            self._r.zadd(self.SIMKEY % row['id'], *flattened)
    

    def predict(self, item_id, num):
        """
        Retrieves the similar items and their 'score' from redis.

        :param item_id: string
        
        :param num: number of similar items to return
        
        :return: A list of lists like: [["19", 0.2203],
        ["494", 0.1693], ...]. The first item in each sub-list is
        the item ID and the second is the similarity score. Sorted
        by similarity score, descending.
        """

        return self._r.zrange(self.SIMKEY % item_id,
                              0,
                              num-1,
                              withscores=True,
                              desc=True)
        

content_engine = ContentEngine()
