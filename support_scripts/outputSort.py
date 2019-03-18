# Supervising list of lists
ozymandias = []

# Copy of ozymandias that holds lists with relevant p values
don = []

# Final sorted list that writes to sortedOutput.txt
arthur = []

# Parses Output.txt, converts each line to list of 5 strings
filen = open("/research/ViromeMetagenomics/Tim/VirusGenomes/RefSeq/results/Output.txt", 'r')
line = filen.readline()
while(line):
	splitLine = line.split('\t', 4)
	ozymandias.append(splitLine)
	line = filen.readline()
filen.close()

# Remove watermark from output file
del ozymandias[-1]

# Copy of output lists that contains only lists with relevant p values
for x in ozymandias:
	if x[2] != '1' or x[3] != '1':
		don.append(x)

# Relevant lists in don have their association value converted to floats in order to rank comparisons
for x in don:
	x[4] = x[4][:-1]
	x[4] = x[4].split('/')
	x[4] = float(x[4][0])/int(x[4][1])

# Arthur is populated by sorted lists based on size of comparitive index	
arthur = sorted(don, key = lambda x: x[4]) 

# Comparitive values are returned to strings for final ouput, and the list is reversed so highest values are presented first
for z in arthur:
	z[4] = z[4] * 1000
	z[4] = str(z[4]) + '/1000'
arthur.reverse()

# List is rejoined into string and written to sorted result file
fileObj = file('/research/ViromeMetagenomics/Tim/VirusGenomes/RefSeq/results/sortedOutput.txt', 'w')
fileObj.write('Tim Kosfeld \n')
for t in arthur:
	i = '\t'.join(t)
	i = i+ '\n'
	fileObj.write(i)	
fileObj.close()	
