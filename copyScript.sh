#!/bin/sh
	for i in 1 2 3 4 5
		do
			mkdir -p assignment2/output_stats/question$1/vm${i}/before
			mkdir -p assignment2/output_stats/question$1/vm${i}/after
			scp -r -i ~/Downloads/group4.pem ubuntu@128.104.223.167:/home/ubuntu/output_stats/trial_1_question$1/disk_before assignment2/output_stats/question${1}/vm${i}/before/
			scp -r -i ~/Downloads/group4.pem ubuntu@128.104.223.167:/home/ubuntu/output_stats/trial_1_question$1/disk_after assignment2/output_stats/question${1}/vm${i}/after/
			scp -r -i ~/Downloads/group4.pem ubuntu@128.104.223.167:/home/ubuntu/output_stats/trial_1_question$1/net_before assignment2/output_stats/question${1}/vm${i}/before/
			scp -r -i ~/Downloads/group4.pem ubuntu@128.104.223.167:/home/ubuntu/output_stats/trial_1_question$1/net_after assignment2/output_stats/question${1}/vm${i}/after/
		done
			

