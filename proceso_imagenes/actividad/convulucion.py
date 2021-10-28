import kernel
import numpy
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage
#g es kernel
def convolucion(imagen,kernel):
	Is=Image.open(imagen)
	I=Is.convert('L')
	I=numpy.asarray(I)
	I=I/255.0
	#/k=g
	j0=ndimage(I, kernel, mode='constant', cval=0.0)

	plt.figure(figsize = (15,15))

	plt.subplot(2,2,1)
	plt.imshow(Is)
	plt.xlabel('Input Image')

	plt.subplot(2,2,2)
	plt.imshow(j0)
	plt.xlabel('VH direction')
	plt.grid(False)
	plt.show()
	return
k=kernel.gauss_blur(k=7,sigma=1)
con=convolucion(imagen='gradients.jpg',kernel=k)
print(con)
