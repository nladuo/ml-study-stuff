#! /bin/bash
#Desc: This Script Download the Stocks Data to the "./data" directory.
wget https://dl.dropboxusercontent.com/u/299169754/ml4t.zip
unzip ml4t.zip
mv ml4t/data ./
rm -rf ml4t*
