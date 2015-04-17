"""Exercise 14.2. Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames; it should read the first file and write the contents into the second file (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced with the replacement string.
"""

import os
import sys
import string

def main():
    # Enter pattern string and replacement string
    pattern_string = sys.argv [1]
    replacement_string = sys.argv [2]

    #Open the file to read (fin) and the file to output to. Raise exceptions if there are problems.  If no output file has been created then create this.

    try:
       fin = open(sys.argv[3])
    except:
       print 'Something went wrong with opening the first file.'

    try:
       fout = open(sys.argv[4], 'w')
    except:
       print 'Something went wrong with opening the second file it has been created'
       fout = open('output.txt', 'w')

    #Read through the input file and replace any of the pattern  strings found with a replacement string.
    for line in fin:
       str(line)
       new_line = string.replace(line, pattern_string, replacement_string)
       fout.write(new_line)

    #Close the input file and the output file
    fin.close()
    fout.close()

if __name__ == "__main__":
    main()