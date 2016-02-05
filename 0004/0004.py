# -*- coding: utf-8 -*-
from collections import Counter
import re
from compiler.ast import flatten

__author__ = "rongc"

with open(r"text.txt") as f:

    file_words = flatten([re.findall("[a-zA-Z]+'*-*[a-zA-Z]*", line) for line in f])

#print file_words
print(Counter(file_words))