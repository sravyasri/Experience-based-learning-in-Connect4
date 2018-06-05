#!/bin/bash
counter=1
while [ $counter -le 6 ]
do
	rm -r Player1
	rm -r Player2
	python game.py
	python contemplation.py
	echo $counter
	((counter++))
done
