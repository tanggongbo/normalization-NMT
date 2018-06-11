# normalization-NMT
This repository is the code for the COLING 2018 paper "An Evaluation of Neural Machine Translation Models on Historical Spelling Normalization"

We use Marian framework (https://github.com/marian-nmt/marian-dev) to train our NMT models. 

The dataset can be found here: 
http://stp.lingfil.uu.se/histcorp/tools.html

You need to segment the token pairs into char sequences or subword units before feeding into Marian. 
We use the subword-nmt tool (https://github.com/rsennrich/subword-nmt) to learn subword units. 

