import sys
import os
import re



attributes_to_keep = [
	'DATE', 'TIME', 'BOROUGH', 'ZIP CODE', 'LATITUDE', 'LONGITUDE', 'ON STREET NAME', 'CROSS STREET NAME', 'OFF STREET NAME', 'NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED', 'NUMBER OF PEDESTRIANS INJURED', 'NUMBER OF PEDESTRIANS KILLED', 'NUMBER OF CYCLIST INJURED', 'NUMBER OF CYCLIST KILLED', 'NUMBER OF MOTORIST INJURED', 'NUMBER OF MOTORIST KILLED'
]


if len(sys.argv) != 2 and len(sys.argv) != 3:
	print("Usage: python clean_input.py INPUT_FILE [OUTPUT_FILE]")
	sys.exit(1)

path_to_input_file = sys.argv[1]

if not os.path.exists(path_to_input_file):
	print("Cannot find the data file")
	sys.exit(2)

if len(sys.argv) == 3 and not os.path.exists(sys.argv[2]):
	path_to_output_file = sys.argv[2]
else:
	path_to_input_file_without_extention = re.sub(r'\.[^.]+', '',  path_to_input_file)
	path_to_output_file = path_to_input_file_without_extention + '_cleaned.csv'
	if os.path.exists(path_to_output_file):
		os.remove(path_to_output_file)


input_file = open(path_to_input_file, 'r')
output_file = open(path_to_output_file, 'w')

raw_input_text = input_file.read()
input_file.close()

# A tweak unique to this data set: One field has a comma mixed in.
raw_input_text = re.sub(r'\"\(([-0-9.]+), ([-0-9.]+)\)\"', r'(\1 \2)', raw_input_text)

# Figure out what the line separator is for this file
num_newlines = len(re.findall(r'\n', raw_input_text))
num_carriage_returns = len(re.findall(r'\r', raw_input_text))
print("num_newlines = %d" % num_newlines)
print("num_carriage_returns = %d" % num_carriage_returns)
if num_newlines > num_carriage_returns:
	line_separator = '\n'
elif num_newlines < num_carriage_returns:
	line_separator = '\r'
else:
	line_separator = '\r\n'

lines = raw_input_text.split(line_separator)

# Find the first line that is not blank. Assume the attributes are listed
#  there
first_line_with_text = 0
while lines[first_line_with_text] == '':
	first_line_with_text += 1

# Parse through the first line to find the indexes of attributes we
#  want
attribute_indexes = []
split_attributes = lines[first_line_with_text].split(',')
for i in range(len(split_attributes)):
	attribute = split_attributes[i].strip()
	if attribute != '' and attribute in attributes_to_keep:
		attribute_indexes.append(i)
		output_file.write(attribute + ',')
# Seek backwards one byte, to overwrite that last comma
#output_file.seek(-1, 1)
output_file.write('\n')
print("Indexes to use: " + str(attribute_indexes))


# Iterate through remaining lines and parse all of the data entries.
for line in lines[first_line_with_text+1:]:
	split_line = line.split(',')
	for i in attribute_indexes:
		output_file.write(split_line[i] + ',')
		print("Writing: " + split_line[i])
	output_file.seek(-1, 1)
	output_file.write('\n')

# Get rid of the final newline we printed
output_file.seek(-1, 1)
output_file.truncate()

# All done!

output_file.close()