import readfile
import json
import pathlib


def create_both(raw_neg_dict, raw_pos_dict, path="final_dict"):
    raw_neg_dict_size = sum(raw_neg_dict.values())
    raw_pos_dict_size = sum(raw_pos_dict.values())

    freq_pos_dict = {key: (value/raw_pos_dict_size)*100 for (key, value) in raw_pos_dict.items()}
    freq_neg_dict = {key: (value / raw_neg_dict_size) * 100 for (key, value) in raw_neg_dict.items()}

    cut_off_neg = cut_off_dict(freq_neg_dict, freq_pos_dict)
    cut_off_pos = cut_off_dict(freq_pos_dict, freq_neg_dict)

    readfile.dump_into_json(path, "pos_dict_cut.json", cut_off_pos)
    readfile.dump_into_json(path, "neg_dict_cut.json", cut_off_neg)


def cut_off_dict(input_dict, compare_dict, tolerance=5):
    new_dict = {key: value for (key, value) in input_dict.items()
                if key not in compare_dict or value / compare_dict[key] > tolerance}

    return new_dict


def wrap():
    neg_dict = json.load(pathlib.Path("resources/dicts/neg/draculafirst.json").open())
    pos_dict = json.load(pathlib.Path("resources/dicts/pos/dearlittlecouple.json").open())
    create_both(neg_dict["draculafirst.xml"], pos_dict["dearlittlecouple.xml"])


wrap()
