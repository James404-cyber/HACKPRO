import platform
import os
try:os.system("xdg-open https://youtube.com/@Mr.James404")
except:pass	
try:os.system("clear")
except:pass	
os.system('termux-setup-storage')
os.system('pkg install wget')
os.system('git pull')
try:os.system('touch /sdcard/james.txt')
except:pass
try:os.system('touch .proxy.txt')
except:pass
try:os.mkdir('/sdcard/OK')
except:pass
try:os.mkdir('/sdcard/CP')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("latter")._site_view_()
elif 'aarch' in arc:
	__import__("Ulib1").ninex()
else:
	exit(f' Unknow device machine {arc}')


	

	

















