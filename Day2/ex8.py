formatter = "%r %r %r %r"
print (formatter % (1, 2, 3, 4))#numbers
print (formatter % ("one", "two", "three", "four")) #strings
print (formatter % (True, False, False, True))#booleans
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % ("I had this thing.","That you could type up right.","But it didn't sing.","So I said goodnight."))
#output gives two types of quotes because there is ' in the don't so it have to show it