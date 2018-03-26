from docx import Document
import os, collections, sys, string
import numpy as np
import matplotlib.pyplot as plt

# Add all words from file 'filename' to 'fulltext'
def getText(filename, fullText):
    doc = Document(filename)
    for para in doc.paragraphs:
        for word in para.text.lower().split():
            fullText.append(word)
    return fullText

# Return unordered dict of word-length frequencies
def lengthFreqDict(fullText):
    lengthFreq = {}

    for word in fullText:
        word_length = len(word)
        try:
            lengthFreq[word_length] = lengthFreq[word_length] + 1 
        except KeyError:
            lengthFreq[word_length] = 1

    return lengthFreq

# Calls getText() on all valid files.
# Uses collected text as data for graph functions.
def graphs_from_directory(directory):
    fullText = []
    for path, subdirs, files in os.walk(directory):
        for f in files:
        	if f.endswith(".docx"):
        		# Skip temporary files
        		if not (f.startswith("~")):
        			getText(os.path.join(path, f), fullText)
        		else:
        			print ("Skipped document " + f)
                
    LFD = lengthFreqDict(fullText)

    graphlength (LFD)
    graphletters (fullText)

# Given a dictionary of word lengths, outputs a bar graph.
def graphlength (LFD):
    LFD = collections.OrderedDict(sorted(LFD.items()))
    n_groups = len(LFD)
    lengths = []
    counts = []

    for key in LFD:
        lengths.append(key)
        counts.append(LFD[key])

    index = np.arange(n_groups)
    bar_width = 0.35

    opacity = 0.4

    rects1 = plt.bar(index, counts, bar_width,
                     alpha=opacity,
                     color='b')

    plt.xlabel('Number of Letters')
    plt.ylabel('Word Count')
    plt.title('Distribution of Word Lengths')
    plt.xticks(index, lengths)

    plt.tight_layout()
    plt.show()

# Given a list of all text in the scanned files,
# outputs a bar graph of letter usage.
def graphletters (fullText):
    allstrings = ''.join(fullText)
    count = collections.Counter(allstrings)
    graph_list = []
    
    for letter in list(string.ascii_lowercase):
        graph_list.append (count[letter])

    index = np.arange(26)
    bar_width = 0.35

    opacity = 0.4

    rects1 = plt.bar(index, graph_list, bar_width,
                     alpha=opacity,
                     color='b')

    plt.xlabel('Letter')
    plt.ylabel('Frequency')
    plt.title('Distribution of Letters Used')
    plt.xticks(index, list(string.ascii_lowercase))

    plt.tight_layout()
    plt.show()

# Searches all files in 'directory' for 'term', 
# then outputs a list of all documents containing 'term'.
def search_directory(directory, term):
    doclist = []
    for path, subdirs, files in os.walk(directory):
        for f in files:
        	if f.endswith(".docx"):
        		# Skip temporary files
        		if not (f.startswith("~")):
        			fullText = getText(os.path.join(path, f), [])
        			for word in fullText:
        				if word == term:
        					doclist.append(f)
        					break
        		else:
        			print ("Skipped document " + f)

    if len(doclist) == 0:
        print ("No documents found containing input term.")
    else:
        print (doclist)

# Check user input for correct syntax,
# determine which subprogram to run.
try:
    prog = sys.argv[1]
    try:
        directory = sys.argv[2]
        if os.path.isdir(directory):
            if prog == "search":
                try:
                    term = sys.argv[3]
                    search_directory(directory, term.lower())
                except IndexError:
                    print ("Please input search term.")
            elif prog == "graphs":
                graphs_from_directory(directory)
            else:
            	print("Invalid program function. Please input 'graphs' or 'search'.") 
        else:
            print ("Invalid directory.")
    except IndexError:
        print("Please input directory.")
except IndexError:
    print("Please input program function.")