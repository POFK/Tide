#!/bin/bash
#git clone https://github.com/POFK/test.git
git add .
git commit -m date `'+%Y/%m/%d %H:%M:%S'`
#git commit -a 
git push origin master
