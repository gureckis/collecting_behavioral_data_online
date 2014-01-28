from jinja2 import Environment, FileSystemLoader
import os, sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import argparse

from config import *

env = Environment(loader=FileSystemLoader(TEMPLATES_FOLDER))
all_templates = os.listdir(TEMPLATES_FOLDER)


class MyHandler(FileSystemEventHandler):
	def on_modified(self, event):
		#self.write_template()
		file_changed = os.path.basename(event.src_path)
		if file_changed not in exclude_list:
			print file_changed + " changed"
			self.write_template(file_changed)
		else:
			# recuilt all files
			for fn in all_templates:
				if fn not in EXCLUDE_LIST: # don't need to rebuild excludes
					print fn + " changed"
					self.write_template(fn)

	# write parsed template to current folder
	def write_template(self, fn):
		template = env.get_template(fn)
		parsed_template = template.render()
		with open(fn, 'wb') as fh:
			fh.write(parsed_template)
		fh.close()

def print_hi():
	print "hi"

if __name__ == "__main__":
	print "monitoring files for changes"
	event_handler = MyHandler()
	observer = Observer()
	observer.schedule(event_handler, path='templates', recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()
	# templates = ['index.html', 'lecture1.html']
	# map(write_template, templates)