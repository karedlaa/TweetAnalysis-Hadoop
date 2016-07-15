#!/bin/bash
output="/user/bollara/ng_output1"
echo "$output"
hadoop fs -rmr $output
hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/1gram/ -output $output -mapper map_ng.py -reducer red_ng.py -file *.py &
hadoop fs -get $output .
