import os
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot
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
	print(strline + "  --->  " + str(line))
	#records.append(map(lambda x: x.strip(), line.split(',')))

print("\nEnums:")
print(enums)

input_file.close()
print("\nRecords:")
print(records)






# Keep in mind numpy arrays do not do mixed types by
#  default!! This means that the records will be stored as strings
print("Converting to np array..")
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

# Plot the long/lat of the accidents
figure, axes = pyplot.subplots(1, 1)
axes.plot(
	records_matrix_transposed[index_of_attribute["LONGITUDE"]],
	records_matrix_transposed[index_of_attribute["LATITUDE"]],
	'k.'
)
pyplot.show()

# Next, decide how to plot a LARGE number of accidents: cluster points and display the clusters?



