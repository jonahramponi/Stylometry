
import os
from os import listdir
import os.path
import re
import string
import collections
import math
from collections import Counter

inputdirectory = "C:\\Users\\jonah\\Documents\\GitHub\\Stylometry\\Stylometry\\data\\Raw\\"
outputdirectory =  "C:\\Users\\jonah\\Documents\\GitHub\\Stylometry\\Stylometry\data\\Processed\\"

frequentwords = ['a', 'all', 'also', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'been', 'but', 'by', 'can', 'do', 'down', 'even', 'every', 'for', 'from', 'had', 'has', 'have', 'her', 'his', 'if', 'in', 'into', 'is', 'it', 'its', 'may', 'more', 'must', 'my', 'no', 'not', 'now', 'of', 'on', 'one', 'only', 'or', 'our', 'shall', 'should', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'then', 'there', 'things', 'this', 'to', 'up', 'upon', 'was', 'were', 'what', 'when', 'which', 'who', 'will', 'with', 'would', 'your']


def only_printable_ascii(string):
    ''' Returns the string without non-ASCII characters and non-printable ASCII'''
    stripped = (c for c in string if 31 < ord(c) < 127)
    return ''.join(stripped)
    

#takes a chunk of words and returns vectors containing the counts of word lenghts, function words, common words etc
def createvector(wordlist):
	wordcounter = Counter()
	numwords = 0
	for word in wordlist:	
		if len(word) > 0:	
			wordcounter[word] += 1
			numwords+=1
		else:
			print('Error: zero length words')		
		
	frequentwordsvec = []
	frequentwordscount = 0
	
	for word in frequentwords:
		frequentwordsvec.append(wordcounter[word])
		frequentwordscount = frequentwordscount+wordcounter[word]

		
	frequentwordsvec.append(numwords-frequentwordscount)
	
	return (frequentwordsvec)



print("Processing files...")
outputdir =  outputdirectory
inputdir =  inputdirectory 

if not os.path.exists(outputdir):
	os.makedirs(outputdir)
		
files = listdir(inputdir)
files.sort() #puts unknown at the end
print(files)

for text in files:
	frequentwordsfile = open(outputdir+text, 'w')
	print(outputdir+text)
	with open(inputdirectory +  text, 'rb') as myfile:
			
		allwords = []
			
		for line in myfile:
			line = only_printable_ascii(line)											#strips other non-english characters
			line =  re.sub('[,\.]',' ',line)											#replace . and , with spaces
			line =  line.translate(str.maketrans('','',string.punctuation))		#delete all remaining punctuation					
			line = line.replace('\n', ' ').replace('\r', '')							#replaces new line with space									
			line = ' '.join(line.split())												#replace multiple spaces with a single one
			line = line.lower()		
			
			words = line.split(" ")													#break the line down into individual words by splitting on spaces
			for word in words:		
				word = word.replace(" ", "")										
				#word = word.translate(None, string.whitespace)
				if word=='' or len(word)<1: 										#if we are left with an empty word after stripping out bad characrers, then throw it away
					continue		
				allwords.append(word)

		frequentwordsvec = createvector(allwords)
		frequentwordsfile.write(str(frequentwordsvec).strip('[]')  + "\n")
    
	
	
	