# parse through csv quickly, good for doing a quick check
# should be opening a CLEANED data file

import os
import sys

if len(sys.argv) != 2:
	print("Usage: python %s DATA_CSV_FILE" % sys.argv[0])
	sys.exit(1)

path_to_datafile = sys.argv[1]

if not os.path.exists(path_to_datafile):
	print("Cannot open provided data file")
	sys.exit(2)


input_file = open(path_to_datafile, 'r')

attributes = input_file.readline().split(',')
print(attributes)

index_of_attribute = {}
for i in range(len(attributes)):
	index_of_attribute[attributes[i]] = i
print("\nIndexes:")
print(index_of_attribute)


lowest_longitude = 0
highest_longitude = 0
lowest_latitude = 0
highest_latitude = 0


for line in input_file:
	split_line = line.split(',')
	latitude = float(split_line[index_of_attribute['LATITUDE']])
	longitude = float(split_line[index_of_attribute['LONGITUDE']])
	#print("Longitude = " + str(longitude))
	if lowest_longitude == 0 or longitude < lowest_longitude:
		print("changing lowest_longitude from %f to %f" % (lowest_longitude, longitude))
		lowest_longitude = longitude
	if highest_longitude == 0 or longitude > highest_longitude:
		print("changing highest_longitude from %f to %f" % (highest_longitude, longitude))
		highest_longitude = longitude
	if lowest_latitude == 0 or latitude < lowest_latitude:
		print("changing lowest_latitude from %f to %f" % (lowest_latitude, latitude))
		lowest_latitude = latitude
	if highest_latitude == 0 or latitude > highest_latitude:
		print("changing highest_latitude from %f to %f" % (highest_latitude, latitude))
		highest_latitude = latitude

print("lowest_latitude = " + str(lowest_latitude))
print("highest_latitude = " + str(highest_latitude))
print("lowest_longitude = " + str(lowest_longitude))
print("highest_longitude = " + str(highest_longitude))



