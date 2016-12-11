name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_metric = height * 2.54 # 1 inch is 2.54 cm
weight = 180 # lbs
weight_metric = weight / 2.2 # 1 kg is 2.2 pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

print "His height in centimeters is %d" % height_metric
print "His weight in kilograms is %d" % weight_metric

# python formats
# d	Signed integer decimal.
# i	Signed integer decimal.
# o	Unsigned octal.	(1)
# u	Unsigned decimal.
# x	Unsigned hexadecimal (lowercase).	(2)
# X	Unsigned hexadecimal (uppercase).	(2)
# e	Floating point exponential format (lowercase).
# E	Floating point exponential format (uppercase).
# f	Floating point decimal format.
# F	Floating point decimal format.
# g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
# G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
# c	Single character (accepts integer or single character string).
# r	String (converts any python object using repr()).	(3)
# s	String (converts any python object using str()).	(4)
