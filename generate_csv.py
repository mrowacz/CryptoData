import ast
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("./logs/"):
    f.extend(filenames)

for index, l in enumerate(f):
    with open("./logs/" + l) as fm:
        print("parse " + l + " " + str(index  + 1) + "/" + str(len(f)) + "\n")
        filename = l.split(".")[0]
        with open("./csv/" + filename + ".csv", "w") as log_file:
            for e in fm.readlines():
                for index, pos in enumerate(ast.literal_eval(e)):
                    if index == 11:
                        log_file.write((str(pos) + "\n"))
                    else:
                        log_file.write(str(pos) + ",")
