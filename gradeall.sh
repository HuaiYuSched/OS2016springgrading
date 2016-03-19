#!/bin/bash

LAB=lab1

for i in *; do
    if [[ ! -d $i ]]; then
	continue
    fi

    pushd $i/labcodes/$LAB > /dev/null
    score_line=`make grade 2>/dev/null | grep "Total Score" | egrep -o "[0-9]+/[0-9]+"`
    score=${score_line%/*}
    max_score=${score_line#*/}
    echo $i $score
    popd > /dev/null
done
