#Name: Tim Kosfeld
#Email: kosfeldtd@slu.edu
#Current Date: 11/5
#driver for genomic seperation program

#import user-defined index class
from Index import Index
from subprocess import call
#creates an index object
viralIndex = Index()
#calls the open file method to attempt to open .txt file editorsNotes
#viralIndex.openFile('all_viral.fa')
#calls loadData method to read and store data from file to dictionary topics
#viralIndex.processData()
call(['python', 'mashOutput.py'])
distIndex = Index()
distIndex.openFile('Output.txt')
distIndex.sortData()
