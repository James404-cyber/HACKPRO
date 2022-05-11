import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Prohack")._site_ope_()
elif 'aarch' in arc:
	__import__("Prohack64")._site_ope_()
else:
	exit(f' Unknow device machine {arc}')
