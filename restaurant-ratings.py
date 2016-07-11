# your code goes here
import sys

alphabetical_ratings = {}

filename = sys.argv[1]
for lines in open(filename):
    #lines_clean = lines.rstrip()
    words = lines.split('\n')


    #strip by line
    #split by colon
    #move to dictionary


    for word in words:
        print word
