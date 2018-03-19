#!/bin/sh

xfce4-terminal -e "node ~/BotFolder/Automatic/bot.js" &
xfce4-terminal -e "node ~/BotFolder/'Schubi Automatic'/automatic.js" &
xfce4-terminal -e "node ~/BotFolder/'Schubi Bot'/bot.js" &
xfce4-terminal -e "node ~/BotFolder/'current bot'/bot.js" &
sleep 5
ratpoison -c vsplit
ratpoison -c hsplit
ratpoison -c focusright
ratpoison -c hsplit
rpws 2
firefox &
