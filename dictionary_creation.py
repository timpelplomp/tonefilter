import counter
from readfile import *
from pathlib import Path

# # all
# lemma_core_nlp_dict = counter.count_files_in_dir("F:/Studium/resources/out_corpusexample-ling1/corenlp",
#                                                  x_path=".//lemma")
#
# lemma_count_dict = {}
# for key in lemma_core_nlp_dict.keys():
#     lemma_count_dict[key] = len(lemma_core_nlp_dict[key])
# print(lemma_count_dict)


def create_lemma_dict(xml_source_dir, output_path):
    for xml_file in Path(xml_source_dir).glob("*.xml"):
        string_path = str(xml_file.resolve())
        print(string_path)
        lemma_core_nlp_dict = counter.count_files_in_dir(xml_source_dir,
                                                         x_path=".//lemma")
        print(lemma_core_nlp_dict)
        dump_into_json(Path(output_path), xml_file.stem + ".json", lemma_core_nlp_dict)
        dump_into_csv(output_path, xml_file.stem + ".csv", lemma_core_nlp_dict)


# quick example

