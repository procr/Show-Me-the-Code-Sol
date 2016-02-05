# -*- coding: utf-8 -*-
from collections import Counter
import re, os

__author__ = "rongc"

path = 'diaries'
files = os.listdir(path)
words = []

for f in files:
	with open(os.path.join(path, f)) as diary:
		words += re.findall("[a-zA-Z]+'*-*[a-zA-Z]*", diary.read())

#print words
print(Counter(words))