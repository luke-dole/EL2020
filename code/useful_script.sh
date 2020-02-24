#!/bin/bash

echo 'This script asks for a New York State phone number and tells you the location of residency.'
echo 'Please Enter a ten digit New York State phone number:'

read var1
let "arcd=${var1:0:3}"

if [ $arcd -eq 518 ]||[ $arcd -eq 838 ]
then
	X='northeastern'
fi

if [ $arcd -eq 914 ]
then
	X='Westchester County,'
fi

if [ $arcd -eq 607 ]
then
	X='south central'
fi

if [ $arcd -eq 585 ]||[ $arcd -eq 716 ]
then
	X='western'
fi

if [ $arcd -eq 315 ]||[ $arcd -eq 680 ]
then
	X='north central'
fi

if [ $arcd -eq 631 ]||[ $arcd -eq 934 ]
then
	X='Suffolk County,'
fi

if [ $arcd -eq 516 ]
then
	X='Nassau County,'
fi

if [ $arcd -eq 347 ]||[ $arcd -eq 718 ]||[ $arcd -eq 917 ]||[ $arcd -eq 929 ]
then
	X='New York City,'
fi

if [ $arcd -eq 212 ]||[ $arcd -eq 332 ]||[ $arcd -eq 646 ]||[ $arcd -eq 917 ]
then
	X='Manhattan,'
fi

echo 'You reside in' $X 'New York'


