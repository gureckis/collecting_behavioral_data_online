from paramiko import SSHClient
from scp import SCPClient
import os, sys
from config import *

manifest = ['index.html',
			'syllabus.html',
			'lecture1.html',
			'lecture2.html',
			'lecture3.html',
			'lecture4.html',
			'slides.html',
			'lectures',
			'images',
			'build_site.py',
			'LICENSE',
			'README.md',		
			'css',
			'js',
			'fonts']

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(HOST,username=USERNAME,password=PASSWORD)

# SCPCLient takes a paramiko transport as its only argument
scp = SCPClient(ssh.get_transport())

print manifest
for item in manifest:
	if item is not 'config.py':
		scp.put(item, BASEPATH, recursive=True)
