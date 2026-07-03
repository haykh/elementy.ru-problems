#!/bin/sh

palette="/tmp/palette.png"
filters="fps=15,scale=720:-1:flags=lanczos"

ffmpeg -v warning -i anim-%06d.png -vf "$filters,palettegen" -y $palette
ffmpeg -v warning -i anim-%06d.png -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y $1

# ffmpeg -v warning -i anim-%06d.png -i $palette -filter_complex "[0:v][1:v] paletteuse" anim.gif
