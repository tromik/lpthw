def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "SUBSTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credits, type it in anyway
print "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "%d + (%d - (%d * (%d / 2))) = %d" % (age, height, weight, iq, (age + (height - (weight * divide(iq, 2)))))
print "35 + (74 - (180 * (50 / 2))) = %d" % (35 + (74 - (180 * (50 / 2))))
