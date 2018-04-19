import os
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot
#import gc


# Takes a string. Return true iff it is a number
def isNumber(s):
	for c in s:
		if c < '0' or c > '9':
			if c != '.' and c != '-':
				return False
	return True


if len(sys.argv) != 2:
	print("Usage: python %s DATA_CSV_FILE" % sys.argv[0])
	sys.exit(1)

path_to_datafile = sys.argv[1]

if not os.path.exists(path_to_datafile):
	print("Cannot open provided data file")
	sys.exit(2)



# First we need to read in the file. This thing is HUGE!
# * Build python array
# * Convert to numpy array/matrix

input_file = open(path_to_datafile, 'r')

attributes_with_whitespace = input_file.readline().split(',')
attributes = map(lambda x: x.strip(), attributes_with_whitespace)
print(attributes)

index_of_attribute = {}
for i in range(len(attributes)):
	index_of_attribute[attributes[i]] = i
print("\nIndexes:")
print(index_of_attribute)

records = []
for line in input_file:
	records.append(map(lambda x: x.strip(), line.split(',')))


input_file.close()

print(records)

# Keep in mind numpy arrays do not do mixed types by
#  default!! This means that the records will be stored as strings
print("Converting to np array..")
records_matrix = np.matrix(records, dtype='bytes_')
print("\nNormal np array:")
print(records_matrix)
print(type(records_matrix))
print(records_matrix.dtype)

print("Creating a transposed records_matrix..")
records_matrix_transposed = records_matrix.getT()
print("\nTransposed np array:")
print(records_matrix_transposed)


#cov_matrix = np.cov(records_matrix, rowvar=False)
#print("\nCovariance matrix:")
#print(cov_matrix)


#gc.collect()





# Plot the long/lat of the accidents

print("\nX values are latitude:")
print(records_matrix_transposed[index_of_attribute["LONGITUDE"]])

print("\nY values are longitude:")
print(records_matrix_transposed[index_of_attribute["LATITUDE"]])
figure, axes = pyplot.subplots(0, 0)
axes.plot(
	records_matrix_transposed[index_of_attribute["LONGITUDE"]],
	records_matrix_transposed[index_of_attribute["LATITUDE"]],
	linestyle = 'None',

)
pyplot.show()





