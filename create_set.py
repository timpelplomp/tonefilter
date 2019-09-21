from textblob import TextBlob
import json
import readfile


def freq_all():
    with open("resources/txt_in/neg/draculafirst.txt", "r", encoding="utf-8") as d:
        drac_raw = d.read()
    with open ("resources/txt_in/pos/dearlittlecouple.txt", "r", encoding="utf-8") as p:
        pos_raw = p.read()

    both_raw = drac_raw + pos_raw
    blob = TextBlob(both_raw)
    id_dict = {}
    id = 0
    for token in blob.words:
        if token not in id_dict:
            id_dict[token] = id
            id += 1
    return id_dict


readfile.dump_into_json("id_dict/", "id_dict.json", freq_all())
