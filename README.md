This script reads through a corpus of Amazon product reviews, obtained from SNAP: http://snap.stanford.edu/, and 
creates a dictionary for each genre. They keys of such a dictionary will be all the words occuring in all of the 
reviews in the corpus, and the values will be the three most common words that come after that word in the corpus 
of reviews. Then the script pickles them for later use. There is also a function defined that combines all of 
the dictionaries into one JSON file.  
