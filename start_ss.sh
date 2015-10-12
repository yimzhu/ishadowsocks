#!/bin/bash
# Author: Yiming Zhu
# Date: 2015-9-27
# Program: Launch SS and Use delegated to enable Socket2HTTP proxy

#Change if network changed
proxy='192.168.1.123:1080'

#Change if this program deployed to somewhere
working_path='/home/pi/projects/freess/'
shadowsocks_conf='/home/pi/projects/freess/shadowsocks.json'
server_log='/home/pi/projects/freess/server.log'
start_log='/home/pi/projects/freess/start.log'

#Find started pid
sslocal_pid=$(ps -A|grep sslocal|wc -l)
delegated_pid=$(ps aux|grep delegated|grep -v grep|wc -l)

# or delegated_pid=$(ps aux|grep [d]elegated|wc -l)

function launchssserver()
{
  cd $working_path
  rm -rf start.log server.log
  python gen_ssjson.py
  cd -
}

if [ "1" == "$sslocal_pid" ];then
  sudo kill -9 $(ps -A|awk /sslocal/'{print $1}')
  launchssserver
  nohup /usr/local/bin/sslocal -c $shadowsocks_conf > $server_log 2>&1 &
  echo "$(date '+%x  %X')""  ""INFO: Shadowsocks server restarted!" >> $start_log
elif [ "0" == "$sslocal_pid" ];then
  launchssserver
  nohup /usr/local/bin/sslocal -c $shadowsocks_conf > $server_log 2>&1 &
  echo "$(date '+%x  %X')""  ""INFO: Shadowsocks server started!" >> $start_log
else
  echo "$(date '+%x  %X')""  ""ERROR: Multiple shadowsocks PIDs detected, please check!!!" >> $start_log
fi

if [ "1" == "$delegated_pid" ];then
  echo "$(date '+%x  %X')""  ""WARN: Delegated server has already started!" >> $start_log
elif [ "0" == "$delegated_pid" ];then
  /home/pi/softwares/delegate9.9.13/src/delegated -P8118 SERVER=http SOCKS=$proxy
  echo "$(date '+%x  %X')""  ""INFO: Delegated server started!" >> $start_log
else
  echo "$(date '+%x  %X')""  ""ERROR: Multiple delegated PIDs detected, please check!!!" >> $start_log
fi
