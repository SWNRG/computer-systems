#!/bin/bash

./asciinemaze.py $1 > out.cast
if [ $? -eq 0 ]; then
	asciinema play out.cast
else
	echo "Cannot create ascii-cast of provided argument (filename)"
fi

