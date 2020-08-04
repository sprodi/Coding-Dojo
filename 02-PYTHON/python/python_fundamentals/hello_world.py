# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Sean"
print( "Hello", name )	# with a comma
print( "Hello"+ name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 27
print( "Hello", name )	# with a comma
print( "Hello"+ str(name) )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string

# NINJA BONUS. Spend a few minutes playing around with other string methods to see what's out there!
fave_food1 = "chicken"
fave_food2 = "burgers"
print( "I love to eat %s and %s." % (fave_food1, fave_food2)) # with .format()

fave_food1 = "pizza"
slices = 4
print( "I love to eat %d slices of %s." % (slices, fave_food1)) # with an f string

