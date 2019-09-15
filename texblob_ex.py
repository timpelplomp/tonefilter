from textblob import TextBlob
from textblob.en.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier


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


def test_naives_bayes_classifier_own(sentence):
    train_tuples = read_sent_to_list()
    classifier = NaiveBayesClassifier(train_tuples)
    return classifier.classify(sentence)


def read_sent_to_list(limit=50):
    tuple_list = []

    with open("resources/testdata/sentiment_saetze.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        sentence = line.split("#")[0]
        classification = int(line.split("#")[1])
        tuple_list.append([sentence, classification])

    return tuple_list[:limit]
