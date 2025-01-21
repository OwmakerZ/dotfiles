# !/bin/zsh
# random select a file from ~/Wallpapers

dir=$HOME/Wallpapers
random_file=$(ls $dir | shuf -n 1)

feh --bg-scale $dir/$random_file
