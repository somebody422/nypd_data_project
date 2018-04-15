import os
import sys


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

input_file = open(path_to_datafile, 'r')

attributes_with_whitespace = input_file.readline().split(',')
attributes = map(lambda x: x.strip(), attributes_with_whitespace)
print(attributes)

records = []
for line in input_file:
	records.append(line.split(','))

for record in records:
	print(record)

	git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/somebody422/nypd_data_project.git
git push -u origin master