import mss
import numpy

class ScreenRegion:

	def __init__(self, top, left, width, height):
		self.top = top
		self.left = left
		self.width = width
		self.height = height
		self.numpy_image = None

	def toDict(self):
		return {'top': self.top, 'left': self.left, 'width': self.width, 'height': self.height }

	def getImage(self):
		sct = mss.mss()
		return sct.grab(self.toDict())

	def getNumpyImage(self):
		if type(self.numpy_image) is not numpy.ndarray:
			self.numpy_image = numpy.array(self.getImage())
		return self.numpy_image

	def getAverageColor(self):
		avg_color_per_row = numpy.average(self.getNumpyImage(), axis=0)       
		return numpy.average(avg_color_per_row, axis=0)