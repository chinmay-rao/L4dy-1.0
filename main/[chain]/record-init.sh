#!/bin/sh

arecord -D plughw:1,0 -d 5 -t raw -c 1 -r 16000 -f S16_LE | python stdin_mod.py 
