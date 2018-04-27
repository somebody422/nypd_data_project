"""
Little script to put together a small data set by randomly sampling
 a larger one
"""
import os
import sys
import random



if len(sys.argv) != 3:
	print("Must provide input and output file names")
	sys.exit(1)

path_to_input_file = sys.argv[1]
path_to_output_file = sys.argv[2]

if not os.path.exists(path_to_input_file):
	print("Cannot find the data file")
	sys.exit(2)

if os.path.exists(path_to_output_file):
	print("Output file already exists, will not overwrite")
	sys.exit(3)


input_file_len_in_bytes = os.stat(path_to_input_file).st_size

input_file = open(path_to_input_file, 'r')
output_file = open(path_to_output_file, 'w')



# First, copy over the first line.. That is the attribute list
output_file.write(input_file.readline())



# randomly sample, and save to output file as we go. This is a quick/dirty
#  solution, it will ignore the last 100 bytes of the file, and will never
#  sample the first line.
# Note: there may be duplicates in the output file!!
NUM_TIMES = 300000
for i in range(NUM_TIMES):
	start_byte = random.randint(0, input_file_len_in_bytes-100)
	input_file.seek(start_byte, 0)
	# iterate forward until we find a new line
	while input_file.read(1) != '\n': pass
	#c = 0
	#while c != '\n':
	#	c = input_file.read(1)
	#	print(c)
	output_file.write(input_file.readline())

input_file.close()
output_file.close()