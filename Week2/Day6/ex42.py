## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is a Animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has a name
        self.name = name

## cat is a animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has a name
        self.name = name

## person is a object
class Person(object):
    def __init__(self, name):
        ## person has a name
        self.name = name

        ## Person has- a pet of some kind
        self.pet = None
##Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        #calling a function from its parent class
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## fish is a object
class Fish(object):
    pass

## salmon is a fish
class Salmon(Fish):
    pass

## halibut is a fish
class Halibut(Fish):
    pass


## rover is- a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## marry is a person
mary = Person("Mary")

## mary has a pet named satan
mary.pet = satan
## frank is a employee
frank = Employee("Frank", 120000)

## frank has a pet named rover
frank.pet = rover

## flipper is a fish
flipper = Fish()
## crouse is a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()