#!/bin/zsh
id=$(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}')
name=$(xprop -id $id | grep "WM_CLASS" | awk -F '"' '/WM_CLASS/ {print $4}')  
echo "$name"
 
