from random import shuffle
import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", default='resources/testfile.txt', help="Path of file to read from")
options = parser.parse_args()

with open(options.filepath, 'r', encoding='utf-8') as f:
    sentences = f.readlines()

rgx = re.compile('\s')
for x in sentences:
    arr = rgx.split(x.replace('\n', ''))
    shuffle(arr)
    print(arr)

