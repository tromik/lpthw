numbers = []

def forlooper(times_to_loop):
    i = 0
    for i in range(0, times_to_loop):
        print "At the top i is %d" % i
        numbers.append(i)
        # this incrementer is no longer needed, for loop auto increments by 1
        # i = i + amount_to_increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

# call the new function
forlooper(11)
print "The numbers: "

for num in numbers:
    print num
