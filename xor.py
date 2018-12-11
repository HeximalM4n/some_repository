inputFile = open('input.txt','r')
outputFile = open('output.txt','w')

print ('Enter the key: ')
key = input()

outputFile.write('Using key: {}\n'.format(key))

for line in inputFile:
	for ch in line:
		try:
			outputFile.write('{}\n'.format(ord(ch) ^ ord(key)))
		except TypeError:
			outputFile.write('{}\n'.format(ord(ch) ^ int(key)))

inputFile.close()
outputFile.close()
