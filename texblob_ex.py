from textblob import TextBlob


def test_blob(sentence):
    blob = TextBlob(sentence)

    polarity = blob.sentiment_assessments.polarity
    if polarity < 0:
        return 0
    elif polarity > 0:
        return 1
    else:
        return -1
