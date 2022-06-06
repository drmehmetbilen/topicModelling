def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if len(token) > 3:
            result.append(token)
    return result
  
def setTopics(tweets):
 for tweetID in range(len(tweets)):
  for index, score in sorted(lda_model_tfidf[bow_corpus[tweetID]], key=lambda tup: -1*tup[1]):
     tweets[tweetID].category=index
     tweets[tweetID].score = score
     break
    
processed_docs = df["message"].map(preprocess)
dictionary = gensim.corpora.Dictionary(processed_docs)
dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]

start = time.time()
topicCount=20
iterationCount=100
lda_model_tfidf = gensim.models.LdaMulticore(corpus_tfidf, num_topics=topicCount, id2word=dictionary, passes=iterationCount, workers=4)
stop = time.time()
print("Time :{}".format(int((stop-start)/60)))
for idx, topic in lda_model_tfidf.print_topics(-1):
    print('Topic: {} Word: {}'.format(idx, topic))
printModel(topicCount)

