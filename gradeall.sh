#!/bin/bash

WORKDIR=`pwd`
SUMMARY="$WORKDIR/summary.txt"
LOG="$WORKDIR/log.txt"
LAB='lab1'
GRADESH='$WORKDIR/lab1grade.sh'

function summary() {
    echo $1 >> $SUMMARY
}

function log() {
    echo $1 >> $LOG
}

score=0
max_score=0
total_score=0
graded_repo=''

function grade() {
    git pull -f 
    cp $GRADESH tools/grade.sh
    score_line=`make grade 2>/dev/null | grep "Total Score" | egrep -o "[0-9]+/[0-9]+"`
    log "score_line: $score_line"
    make clean
    if [[ -z "$score_line" ]]; then
	    score=0
    else
	score=${score_line%/*}
	total_score=${score_line#*/}
	if [[ $score -gt $max_score ]]; then
	    max_score=$score
	    graded_repo=`pwd | sed "s#$WORKDIR/##g"`
	fi
    fi
}

for stu_dir in *; do
    if [[ ! -d $stu_dir ]]; then
	continue
    fi
    log "Check $stu_dir"

    # For each dir containing repos, we consider the following cases.
    # 1) One may have multiple *ucore_lab* repos
    # 2) One may reorganize the dir layout
    pushd $stu_dir > /dev/null 2>>$LOG
    max_score=-1
    graded_repo=''
    for repo_dir in *; do
	if [[ ! -d $repo_dir ]]; then
	    continue
	fi

	log "Entering $stu_dir/$repo_dir"
	# Guess if $repo_dir is a ucore_lab repo
	if find -L $repo_dir -name $LAB -type d | grep -q $LAB 2>>$LOG; then
	    pushd $repo_dir > /dev/null 2>>$LOG

	    if [[ -d labcodes/$LAB ]] && [[ -f labcodes/$LAB/Makefile ]] && [[ -d labcodes/$LAB/kern ]]; then
		# case 1: standard ucore_lab
		pushd labcodes/$LAB > /dev/null 2>>$LOG
		grade
		popd > /dev/null 2>>$LOG
	    else
		# case 2: customized layout, try all potential dirs
		candidates=`find -L . -name $LAB -type d`
		for candidate_dir in $candidates; do
		    if [[ -f $candidate_dir/Makefile ]] && [[ -d $candidate_dir/kern ]]; then
			log "Grade potential lab dir: $candidate_dir"
			pushd $candidate_dir > /dev/null 2>>$LOG
			grade
			popd > /dev/null 2>>$LOG
		    fi
		done
	    fi

	    popd > /dev/null 2>>$LOG
	else if [[ -f $repo_dir/Makefile ]] && [[ -f $repo_dir/tools/grade.sh ]];then
	    pushd $repo_dir >/dev/null 2>>$LOG
	    grade
	    popd >/dev/null 2>>$LOG
	fi
	    log "Unknown repo: $repo_dir"
	fi
    done

    if [[ $max_score -eq -1 ]] || [[ -z "$graded_repo" ]]; then
	log "No valid ucore_lab repo found under $stu_dir"
    else
	summary "$stu_dir $graded_repo $max_score/$total_score"
    fi

    popd > /dev/null 2>>$LOG
done
