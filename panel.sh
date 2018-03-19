#!/bin/bash

COLOR1="-"
COLOR2="-"
while true; do
if [ "$(rpws current)" == "1" ]; then
	COLOR1="#888888"
elif [ "$(rpws current)" == "2" ]; then
	COLOR2="#888888"
fi
echo "%{l}%{B${COLOR1}}%{A:rpws 1:}terminals%{A}%{B-} %{B${COLOR2}}%{A:rpws 2:}firefox%{A}%{B-}%{c}$(date)%{r}%{A:sudo reboot:}restart%{A} %{A:sudo poweroff:}shutdown%{A}"
COLOR1="-"
COLOR2="-"
done
