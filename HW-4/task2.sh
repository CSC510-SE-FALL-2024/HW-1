#!/bin/bash
#pipeline to perform all tasks
grep -l "sample" dataset1/* | while read file; do
    csc510_count=$(grep -o "CSC510" "$file" | wc -l)   # Count the occurrences of "CSC510" in the file

    # If the count is 3 or more, print the file name, count, and file size
    if [ "$csc510_count" -ge 3 ]; then 
        file_size=$(stat -c%s "$file")  # Get the file size in bytes
        echo "$file $csc510_count $file_size"
    fi
done | sort -k2,2nr -k3,3nr | gawk '{print "Occurrences: " $2" , File size: " $3 " bytes,  File path:" $1 }' | sed 's/file_/filtered_/' 
