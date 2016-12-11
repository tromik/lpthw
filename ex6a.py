x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # string in a string 1 and 2

print x
print y

print "I said: %r." % x # string in a string 3
print "I also said: %r." % y # string in a string 4

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

print w + e
