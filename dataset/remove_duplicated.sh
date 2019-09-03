#!/bin/bash

DIR=$1

function remove_duplicated() {
	local file="$1"
	diff "$file" "$file.~1~"
	if [ $? -eq 0 ]; then
		rm "$file.~1~"
	fi
}

while read -r file; do
	remove_duplicated "$DIR/$file"
done
