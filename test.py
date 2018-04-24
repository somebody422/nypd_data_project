import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot
from sklearn import cluster


#as_array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

as_array = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12]
]

as_matrix = np.matrix(as_array)

matrix_transposed = as_matrix.getT()



data = np.matrix([
	[1, 3, 22, 345, 12, 2],
	[2, 4, 6, 8, 55, 363]
])

data = np.matrix([
	[1, 2],
	[3, 4],
	[22, 6],
	[345, 8],
	[12, 55],
	[2, 363]
])

cl = cluster.KMeans(n_clusters = 3)


"""
figure, axes = pyplot.subplots(1, 1)
axes.set_xlim(0, 5)
axes.set_ylim(0, 5)
for i in (1, 2, 3, 4):
	axes.text(i, i, str(i), size=14)
axes.legend(["test legend"])
pyplot.show()
"""