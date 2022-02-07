#program of string formatting
user="sovan"
str=f"hey {user} welcome"
print(str)
user="somi"
print(str)
name="josh"
greeting="you are {}"
greetnew=greeting.format(name)
print(greetnew)
name="bob"
greetnew=greeting.format(name)
print(greetnew)
welcome="hey {name} welcome to party"
greet=welcome.format(name="suman")
print(greet)