import os
from subprocess import call
from random import choice as rchoice
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("input", type = str, help = "Input directory")
parser.add_argument("output", type = str, help = "Output directory")
parser.add_argument("-n", "--number", type = int, default = 100, 
	help = 'Optional argument to set number of genomes processed, default to 100')
parser.add_argument("-f", "--filetype", type = str, default = '.fna',
	help = "Optional argument to set genome file type for analysis, defaults to .fna")
args = parser.parse_args()
print args.input
print args.output
print args.number
print args.filetype

f = []
g = []
p = []

# Populate list f with fna filenames
for file in os.listdir(args.input):
	if file.endswith(args.filetype):
		f.append(file)

# Re-populate list with filename, size tuples
#for i in xrange(len(f)):
#	f[i] = (f[i], os.path.getsize(f[i]))

# Sort list by file size
# If reverse=True sort from largest to smallest
# If reverse=False sort from smallest to largest
#f.sort(key=lambda filename: filename[1], reverse=True)

# Re-populate list with just filenames
#for i in xrange(len(f)):
#	f[i] = f[i][0]

# Subindex genome list for first user dictated entries
g = f[:args.number]

# Mash Sketch of each of the genomes
for genome in g:
	call(['mash','sketch', args.input + '/' + genome])

# Populate list p with .msh sketchest
for file in os.listdir(args.input):
        if file.endswith('.msh'):
                p.append(file)

# Error checking for population P
print len(p)

# File output automation
a = open(args.output + '/Output.txt', 'w')
a.write('Tim Kosfeld')

# Piecewise mash distance comparison
h = 0
for x in p:
	for y in p:
		call(['mash','dist', args.input + '/' + x, args.input + '/' + y], stdout = a)
	p.remove(p[h])
	print h
	h += 1	
print h
a.close()
