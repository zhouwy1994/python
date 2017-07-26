#!/bin/bash

var="Helo World Hello World"

#echo $var
#echo ${var[1]}

#printf "%s" var
for i in $var
do
	printf "%s\n" $i
done
