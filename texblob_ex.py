from textblob import TextBlob
from textblob.en.sentiments import NaiveBayesAnalyzer


def test_blob(sentence):
    blob = TextBlob(sentence)

    polarity = blob.sentiment_assessments.polarity
    if polarity < 0:
        return 0
    elif polarity > 0:
        return 1
    else:
        return -1


def test_blob_bayes(sentence):
    classification = NaiveBayesAnalyzer.analyze(NaiveBayesAnalyzer(), sentence).classification
    if classification == "pos":
        return 1
    elif classification == "neg":
        return 0
    else:
        return -1
