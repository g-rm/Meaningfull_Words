def alt_lexical_diversity(text):
    return len(set(text)) / len(text) * 100


def tf_idf(corpus, stopwords, top_n_words=9):
    vectorizer = TfidfVectorizer(stop_words=stopwords, ngram_range=(1,2))
    X = vectorizer.fit_transform(corpus)

    feature_array = np.array(vectorizer.get_feature_names())

    score_list = []
    size = len(corpus)

    for i in range(size):
        #scores in a single doc
        tfidf_score_single_doc = X[i].toarray().flatten()
        #ordering
        indices = np.argsort(tfidf_score_single_doc)[::-1]
        #group feature and score
        local_top_features = [(feature_array[j], tfidf_score_single_doc[j]) for j in indices]
        #add to global list
        score_list.extend(local_top_features)

    #alias
    top_n = top_n_words

    global_top_features = sorted(score_list, key=lambda score: score[1], reverse=True)[:top_n]
    #words = [g[0] for g in global_top_features]
    #scores = [g[1] for g in global_top_features]

    return global_top_features


def lexical_diversity_stopwords(corpus):

    text_density = []
    types = 0
    tokens = 0

    #gets set of words in text
    for t in wordlists.fileids():
        text_words = wordlists.words(t)
        types += len(set(text_words))
        tokens += len(text_words)

        #removes stopwords
        filtered_words = [word for word in text_words if word not in stopwords]

        #calculates lexical diversity
        text_density.append("%.3f" % alt_lexical_diversity(filtered_words))

    #some adjusts
    text_density = [item.replace("'", "") for item in text_density]
    text_density = np.asarray(text_density).astype(np.float)

    #calculates mean and var
    mean = np.mean(text_density)
    var = np.std(text_density)

    return mean, var
