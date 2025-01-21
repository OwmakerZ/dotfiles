#!/bin/zsh
i3status -c .config/i3status/i3status.conf | while :
do
    read line
    id=$(xprop -root | awk '/_NET_ACTIVE_WINDOW\(WINDOW\)/{print $NF}')
    name=$(xprop -id $id | grep "WM_CLASS" | awk -F '"' '/WM_CLASS/ {print $4}')  
    echo "$name | $line" || exit 1
done
