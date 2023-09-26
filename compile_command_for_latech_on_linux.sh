#!/bin/bash

# kill -15 $(pgrep firefox)
: | pdflatex -halt-on-error *.tex | grep '^!.*' -A200 --color=always
# firefox /home/xses/Desktop/Resume Wiktor Tomanek-1.pdf *.pdf &
