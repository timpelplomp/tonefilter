import json
from textblob import TextBlob
from pathlib import Path
# import nltk
# nltk.download('averaged_perceptron_tagger')


def analyse_sent(sentence, pos_fp="final_dict/pos_dict_cut.json", neg_fp="final_dict/neg_dict_cut.json"):
    pos_dict = json.load(Path(pos_fp).open())
    neg_dict = json.load(Path(neg_fp).open())
    lemma_sent = lemmatise(sentence)
    final_score = 0
    for lemma in lemma_sent:
        if lemma in pos_dict:
            final_score += 1
        elif lemma in neg_dict:
            final_score -= 1
    if final_score > 1:
        return 1
    # elif final_score == 0:
    #     return 0
    else:
        return 0


# https://www.machinelearningplus.com/nlp/lemmatization-examples-python/
def lemmatise(sentence):
    sent = TextBlob(sentence)
    tag_dict = {"J": 'a',
                "N": 'n',
                "V": 'v',
                "R": 'r'}
    words_and_tags = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]
    lemmatized_list = [wd.lemmatize(tag) for wd, tag in words_and_tags]
    return lemmatized_list

