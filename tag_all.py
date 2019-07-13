# planning to tag all
import os
from stanfordcorenlp import StanfordCoreNLP

# need to set the java environment first
# os.environ["JAVAHOME"] = "E:/Coding/jdks/jdk-12.0.1/bin/java.exe"

sentence = "I dislike the oracle java standard."
corenlp_path = "D:/to keep/Tools/Stanford/stanford-corenlp-full-2018-10-05"
properties = {'annotators': 'tokenize,ssplit,pos,lemma', 'pipelineLanguage': 'en', 'outputFormat': 'xml'}
with StanfordCoreNLP(corenlp_path, memory='8g',) as corenlp:

    print(corenlp.annotate(sentence, properties=properties))
