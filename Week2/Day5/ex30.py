people = 30
cars = 40
buses = 15

if cars > people:
    print("We should take the cars.")
elif cars< people:
    print("we should not take the cars.")
else:
    print("we can't decide.")

if buses>cars:
    print("That's too many buses.")
elif buses<cars:
    print("Maybe could take the bus")
else:
    print("we still can't decide")

if people>buses:
    print("alright, let's just take the buses.")
else:
    print("Fine,let's stay home then.")