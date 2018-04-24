import os
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot
from sklearn import cluster
#import gc


# Takes a string. Return true iff it is a number
def isNumber(s):
	# Special case: empty string is a string
	if s == '':
		return False
	for c in s:
		if c < '0' or c > '9':
			if c != '.' and c != '-':
				return False
	return True


# I'm borrowing from C. An "enum" here is an number representation
#  of a string. As I go through I will be making sure EVERYTHING
#  is a number, which will numpy much nicer
class Enum:
	def __init__(self):
		self.next_index = 1
		self.name_from_num = []
		self.num_from_name = {}

	def addValue(self, name):
		self.name_from_num.append(name)
		self.num_from_name[name] = self.next_index
		self.next_index += 1

	#def numFromName(self, name):
	#	return self.num_from_name[name]
	#def nameFromNum(self, num):
	#	return self.name_from_num[num]



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
enums = [Enum() for _ in attributes]
for strline in input_file:
	fields = strline.split(',')
	line = []
	for i in range(len(fields)):
		field = fields[i]#.strip()
		#print("Field: " + str(field))
		if isNumber(field):
			line.append(float(field))
		else:
			if field not in enums[i].num_from_name:
				enums[i].addValue(field)
			line.append(enums[i].num_from_name[field])
	records.append(line)

print("\nEnums:")
print(enums)

input_file.close()
print("\nRecords:")
print(records)




print("Converting to np matrix..")
#records_matrix = np.matrix(records, dtype='bytes_')
records_matrix = np.matrix(records)
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

"""
# Plot the long/lat of the accidents
figure, axes = pyplot.subplots(1, 1)
axes.plot(
	records_matrix_transposed[index_of_attribute["LONGITUDE"]],
	records_matrix_transposed[index_of_attribute["LATITUDE"]],
	'k.'
)
axes.legend(["test legend"])
pyplot.show()
"""

# Next, decide how to plot a LARGE number of accidents: cluster points and display the clusters?
k = 5
kmeans = cluster.KMeans(n_clusters = k)
# This won't work if longitude doesn't come right after
#  latitude
kmeans.fit(records_matrix[:, index_of_attribute['LATITUDE']:index_of_attribute['LATITUDE']+2])

# Now count the number of point in each cluster:
num_points_in_cluster = [0 for _ in range(k)]
for clustered_point in kmeans.labels_:
	num_points_in_cluster[clustered_point] += 1

print("\nnum_points_in_cluster:")
print(num_points_in_cluster)
print("\nkmeans centers:")
print(kmeans.cluster_centers_)
print("\nkmeans labels:")
print(kmeans.labels_)

# Find the highest/lowest long/lat for plotting
lowest_longitude = 0
highest_longitude = 0
lowest_latitude = 0
highest_latitude = 0
for record in records:
	latitude = line[index_of_attribute['LATITUDE']]
	longitude = line[index_of_attribute['LONGITUDE']]
	if lowest_longitude == 0 or longitude < lowest_longitude:
		lowest_longitude = longitude
	if highest_longitude == 0 or longitude > highest_longitude:
		highest_longitude = longitude
	if lowest_latitude == 0 or latitude < lowest_latitude:
		lowest_latitude = latitude
	if highest_latitude == 0 or latitude > highest_latitude:
		highest_latitude = latitude


# Plot the kmeans cluster centers with the number
#  of points in the cluster
figure, axes = pyplot.subplots(1, 1)
axes.set_xlim(0, 5)
axes.set_ylim(0, 5)
for i in (1, 2, 3, 4):
	axes.text(i, i, str(i), size=14)
axes.legend(["test legend"])
pyplot.show()



#sc.fit()

