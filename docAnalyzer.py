from docx import Document
import os, collections, sys

# Get all words from file 'filename' 
def getText(filename, fullText):
    doc = Document(filename)
    for para in doc.paragraphs:
        for word in para.text.lower().split():
            fullText.append(word)
    return fullText

# Return unordered dict of word frequencies
def wordFreqDict(fullText):
    wordFreq = []  
    for word in fullText:
        word_count = fullText.count(word) 
        wordFreq.append((word, word_count)) 
    return dict(wordFreq)

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

# 
def lists_from_directory(directory):
    fullText = []
    for path, subdirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".docx"):
                #try:
                    getText(os.path.join(path, f), fullText)
                #except:
                #    print ("Skipping document" + f)
    
    WFD = wordFreqDict(fullText)             
    LFD = lengthFreqDict(fullText)

    print (list(collections.OrderedDict(sorted(WFD.items(), key=lambda t: t[1], reverse = True)).items()))
    print (list(collections.OrderedDict(sorted(LFD.items(), key=lambda t: t[1], reverse = True)).items()))

#
def search_directory(directory, term):
    doclist = []
    for path, subdirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".docx"):
                fullText = getText(os.path.join(path, f), [])
                for word in fullText:
                    if word == term:
                        doclist.append(f)
                        break

    if len(doclist) == 0:
        print ("No documents found containing input term.")
    else:
        print (doclist)

# Main
try:
    prog = sys.argv[1]
    try:
        directory = sys.argv[2]
        if os.path.isdir(directory):
            if prog == "search":
                try:
                    term = sys.argv[3]
                    search_directory(directory, term)
                except:
                    print ("Please input search term.")
            elif prog == "lists":
                lists_from_directory(directory)
        else:
            print ("Invalid directory.")
    except IndexError:
        print("Please input directory.")
except IndexError:
    print("Please input program instruction.")

