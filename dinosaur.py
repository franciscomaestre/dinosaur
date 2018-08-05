import time
import cv2
import pyautogui

from classes import ScreenRegion
from functions import *

RED = (0, 0, 255)
BLUE = (255, 0, 0)

if __name__ == "__main__":

	#Initial Timer
	for i in range(2):
		time.sleep(1)
		print 2-i

	print 'Go!!!!!'

	while True:

		#We get the mouse position
		left, top = pyautogui.position()

		#Array of regions to check for Jump
		regions_list = []
		regions_list.append(ScreenRegion(top=top, left=left, width=15, height=40))
		regions_list.append(ScreenRegion(top=top, left=left-70, width=15, height=40))

		#Creation of the Window
		screen_name = 'Jumper'
		cv2.namedWindow(screen_name)
		cv2.moveWindow(screen_name, 40, 500)

		windows_region = ScreenRegion(top=top, left=left-110, width=150, height=50)

		for region in regions_list:

			jump_action = jump_check(region)

			if jump_action:
				print "jump!"
				pyautogui.press('space')
			
			draw_region(windows_region, region, RED if jump_action else BLUE)
		
		#Render de ScreenRegion
		cv2.imshow(screen_name, windows_region.getNumpyImage())
		cv2.waitKey(10)














				
			