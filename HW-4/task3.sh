#!/bin/bash

awk -F"," '$3=="2" && $NF ~ /S/' titanic.csv | sed 's/female/F/g; s/male/M/g' | awk -F"," 'BEGIN {sum=0; count=0} { if($7 != "") {sum += $7; count += 1} } END { if (count > 0) print "Average Age is = " sum / count} {print $0}'