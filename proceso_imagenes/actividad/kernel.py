import numpy
def gauss_blur(k, sigma):
	G=numpy.zeros((k, k))
	for x in range(0,k):
		for y in range(0,k):
			G[x][y]=(1/(2*numpy.pi*sigma**2))*numpy.exp(-((x**2+y**2)/(2*sigma**2)))
	return G

g=gauss_blur(k=7,sigma=1)
print(g)
