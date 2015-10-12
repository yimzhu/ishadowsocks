#!/bin/bash
# Author: Yiming Zhu
# Date: 2015-10-03
# Program: Check if PAC file should be updated.

lastmod='/usr/share/nginx/www/autoproxy.pac'
currentmod='/home/pi/projects/gfwlist2pac-master/autoproxy.pac'
log='/home/pi/projects/freess/pac.log'

# Compare if new generated pac file is same as the old one. Same return null, different return 2 
compareresult=$(grep -vxFf $lastmod $currentmod)

if [ -z $currentmod ] ;then
  echo "$(date '+%x  %X')""  ""ERROR: PAC updating interrupted." >>$log
else
  if [ -z "$compareresult" ] ;then
    echo "$(date '+%x  %X')""  ""INFO: PAC is up to date. No update available." >> $log
  else 
    sudo cp -r $currentmod $lastmod 
    echo "$(date '+%x  %X')""  ""INFO: PAC has been updated." >>$log
  fi
fi
