import cv2

def jump_check(region, level=200.0):
	r,g,b,_ = region.getAverageColor()
	return (r.item() < level) and (g.item() < level) and (b.item() < level)

def draw_region(w_region, region, color):
	#We have to setup an Scala because Mac Retina Display increase the size of the regions
	scala = 2
	x_1 = (region.left - w_region.left) * scala
	x_2 = x_1 + region.width * scala
	y_1 = (region.top - w_region.top) * scala
	y_2 = y_1 + region.height * scala
	cv2.rectangle(w_region.getNumpyImage(), (x_1, y_1), (x_2, y_2), color, 2)