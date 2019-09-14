import analyse


def test(sent_path):
    num_pos = 0
    correct = 0
    with open(sent_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    total = len(lines)
    for line in lines:
        sentence = line.split("#")[0]
        validation = line.split("#")[1]
        analysis = analyse.analyse_sent(sentence)
        if int(validation) == analysis:
            correct += 1
        if int(validation) == 1:
            num_pos += 1
        print("sentence: " + sentence)
        print("validation: " + validation)
        print("analysis: " + str(analysis))

        print("BREAK")

    acc_percentage = round(correct/total * 100, 2)
    print("Final ACC: " + str(acc_percentage))
    print("num_pos: " + str(num_pos) + " out of " + str(total))

test("resources/testdata/sentiment_saetze.txt")
