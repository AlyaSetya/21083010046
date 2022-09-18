printf "Harga photocard Bangtan = "

read hargaPC

if [ $hargaPC > 1000000 ]
then
 echo "Harga PC nya sangat mahal jangan dibeliii"
elif [ $hargaPC < 1000000 ]
then
 echo "Harga ramah di kantong tapi jangan boros"
else
 echo "Harga on budget tapi pikir-[ikir lagi yaaa"
fi
