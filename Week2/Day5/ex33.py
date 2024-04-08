
numbers = []
def while_loop_checking(num,i):
        j = 0
        while j < num:
            print ("At the top i is %d" % i)
            numbers.append(j)

            j = i + j
            print ("Numbers now: ", numbers)
            print ("At the bottom i is %d" % i)
num = int(input("tell me the number:"))
increament = int(input("tell me the increament:"))
while_loop_checking(num,increament)
print ("The numbers: ")

for num in numbers:
    print (num)