from sys import argv

script, user_name = argv
prompt = '> '

print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = input(prompt)

print ("Where do you live %s?" % user_name)
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print ("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))
#chatting in command prompt
#python ex14.py Pratham
#Hi Pratham, I'm the ex14.py script.
#I'd like to ask you a few questions.
#Do you like me Pratham?
#> yuppsss!!!
#Where do you live Pratham?
#> Agra
#What kind of computer do you have?
#> Laptop With 8Gb Ram

#Alright, so you said 'yuppsss!!!' about liking me.
#You live in 'Agra'. Not sure where that is.
#And you have a 'Laptop With 8Gb Ram' computer. Nice.