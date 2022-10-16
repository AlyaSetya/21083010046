#!/bin/bash

printf "Input nama mahasiswa : "
read nama

printf "Input IPS Mahasiswa : "
read n

declare -a arrayIPSMahasiswa

i=0
let jumlah=$n-1

while [ $i -le $jumlah ];
do
   let nilai=$i+1
   printf " " $nilai;
   read nilaismt;
   arrayIPSMahasiswa[$i]=$nilaismt;
   let total=total+$nilaismt;
   let i=$i+1;
done

let IPK=$total / $n
echo "IPK Mahasiswa = " $total
echo "IPK Mahasiswa = " $IPK
