#!/bin/bash
c=1
while [ $c -le 5 ]
do
	echo "NEW ROUND" >> ENDRESULTFREQUENT
	rm -r contemplation.db
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
	((c++))
done
python AverageResults.py
