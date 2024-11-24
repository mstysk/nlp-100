def getSentences():
    sentences = []
    with open("./neko.txt.mecab", "r") as f:
        for line in f:
            l1 = line.split("\t")
            if len(l1) == 2:
                l2 = l1[1].split(",")
                if l2[0] != "記号":
                    surface = l1[0]
                    base = l2[6]
                    pos = l2[0]
                    pos1 = l2[1]
                    sentences.append({"surface": surface, "base": base, "pos": pos, "pos1": pos1})
    return sentences


