#!/usr/bin/env python

#split the tokens into character sequence
#arg1: source input file
#arg2: char_seq output file

import sys
import re

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')
for line in fin:
  tokens = list(line.strip())
  seq = " ".join(tokens)
  seq = re.sub(r" +", " ", seq)
  seq = seq + "\n"
  fout.write(seq)

fin.close()
fout.close()
