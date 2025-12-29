# multiple ineritance = when a child class is derived from more then one parent class

class Prey:

    def flee(self):
        print("This animal if flees")
class Predator:

    def  hunt(self):
        print("This animal is hunting")

class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Prey):
    def eat(self):
        print("This animal is eating carrot")

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
rabbit.eat()
hawk.hunt()
#fish.hunt(self=Predator)
#fish.flee(self=Prey)
#hawk.hunt(self=Prey)

# multiple inheritance = when a child class is derived from more than one parent class

#class Prey:

#    def flee(self):
#        print("This animal flees")

#class Predator:

#    def hunt(self):
#        print("This animal is hunting")

#class Rabbit(Prey):
#    pass

#class Hawk(Predator):
#    pass

#class Fish(Prey, Predator):
#    pass


#rabbit = Rabbit()
#hawk = Hawk()
#fish = Fish()

#rabbit.flee()
#hawk.hunt()
#fish.flee()
#fish.hunt()





































