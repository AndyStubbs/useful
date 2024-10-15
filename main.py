from useful import useful


@useful
def cool(a="", b="", c=""):
	print( a + b + c )


print( "Welcome to the most powerful AI assitant in the world, better than ChatGPT" )
print( "Type in things below, enter nothing to stop" )
something = " "
while something != "":
	something = input( "Enter something: " )
	cool( something )