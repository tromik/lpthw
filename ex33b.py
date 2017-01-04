numbers = []

def whilelooper(times_to_loop, amount_to_increment):
    i = 0
    while i < times_to_loop:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + amount_to_increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

# call the new function
whilelooper(11, 2)
print "The numbers: "

for num in numbers:
    print num
