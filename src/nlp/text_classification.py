from sklearn.datasets import load_files
import pickle

def find_sentiment(txt):
    # Using our classifier
    with open('nlp/models/tfidfmodel.pickle','rb') as f:
        tfidf = pickle.load(f)
        
    with open('nlp/models/classifier.pickle','rb') as f:
        clf = pickle.load(f)
        
        
    sample = [txt]
    sample = tfidf.transform(sample).toarray()
    sentiment = clf.predict(sample)
    return sentiment