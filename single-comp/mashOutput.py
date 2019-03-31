import os
from subprocess import call
import random
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("input", type = str, help = "Dataset directory")
parser.add_argument("output", type = str, help = "Results directory")
#parser.add_argument("file", type = str, help = "Single comparison file compared to all genomes in dataset")
parser.add_argument("-f", "--filetype", type = str, default = '.fna',
	help = "Optional argument to set genome file type for analysis, defaults to .fna")
args = parser.parse_args()
print args.input
print args.output
#print args.file
print args.filetype

f = []
g = []
p = []

# Populate list p with .msh sketchest
for file in os.listdir(args.input):
        if file.endswith('.msh'):
                p.append(file)


# Error checking for population P
print len(p)



lineCount = 0;
while lineCount < 51:
	h = 0
	a = open(args.output + '/Output.txt', 'w')
	randFile = random.choice(p)

	for x in p:
		if args.input + x == args.input + randFile:
			continue
		call(['mash','dist', args.input + randFile, args.input + x], stdout = a)
		h = h + 1
		print h	
	print h
	a.close()

	call(['python', 'outputSort.py', 'results/', 'Output.txt'])

	lineCount = 0
	sortedFile = open('results/sortedOutput.txt', 'r');
	for line in sortedFile:
		lineCount += 1
	print lineCount

