import platform
import os
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('touch .prox.txt')
except:pass
try:os.system('touch .proxy.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("latter")._site_view_()
elif 'aarch' in arc:
	__import__("Loppp").minex()
else:
	exit(f' Unknow device machine {arc}')
