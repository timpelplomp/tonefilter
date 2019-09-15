from core_all import core_all
import dict_comparison
import dictionary_creation


def wrap():
    # example
    input_dir_pos = "resources/txt_in/pos"
    output_dir_pos = "resources/tagged_in/pos"
    # input_dir_neg = "resources/txt_in/neg"
    # output_dir_neg = "resources/tagged_in/neg"
    # starts programme
    core_all(input_dir_pos, output_dir_pos)
    in_pos_dir = "resources/tagged_in/pos"
    out_pos_dir = "resources/dicts/pos"
    dictionary_creation.create_lemma_dict(in_pos_dir, out_pos_dir)


    dict_comparison.wrap()
