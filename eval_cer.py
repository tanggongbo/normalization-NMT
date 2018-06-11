#!/usr/bin/env python

#use character error rate to evaluate the predictions, based on the reference
#arg1: predictions
#arg2: reference
#arg3: sources
#arg4: wrong predictions with references and sources, and edit distance

import sys
import Levenshtein
import re

fin = open(sys.argv[1], 'r')
fref = open(sys.argv[2], 'r')
fsrc= open(sys.argv[3], 'r')
total_char = 0
incorrect_char = 0
incorrect = 0
predictions = []
references = []
srcs = []

for line in fin:
  line = line.lower().strip()
  if line != "":
    predictions.append(line)
fin.close()

for line1 in fref:
  line1 = line1.lower().strip()
  if line1 != "":
    references.append(line1)
fref.close()

for line1 in fsrc:
  line1 = line1.lower().strip()
  if line1 != "":
    srcs.append(line1)
fsrc.close()

fres=open(sys.argv[4],'w')
for i in range (len(predictions)):
  if predictions[i] != "":
    #total += 1
    predictions[i] = re.sub(r" ", "", predictions[i])
    references[i] = re.sub(r" ", "", references[i])
    if predictions[i] == references[i]:
      total_char += len(references[i])
    else:
      total_char += len(references[i])
      ed = Levenshtein.distance(predictions[i], references[i])
      incorrect_char += ed
      incorrect += 1
      token_src = srcs[i].replace(" ","")
      token_pre = predictions[i].replace(" ","")
      token_ref = references[i].replace(" ","")
      fres.write(str(i)+"\t"+token_src+"\t"+token_pre+"\t"+token_ref+"\t"+str(ed)+"\n")

aver_ed = float(incorrect_char)/incorrect
fres.write("average edit distance: "+str(aver_ed))


print(incorrect_char)
print(total_char)
