#!/bin/bash

#Mendeklarasikan fungsi
panjang() {
       echo "Masukkan panjang : "
       read panjang
}
lebar() {
       echo "Masukkan lebar : "
       read lebar
       let luasbidang=$panjang*$lebar
       echo "Luas bidang :
$luasbidang"
}

#Memanggil fungsi
panjang
lebar
