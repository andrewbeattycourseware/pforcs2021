# demonstrate reading hamlet
# Author: Andrew Beatty

filename = 'shakespeare-hamlet-25.txt'
path = '../data/'

outputFile = "linesToLearn.txt"

player = 'MARCELLUS'

isPlayerLine= False
with open (path+filename, 'rt') as f:
    with open (path+outputFile, 'wt') as out:
        for line in f.readlines():
            if line.startswith(player):
                isPlayerLine = True
                out.write(line)
            elif line.startswith('\t') and isPlayerLine:
                out.write(line)
            else:
                isPlayerLine= False

