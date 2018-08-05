#from mss import mss
from mss.darwin import MSS as mss
from PIL import Image, ImageDraw
import numpy
import cv2
import time
import pyautogui

SCREEN_NAME = 'Jumper'
SHOW_FRAME = True
TIMER = 2
X_AXIS = 0
Y_AXIS = 0
WIDTH  = 15 #15
HEIGHT = 40 #40
W_WIDTH = 150
W_HEIGTH = 50
W_X_AXIS = 0
W_Y_AXIS = 0
DIFF_MOUSE_X_AXIS = 110
windows_image = None
SCALA = 2

def region_average_color(x, y, width, height):
	region = {'top': y, 'left': x, 'width': width, 'height': height }
	numpy_img = numpy.array(sct.grab(region))
	avg_color_per_row = numpy.average(numpy_img, axis=0)       
	return numpy.average(avg_color_per_row, axis=0)

def jump_check(x, y, width=WIDTH, height=HEIGHT, level=200.0, show_frame = SHOW_FRAME):
	r,g,b,_ = region_average_color(x=x, y=y, width=width, height=height)
	
	jump_action = (r.item() < level) and (g.item() < level) and (b.item() < level)

	if show_frame:

		x_1 = (x-W_X_AXIS)*SCALA
		x_1 = int(x_1)
		x_2 = x_1 + width*SCALA
		x_2 = int(x_2)
		y_1 = (y-W_Y_AXIS)*SCALA
		y_1 = int(y_1)
		y_2 = y_1+height*SCALA
		y_2 = int(y_2)

		if jump_action:
			cv2.rectangle(windows_image, (x_1, y_1), (x_2, y_2), (0,0,255), 2)
		else:
			cv2.rectangle(windows_image, (x_1, y_1), (x_2, y_2), (255,0,0), 1)

	if jump_action:
		print "jump!"
		print '%.2f - %.2f - %.2f' % (r,g,b)
		pyautogui.press('space')

		#pyautogui.press('down')

if __name__ == "__main__":

	for i in range(TIMER):
		time.sleep(1)
		print TIMER-i

	print 'Go!!!!!'

	with mss() as sct:

		if SHOW_FRAME:
			cv2.namedWindow(SCREEN_NAME)
			cv2.moveWindow(SCREEN_NAME, 40, 500)

		while True:

			X_AXIS, Y_AXIS = pyautogui.position()
			#X_AXIS = 760
			#Y_AXIS = 280

			W_Y_AXIS = Y_AXIS
			W_X_AXIS = X_AXIS-DIFF_MOUSE_X_AXIS

			region = {'top': W_Y_AXIS, 'left': W_X_AXIS, 'width': W_WIDTH, 'height': W_HEIGTH }
			windows_image = numpy.array(sct.grab(region))

			jump_check( x=X_AXIS, y=Y_AXIS, show_frame=True)
			jump_check( x=X_AXIS-70, y=Y_AXIS, show_frame = True)

			cv2.imshow(SCREEN_NAME, windows_image)
			cv2.waitKey(10)














				
			