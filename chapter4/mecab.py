import MeCab

filename = "./neko.txt"
outputFilename = "./neko.txt.mecab"
file = open(filename, "r")
output = open(outputFilename, "w")

wakati = MeCab.Tagger()

for line in file:
    parsed = wakati.parse(line)
    output.write(parsed)

file.close()
output.close()
