from textblob import TextBlob
import json
import readfile


def blob_it(what_to):
    if what_to is "drac":
        with open("resources/txt_in/neg/draculafirst.txt", "r", encoding="utf-8") as d:
            drac_raw = d.read()
            return TextBlob(drac_raw)
    elif what_to is "pos":
        with open("resources/txt_in/pos/dearlittlecouple.txt", "r", encoding="utf-8") as p:
            pos_raw = p.read()
            return TextBlob(pos_raw)


def freq_all():
    with open("resources/txt_in/neg/draculafirst.txt", "r", encoding="utf-8") as d:
        drac_raw = d.read()
    with open ("resources/txt_in/pos/dearlittlecouple.txt", "r", encoding="utf-8") as p:
        pos_raw = p.read()

    both_raw = drac_raw + pos_raw
    blob = TextBlob(both_raw)
    id_dict = {}
    id = 1
    for token in blob.words:
        if token not in id_dict:
            id_dict[token] = id
            id += 1
    return id_dict


def encode_text(blob, flag):
    with open("id_dict/id_dict.json", "r", encoding="utf-8") as f:
        encode_dict = json.load(f)
    encoded_sents = []
    for sentence in blob.sentences:
        subset = []
        for word in sentence.words:
            if word in encode_dict:
                subset.append(encode_dict[word])
            else:
                subset.append(0)

            encoded_sents.append(subset)

    print(encoded_sents)


readfile.dump_into_json("id_dict", "id_dict.json", freq_all())
# encode_text(blob_it("drac"), 1)
