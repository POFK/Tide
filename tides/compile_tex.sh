#!/bin/bash
name=$@
latex  $name.tex
bibtex $name.aux
latex  $name.tex
dvips  $name.dvi
ps2pdf $name.ps
