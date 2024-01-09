
import platform
import os

try:
	import pyzipper
except ModuleNotFoundError:
	print("pyzipper is not installed. Installing...")
	os.system('pip install pyzipper')

# Continue with the rest of your script
os.system('pkg install wget')
os.system('pkg install cmatrix')
os.system('git pull')

try:
	os.system('touch /sdcard/james.txt')
except:
	pass

try:
	os.system('touch .proxy.txt')
except:
	pass

try:
	os.mkdir('/sdcard/OK')
except:
	pass

try:
	os.mkdir('/sdcard/CP')
except:
	pass

arc = str(platform.uname().machine)

if 'arm' in arc:
	__import__("latter")._site_view_()
elif 'aarch' in arc:
	__import__("Ulibv").ninex()
else:
	exit(f' Unknown device machine {arc}')
