import os
import sys
import time
import datetime
import subprocess
import pynput
from pynput.keyboard import Key, Controller
screenshotsfolder = 'C:\\Program Files (x86)\\World of Warcraft\\_classic_\\Screenshots'

def activeScanner():
	initial_run_time = time.time()
	data = {}
	keyboard = Controller()
	try:
		while True:
			for file in os.listdir(screenshotsfolder):
				if file.startswith("WoWScrnShot_") and file.endswith(".jpg"):
					fndtstr =  file.replace("WoWScrnShot_",'').replace(".jpg",'')
					fndt = time.mktime(datetime.datetime.strptime(fndtstr, "%m%d%y_%H%M%S").timetuple())
					if fndt not in data.keys():
						if fndt > initial_run_time:
							data[fndt]=fndtstr
							keyboard.press(Key.f1) ###CHANGE TO YOUR SPLIT HOTKEY####
						else:
							#not from this session, ignore
							pass
					else:
						#already know about it, ignore
						pass
	except KeyboardInterrupt:
		pass
def main():
	activeScanner()
if __name__ == '__main__':
	main()








