#Name: Tim Kosfeld
#Email: kosfeldtd@slu.edu
#Current Date:  11/4/2018
#Research Folder: Virome Metagenomics
#Abstract: Mash sketch and draw functions only operate on single genomic sequences. 
#	   As such a program must be able to efficiently seperate large amounts of Genomic data. 
#	   As Python has the ability to read and write lines of data it is more efficient in handling such a task.


class Index:
    #creates fileObject given None
    def __init__(self): 
        self._fileObject = None

    #function hopefully opens a compatible .fa file containing multiple genomese
    def openFile(self, fileName):
        #filename iput will persist through errors in input
        while (not self._fileObject):
            #try except asks for new file name if IOError occurs
            try:
                self._fileObject = file(fileName)
            except IOError:
                #if the file cannot be found asks for reinpute
                print 'Sorry, unable to open file', fileName
                fileName = raw_input('Enter a new file name : ')
                
    #loads data from opened file, writing it to a dictionary topics 
    def processData(self):
        count = 1
        #reads first line
        line = self._fileObject.readline()
        #while there are still lines in file
        while(line):
            #if the line contains a number, it is presumably the appopriate title for the following genome
            if any(char.isdigit() for char in line) == True:
                if(count>1):
                    fileObj.close()
                #strip file title of unecessary repetitions
                splitList = line.split(',', 1)
                splitList.pop()
                fileName = ''.join(splitList)
                fileName = fileName.replace(' ', '_')
                fileName = fileName.replace('/', '_')
                fileName = fileName[4:]
		fileName = fileName + ('.fna')
                fileObj = file(fileName,'w')
                fileObj.write(line)
                count = count + 1
            #if the line is part of a genomic database it gets writtent to the specified file
            else:
                fileObj.write(line)           
            #reads next line
            line = self._fileObject.readline()
    def sortData(self):
	ozymandias = []
	line = self._fileObject.readline()
	while(line):
		splitLine = line.split('\t', 4)
		ozymandias.append(splitLine)
		line = self._fileObject.readline()
	for x in ozymandias:
		x[4] = x[4][:-1]
		num,dem = x[4].split('/')
		x[4] = float(int(num)/int(dem))
		#print x[4]
	for y in range(len(ozymandias)):
		min = y
		for z in range(y+1, len(ozymandias)):
			if ozymandias[min][4] > ozymandias[z][4]:
				min = z
		ozymandias[y], ozymandias[min] = ozymandias[min], ozymandias[y] 
	fileObj = file('sortedOutput.txt', 'w')
	for a in reversed(ozymandias):
		a[4] = repr(a[4])
		string = '\t'.join(a)
		fileObj.write(string + '\n')
	fileObj.close()		
