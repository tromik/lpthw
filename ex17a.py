from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these on one line, how?
# in_file = open(from_file)
# indata = in_file.read()
in_file = open(from_file);indata = in_file.read()

print "Ready, hit ENTER to continue, CRTL-C to abort."
raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)
# Another way to write on one line
open(to_file, 'w').write(indata)

print "Alright, all done."

# out_file no longer exists, no need to close
# out_file.close()
in_file.close()
