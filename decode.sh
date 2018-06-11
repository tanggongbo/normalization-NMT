#!/bin/bash

#this file is used for decoding 
MARIAN=the-path-of-Marian

for lan in "en" "de" "hu" "ic" "se"
do
    DATADIR=your-root-directory-of-data
    MODEL_ROOT=the-directory-that-stored-your-models

    for model in "tanh-noatt" "gru-noatt" "lstm-noatt" "tanh-att" "gru-att" "lstm-att" "transformer" "bpe100" "bpe200" "bpe300" "bpe500" "bpe1000" "bpe5000"
    do
        #translating two test sets               
        MODEL_DIR=${MODEL_ROOT}/${model}
        DIR_OUT=${MODEL_DIR}/pred
        mkdir -p ${DIR_OUT}
        
        #both development set and test set
        for dir in "test" "dev" 
        do
            #both the changed spellings and unchanged spellings
            for type in "ch" "unch"
            do
                    #decode                                                                                        
                    INPUT=/the-input-path 
                    for B in 5
                    do
                        OUTPUT=/the-output-path 

                        cat $INPUT \
                        | $MARIAN/build/marian-decoder -c ${MODEL_DIR}/model.npz.best-perplexity.npz.decoder.yml \
                          -m ${MODEL_DIR}/model.npz.best-perplexity.npz --quiet-translation --device 0 \
                          --mini-batch 16 --maxi-batch 100 --maxi-batch-sort src -w 5000 --beam-size $B \
                        > $OUTPUT
                    done
                done
        done
    done
done
