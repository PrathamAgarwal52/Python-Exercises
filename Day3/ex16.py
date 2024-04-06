from sys import argv
script, filename = argv
print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL- C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()
#Chatting in terminal
#python ex16.py test.txt
#We're going to erase 'test.txt'.
#If you don't want that, hit CTRL- C (^C).
#If you do want that, hit RETURN.
#?Traceback (most recent call last):
#  File "C:\Users\lenovo\dei\Day3\ex16.py", line 7, in <module>
#    input("?")
#KeyboardInterrupt
#PS C:\Users\lenovo\dei\Day3> 
#PS C:\Users\lenovo\dei\Day3> python ex16.py test.txt
#We're going to erase 'test.txt'.
#If you don't want that, hit CTRL- C (^C).
#If you do want that, hit RETURN.
#?
#Opening the file...
#Truncating the file. Goodbye!
#Now I'm going to ask you for three lines.
#line 1: hello ji
#line 2: how are you
#line 3: tell me what we are going to do
#I'm going to write these to the file.
#And finally, we close it.