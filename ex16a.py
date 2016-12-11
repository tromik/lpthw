from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want to do that, hit CRTL-C (^C)."
print "If you do want that, hit ENTER."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodby!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
print "Closing the file..."
target.close()

target = open(filename)
contents = target.read()
print contents
print "Here are the contents of the file %r: \n%r" % (filename, contents)


print "And finally, we close it."
target.close()
