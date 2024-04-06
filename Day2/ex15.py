from sys import argv

script, filename = argv

txt = open(filename)
print ("Here's your file %r:" % filename)
print (txt.read())

print ("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())


#chatting with terminal
#python ex15.py ex15_sample.text
#Here's your file 'ex15_sample.text':
#This is stuff I typed into a file.
#It is really cool stuff.
#Lots and lots of fun to have in here.
#Type the filename again:
#> ex15_sample.text
#This is stuff I typed into a file.
#It is really cool stuff.
#Lots and lots of fun to have in here.'''

#we can also use filename.close() to close the file but in this case it is automatically closed
#example:in this we hav eto close the path.... 
#file_path = 'path_to_your_text_file.txt'  # Replace 'path_to_your_text_file.txt' with the actual path to your file
#file = open(file_path, 'r')  # Open the file
#file_contents = file.read()  # Read the contents of the file
#file.close()