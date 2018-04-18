import os
import sys
import numpy as np
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

records = []
for line in input_file:
	records.append(map(lambda x: x.strip(), line.split(',')))

#for record in records:
#	print(len(record))

input_file.close()

#dont keep this
for row in range(len(records)):
	for col in range(len(records[row])):
		if records[row][col].find('\"') >= 0:
			records[row][col] = "butts"

for record in records:
	print(len(record))
	for d in record:
		if not ( type(d) is str):
			print("ERROR: record is not string")
			print(record)
			print(d)

print(records)

# Keep in mind numpy arrays do not do mixed types by
#  default!! This means that the records will be stored as strings
print("Converting to np array..")
records_np = np.matrix(records, dtype='bytes_')
print("\nNormal np array:")
print(records_np)
print(type(records_np))
print(records_np.dtype)

#print("Creating a transposed version..")
#records_np_transposed = records_np.getT()
#print("\nTransposed np array:")
#print(records_np_transposed)


#cov_matrix = np.cov(records_np)
#print("\nCovariance matrix:")
#print(cov_matrix)


#gc.collect()

# Next step: Data cleaning!
# Try creating several versions of "attributes" and "records". Each
#  Will only have the attribtues we are interested in.
#  Do this with references somehow? Don't really want multiple copies of 
#  that large database..




# Plot the long/lat of the accidents

