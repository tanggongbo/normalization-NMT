#!/usr/bin/env python

#remove the "@@"
#arg1: source input file
#arg2: char_seq output file

import sys
seq=""
fin = open(sys.argv[1], 'r')
for line in fin:
  line = line.replace("@@","")
  seq = seq + line
fin.close()
fout = open(sys.argv[2], 'w')
fout.write(seq)
fout.close()
