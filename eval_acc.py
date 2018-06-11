#!/usr/bin/env python

#evaluate the predictions, based on the reference
#arg1: predictions
#arg2: reference
#arg3: sources
#arg4: wrong predictions with references and sources

import sys

fin = open(sys.argv[1], 'r')
fref = open(sys.argv[2], 'r')
fsrc= open(sys.argv[3], 'r')
total = 0
correct = 0
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
    total += 1
    #if total == 46:
     # print("#"+str(predictions[i])+"#"+str(references[i])+"#")
    if predictions[i] == references[i]:
      correct += 1
    else:
      token_src = srcs[i].replace(" ","")
      token_pre = predictions[i].replace(" ","")
      token_ref = references[i].replace(" ","")
      fres.write(str(i)+"\t"+token_src+"\t"+token_pre+"\t"+token_ref+"\n")

#print(str(len(predictions)))
#print(str(total))
#print(str(correct))

accuracy = float(correct)/total
print(str(accuracy)+"\t"+str(correct)+"\t"+str(total))
