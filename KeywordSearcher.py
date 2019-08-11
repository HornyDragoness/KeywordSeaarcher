import re, os
compiled = input('Enter the pattern:\n')
directory = input('Enter the directory to search in:\n')
pattern = re.compile(compiled)

for file in os.listdir(str(directory)):
	if '.txt' in str(file):
		found = open(directory + str(file), 'r')
		red = found.read()
		spl = red.split('\n')
		if compiled in red:
			for i in range(len(spl)):
				if compiled in spl[i]:
					print(spl[i])
