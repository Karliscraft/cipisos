#!/bin/bash

wmctrl -r 'bot1' -t 1
wmctrl -r 'bot1' -e 0,0,0,640,400
wmctrl -r 'bot2' -t 1
wmctrl -r 'bot2' -e 0,0,400,640,400
wmctrl -r 'bot3' 1
wmctrl -r 'bot3 -e 0,640,0,640,400
wmctrl -r 'bot4 -t 1
wmctrl -r 'bot4' -e 0,640,400,640,400
wmctrl -x -r 'Chromium' -t 2
wmctrl -x -r 'Chromium' -s add,maximized_vert,maximized_horz
