#!/bin/bash
printf "input batas bil.ganjil : "
a=1
read input

until [ ! $input -gt $a ]
do
  echo $input
  input=$((input-2))
done
