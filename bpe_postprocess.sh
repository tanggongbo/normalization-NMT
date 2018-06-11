#!/bin/bash

#post-processing: bpe output-->char sequence

for lan in "en" "de" "hu" "ic" "se"
do
    for model in "bpe100" "bpe200" "bpe300" "bpe500" "bpe1000" "bpe5000" 
    do
        #both the development and test set
        for dir in "dev" "test"
        do
            #both the changed spellings and unchanged spellings
            for type in "ch" "unch"
            do
                for B in 5
                do
                    OUTPUT=your-bpe-output-fie
                    python3 editbpe.py ${OUTPUT} ${OUTPUT}.tkn
                    python3 token2char.py ${OUTPUT}.tkn ${OUTPUT}.seq
                done
            done
        done
    done
done
