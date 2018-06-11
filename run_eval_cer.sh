#!/bin/bash

# evaluate the predictions of changed and unchanged set 

for LAN in "en" "de" "hu" "ic" "se"
do

  for mod in "tanh-noatt" "gru-noatt" "lstm-noatt" "tanh-att" "gru-att" "lstm-att" "transformer" "bpe100" "bpe200" "bpe300" "bpe500" "bpe1000" "bpe5000"
  do
    echo "===================="
    echo $LAN----$mod
    echo "===================="
    for dir in "test" "dev"
    do
      echo "------"+${dir}+"--------"      
      for tp in "ch" "unch"
      do
        echo "------"+${tp}+"--------"
        for beam in 5
        do
          python3 eval_cer.py your-prediction-file reference-file source-file cer-error-output-file
        done
      done
    done
  done

done
