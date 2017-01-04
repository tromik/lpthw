numbers = []

def whilelooper(times_to_loop):
    i = 0
    while i < times_to_loop:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

# call the new function
whilelooper(11)
print "The numbers: "

for num in numbers:
    print num
