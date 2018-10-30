from random import shuffle
import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", default='resources/testfile.txt', help="Path of file to read from")
parser.add_argument("-o", "--outpath", default='questions.txt', help="Path of question file")
options = parser.parse_args()

with open(options.filepath, 'r', encoding='utf-8') as f:
    sentences = f.readlines()


rgx = re.compile('\s')
with open(options.outpath, 'w+', encoding='utf-8') as o:
    for x in sentences:
        arr = rgx.split(x.replace('\n', ''))
        shuffle(arr)
        o.write(' '.join(arr) + '\n')
