#!/bin/bash 

while [ 1 ]; do 
	python getHarimMenuPDF.py 
	python3.5 image_menu_convert.py
	python3.5 kakao_vision_convert.py
	sleep 3600
done
