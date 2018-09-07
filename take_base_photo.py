import cmd
import camera
import time

def timestamp():
	t = time.localtime()
	stamp = '%d-%02d-%02d-%02d%02d%02d' % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
	return stamp

args = cmd.readArguments()

if  args['name'] == 'TIME':
	camera.takePhoto(timestamp())
if  args['name'] == 'empty':
	camera.takePhoto('empty')