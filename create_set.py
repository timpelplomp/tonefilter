from textblob import TextBlob
import json
import readfile
import random


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


def encode_text(blob, flag, until):
    with open("id_dict/id_dict.json", "r", encoding="utf-8") as f:
        encode_dict = json.load(f)

    encoded_sents = []
    for sentence in blob.sentences[:until]:
        subset = []
        for word in sentence.words:
            if word in encode_dict:
                subset.append(encode_dict[word])
            else:
                subset.append(0)

        encoded_sents.append([subset, flag])
    return encoded_sents


def shuffle_save_all(encoded_lists, path_ef="total_train_sets"):
    random.shuffle(encoded_lists)

    enc_sents = []
    cl_sents = []
    for sublist in encoded_lists:
        enc_sents.append(sublist[0])
        cl_sents.append(sublist[1])

    readfile.dump_into_json(path_ef, "enc_sents.json", enc_sents)
    readfile.dump_into_json(path_ef, "cl_sents.json", cl_sents)


def get_both_corp():
    drac_blob = blob_it("drac")
    pos_blob = blob_it("pos")

    max_len_possible = min(len(drac_blob.sentences), len(pos_blob.sentences))
    combined_list = encode_text(drac_blob, 0, max_len_possible) + encode_text(pos_blob, 1, max_len_possible)

    shuffle_save_all(combined_list)


def create_test_set():
    with open("resources/testdata/sentiment_saetze.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open("id_dict/id_dict.json", "r", encoding="utf-8") as f:
        encode_dict = json.load(f)

    enc_list = []

    for line in lines:
        split_line = line.split("#")
        sent_blob = TextBlob(split_line[0])
        flag = int(split_line[1])

        sublist = []
        for word in sent_blob.words:
            if word in encode_dict:
                sublist.append(encode_dict[word])
            else:
                sublist.append(0)
        enc_list.append([sublist, flag])

    shuffle_save_all(enc_list, "resources/testdata")

# readfile.dump_into_json("id_dict", "id_dict.json", freq_all())
# encode_text(blob_it("drac"), 1)
# get_both_corp()

create_test_set()
