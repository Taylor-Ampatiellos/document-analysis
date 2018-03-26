Program: docAnalyzer.py
Creator: Taylor Ampatiellos

How to Use:
	This program has two current functions:
		- The first function, accessed with the "graphs" argument, scans a given 
		  directory for .docx files then returns two bar graphs:
		  	 - A word-length frequency bar graph, where the x-axis is 
		  	   length in letters and the y-axis is the number of times 
		  	   a word of that length appears throughout the scanned documents.
		  	 - A letter frequency bar graph, where the x-axis is each letter
		  	   of the English alphabet, and the y-axis is the number of times
		  	   the letter appears throughout the scanned documents.
		  Note that the second graph is not shown until the first graph
		  is closed.
		- The second function, accessed with the "search" argument, scans a given 
		  directory for .docx files and returns a list of files containing
		  the given search term.

Syntax:
	The program takes 2 or 3 arguments, depending on the intended function.
		- Graphs: docAnalyzer.py graphs [directory]
		- Search: docAnalyzer.py search [directory] [term]

	Note that inputting '.' for the directory scans the current directory.

Outside Packages Used:
	python-docx
	matplotlib (https://matplotlib.org)
	  
Planned Changes:
	- Make length and letter frequency graphs display at the same time.
	- Display counts above graph bars 
	  (i.e. "43,251" above the bar for the letter 'e').
	- Add options for other kinds of graphs, 
	  such as a pie chart for letter frequency.
	- Improve readability of output from "search" argument,
	  including outputting the full path to each file. 
