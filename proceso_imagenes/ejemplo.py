import numpy
def mexhat(sigma,k):
	m = numpy.zeros((k,k));
	for x in range(0,k):
		for y in range(0,k):
			m[x][y] = 1/(numpy.pi*sigma**4) * (1-1/2*(x**2 + y**2)/sigma**2)*numpy.exp(-(x**2+y**2)/(2*sigma**2))
	return m
m1=mexhat(sigma=1,k=5)
print(m1)
