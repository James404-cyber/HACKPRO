#coding=utf-8
import os,sys,subprocess
device_arch=subprocess.check_output('uname -m',shell=True)
if 'aarch64' in str(device_arch):
    os.system('chmod 777 Prohack && ./Prohack')

