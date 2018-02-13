Program: docAnalyzer.py
Creator: Taylor Ampatiellos

How to Use:
	This program has two current functions.
		- The first, accessed with the "lists" argument, scans a given directory
		  for .docx files, then returns two lists of pairs:
		  	 - A word frequency list, where the first pair element is a word
		  	   and the second pair element is the number of times it appears
		  	   throughout all scanned documents.
		  	 - A word length frequency list, where the first pair element is
		  	   an int signifying word length and the second pair element is
		  	   the number of words of this length appearing throughout all
		  	   scanned documents.
		- The second, accessed with the "search" argument, scans a given 
		  directory for .docx files and returns a list of files containing
		  the given search term.

Syntax:
	The program takes 2 or 3 arguments, depending on the intended function.
		- Lists: docAnalyzer.py lists [directory]
		- Search: docAnalyzer.py search [directory] [term]

	Note that inputting '.' for the directory scans the current directory.

Outside Packages Used:
	python-docx
	matplotlib (https://matplotlib.org)

Known Bugs:
	- Search raises an unchecked exception if the .docx file is not readable
	  (such as with a temporary file). 