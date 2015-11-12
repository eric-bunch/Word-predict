import gzip
import math
import collections
from collections import defaultdict, Counter
import pickle
import json

# Natural Language Processing
import nltk
from nltk.tokenize import word_tokenize


def create_foll_wds_hash(genres):

	followingWordsHash = defaultdict(lambda: [], {})
	
	for genre in genres:
		f = gzip.open("../" + genre + ".txt.gz")

		for index, line in enumerate(f):
			if (index % 11) == 9:
				tokenizedReviewHash = {index: word for index, word in enumerate(word_tokenize(line[13:]))}
		
				for key in tokenizedReviewHash.keys()[:-1]:
					followingWordsHash[tokenizedReviewHash[key]] += [tokenizedReviewHash[key + 1]] 
		
		f.close()

		threeMostCommonHash = {}
		for word in followingWordsHash.keys():
			threeMostCommonHash[word] = [x[0] for x in Counter(followingWordsHash[word]).most_common(3)]
	
		with open(genre + "_three_most_common.pickle", 'w') as f:
			pickle.dump(threeMostCommonHash, f)
			
		followingWordsHash.clear()
		threeMostCommonHash.clear()


def consolidate(genres):

	consolidatedHash = {}
	
	for genre in genres:
		with open(genre + '_three_most_common.pickle', 'rb') as dictionary:
			consolidatedHash[genre] = pickle.load(dictionary)

	with open('Three_most_common_following_words_combined_list.json', 'w') as outfile:
		json.dump(consolidatedHash, outfile, sort_keys=True, indent=4, separators=(',',': '))	


genres_list = ['Arts', 'Automotive', 'Baby', 'Beauty', 'Gourmet_Foods', 'Jewelry']

create_foll_wds_hash(genres_list)
consolidate(genres_list)



