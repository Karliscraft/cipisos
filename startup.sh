#!/bin/bash

rpws init 2
#SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
ratpoison -c "addhook newwindow exec ${0} urxvt1"
urxvt -e "sh" &
if [ "$1" == "urxvt1" ]; then
	ratpoison -c "remhook newwindow $(ratpoison -c "listhook newwindow")"
	ratpoison -c "addhook newwindow exec ${0} urxvt2"
	urxvt -e "sh" &
elif [ "$1" == "urxvt2" ]; then
	ratpoison -c "remhook newwindow $(ratpoison -c "listhook newwindow")"
	ratpoison -c vsplit
	rpws 2
	ratpoison -c "addhook newwindow exec rpws 1"
	firefox &
	./panel.sh | lemonbar -p | sh
fi
