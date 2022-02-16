#!/usr/bin/env python3

import sys, os, pwd, grp
import os.path

_, owner, group, dirmod, mod, *targets = sys.argv

uid = pwd.getpwnam(owner).pw_uid
gid = grp.getgrnam(group).gr_gid

dirmod =int(dirmod, base=8)
mod = int(mod, base=8)

c = 0
def progress():
	global c
	c += 1
	if c % 1000 == 0:
		print('.', end='', flush=True)
	if c % 60000 == 0:
		print()

		

for target in targets:
	print(dict(uid=uid, gid=gid, dirmod=oct(dirmod), mod=oct(mod), target=target))
	p = target
	os.lchown(p, uid, gid)
	os.lchmod(p, dirmod)	
	progress()
	for dirpath, dirnames, filenames in os.walk(target):
		for f in filenames:
			p = os.path.join(dirpath, f)
			os.lchown(p, uid, gid)
			os.lchmod(p, mod)	
			progress()
		for d in dirnames:
			p = os.path.join(dirpath, d)
			os.lchown(p, uid, gid)
			os.lchmod(p, dirmod)	
			progress()
	print()
