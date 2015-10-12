#!/usr /bin/env python
# -*- coding: utf-8 -*-
# author: Yiming Zhu

import socket,fcntl,struct,os,json

json_file="/home/pi/projects/freess/shadowsocks.json"

def get_ip_address(ifname='eth0'):  
    try:  
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    
        return socket.inet_ntoa(fcntl.ioctl(  
            s.fileno(),    
            0x8915, # SIOCGIFADDR    
            struct.pack('256s', ifname[:15])    
        )[20:24])   
    except:  
        ips = os.popen("LANG=C ifconfig | grep \"inet addr\" | grep -v \"127.0.0.1\" | awk -F \":\" '{print $2}' | awk '{print $1}'").readlines()  
        if len(ips) > 0:  
            return ips[0]  
    return '' 

os.system('curl http://www.ishadowsocks.com -o ss.htm')

def dict2json(vardict):
  jsondata=json.dumps(vardict)
  fp = open(json_file, 'w')
  fp.write(jsondata)
  fp.close()

#Get hk1 server info to dict_hk1
dict_hk1 = {}
dict_hk1['server'] = os.popen('cat ss.htm|sed -n \'213p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n')
dict_hk1['server_port'] = os.popen('cat ss.htm|sed -n \'214p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n')
dict_hk1['local_address'] = get_ip_address('wlan0')
dict_hk1['local_port'] = '1080'
dict_hk1['password'] = os.popen('cat ss.htm|sed -n \'215p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n')
dict_hk1['timeout'] = '300'
dict_hk1['method'] = os.popen('cat ss.htm|sed -n \'216p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n')
dict_hk1['fast_open'] = 'false'

#Get hk2 server info to dict_hk2
dict_hk2 = {}
dict_hk2['server'] = os.popen('cat ss.htm|sed -n \'221p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n')
dict_hk2['server_port'] = os.popen('cat ss.htm|sed -n \'222p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n')
dict_hk2['local_address'] = get_ip_address('wlan0')
dict_hk2['local_port'] = '1080'
dict_hk2['password'] = os.popen('cat ss.htm|sed -n \'223p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n')
dict_hk2['timeout'] = '300' 
dict_hk2['method'] = os.popen('cat ss.htm|sed -n \'224p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n')
dict_hk2['fast_open'] = 'false'

#Get hk3 server info to dict_hk3
dict_hk3 = {}
dict_hk3['server'] = os.popen('cat ss.htm|sed -n \'229p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n')
dict_hk3['server_port'] = os.popen('cat ss.htm|sed -n \'230p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n')
dict_hk3['local_address'] = get_ip_address('wlan0')
dict_hk3['local_port'] = '1080'
dict_hk3['password'] = os.popen('cat ss.htm|sed -n \'231p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n')
dict_hk3['timeout'] = '300'
dict_hk3['method'] = os.popen('cat ss.htm|sed -n \'232p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n')
dict_hk3['fast_open'] = 'false'

status_hk2 = os.popen('cat ss.htm|sed -n \'225p\'|awk -F: \'{print $2}\'|awk -F\\" \'{print $2}\'').read().strip('\n')
status_hk3 = os.popen('cat ss.htm|sed -n \'233p\'|awk -F: \'{print $2}\'|awk -F\\" \'{print $2}\'').read().strip('\n')

print (os.popen('cat ss.htm|sed -n \'231p\'|awk -F: \'{print $2}\'|awk -F\< \'{print $1}\'').read().strip('\n'))

if (status_hk2 == 'green' and dict_hk2['password']):
  dict2json(dict_hk2)
elif (status_hk3 == 'green' and dict_hk3['password']):
  dict2json(dict_hk3)
else:
  dict2json(dict_hk1)

#os.remove("ss.htm")


