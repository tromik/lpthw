def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): # FIXED missing colon
    """Prints the first word after popping it off."""
    word = words.pop(0) # FIXED replaced 'poop' with 'pop'
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # FXIED missing closing paran
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 # FIXED assuming division was wanted, replace '\' with '/''
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # FIXED replace '==' with '-' and 'start-point' with 'start_point'

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point) # FIXED missing closing paran, fixed typo in start_point


sentence = "All god\tthings come to those who weight."

words = break_words(sentence) # FIXED removed reference to ex25
sorted_words = sort_words(words) # FIXED removed reference to ex25

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) # FIXED removed '.' from beginning of line
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence) # FIXED removed reference to ex25
print sorted_words # FIXED replaced 'prin' with 'print'

print_first_and_last(sentence) # FIXED typo

print_first_and_last_sorted(sentence) # FIXED removed line indent, function name typo, function param typo
