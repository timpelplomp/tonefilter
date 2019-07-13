# planning to tag all
import os
from stanfordcorenlp import StanfordCoreNLP

# need to set the java environment first
# os.environ["JAVAHOME"] = "E:/Coding/jdks/jdk-12.0.1/bin/java.exe"


def core_all(input_dir, output_dir, memory="8g"):
    # set path to corenlp here
    corenlp_path = "D:/to keep/Tools/Stanford/stanford-corenlp-full-2018-10-05"
    # adjust parameters to your liking, it is called for each annotation
    properties = {'annotators': 'tokenize,ssplit,pos,lemma', 'pipelineLanguage': 'en', 'outputFormat': 'xml'}
    # the full server is started (negligible impact if inputs are large enough)
    with StanfordCoreNLP(corenlp_path, memory=memory) as corenlp:

        for input_file in os.listdir(input_dir):
            basename = os.path.basename(input_file)
            output_file_path = os.path.join(output_dir, basename)

            with open(input_file, "r", encoding="utf-8") as i:
                input_text = i.read()

            output_xml = corenlp.annotate(input_text, properties=properties)

            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(output_xml)
