#!/bin/bash
# Author: Yiming Zhu
# Date: 2015-10-03

#gfwlist to pac
python /home/pi/projects/gfwlist2pac-master/gfwlist2pac.py >> /home/pi/projects/freess/pac.log

#publish pac
bash /home/pi/projects/freess/publish_pac.sh >> /home/pi/projects/freess/pac.log
