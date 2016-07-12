# your code goes here
import sys

alphabetical_ratings = {}

filename = sys.argv[1]
for line in open(filename):
    clean_line = line.rstrip()

    #words = clean_line.split(':')
    #alphabetical_ratings[words[0]] = words[1]

    restaurant, rating = clean_line.split(':')
    alphabetical_ratings[restaurant] = rating

    #dictionary[key] = value

for restaurant, rating in sorted(alphabetical_ratings.items()):
                          # [(k,v), (k,v)]
    print "{} is rated at {}.".format(restaurant, rating)
