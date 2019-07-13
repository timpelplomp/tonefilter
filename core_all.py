# planning to tag all
from stanfordcorenlp import StanfordCoreNLP
from pathlib import Path
# need to set the java environment first
# os.environ["JAVAHOME"] = "E:/Coding/jdks/jdk-12.0.1/bin/java.exe"
#  java -mx16g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 25000 -MaxCharLength
#  100000000000
# from commandline to have a server at localhost


def core_all(input_dir, output_dir, memory="8g"):
    # set path to corenlp here
    corenlp_path = "D:/to keep/Tools/Stanford/stanford-corenlp-full-2018-10-05"
    # adjust parameters to your liking, it is called for each annotation
    properties = {'annotators': 'tokenize,ssplit,pos,lemma', 'pipelineLanguage': 'en', 'outputFormat': 'xml'}
    # the full server is started (negligible impact if inputs are large enough)

    # I hate having to do this, maybe we should switch to a different wrapper or roll our own
    # with StanfordCoreNLP(corenlp_path, memory=memory) as corenlp:
    with StanfordCoreNLP('http://localhost', port=9000) as corenlp:
        for input_file in Path(input_dir).glob("*.txt"):
            basename = input_file.stem
            print("looking at: " + str(basename))
            # should work on this
            output_file_path = Path(output_dir).joinpath(basename + ".xml")

            with input_file.open(mode="r", encoding="utf-8") as i:
                input_text = i.read()

            output_xml = corenlp.annotate(input_text, properties=properties)

            with output_file_path.open(mode="w", encoding="utf-8") as f:
                f.write(output_xml)
