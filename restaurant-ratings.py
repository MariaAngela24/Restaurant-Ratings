# your code goes here
import sys

alphabetical_ratings = {}

filename = sys.argv[1]
for lines in open(filename):
    lines_clean = lines.rstrip()
    words = lines_clean.split(':')
    alphabetical_ratings[words[0]] = words[1]

for restaurant, rating in sorted(alphabetical_ratings.items()):
    print "{} is rated at {}.".format(restaurant, rating)
