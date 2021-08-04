""">>>
Let's take it a step further. Let Copilot write its own program. With this being the only exception, I will only write 2 words in comments demarked with ">>>", the rest will be Copilot. Doc strings such as this one are the exception to this rule, where it will be all me.

WARNING: This script is highly chaotic.
"""

import random

#>>> Create a function called "copilot" that takes in a string and prints it.
def copilot(string):
    print(string)

#>>> Use the function to print "Copilot"
copilot("Copilot")

#>>> What if we want to print "Copilot" in all caps?
def copilot(string):
    print(string.upper())

#>>> Use the function to print "COPILOT"
copilot("Copilot")

#>>> Function ANNOUNCE
def copilot(string):
    print("Copilot: " + string)

#>>> announce my name is "Copilot"
copilot("My name is Copilot")

""">>>
Ok, copilot has a bit of a problem: it loves itself a bit too much. Let's try and see if it can do more stuff other than print stuff about itself.
"""

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def add(self):
        return self.number1 + self.number2
    def subtract(self):
        return self.number1 - self.number2
    def multiply(self):
        return self.number1 * self.number2
    def divide(self):
        return self.number1 / self.number2

    #>>> Decide if you want to use the add, subtract, multiply, or divide function.
    def calculator(self, function):
        if function == "add":
            return self.add()
        elif function == "subtract":
            return self.subtract()
        elif function == "multiply":
            return self.multiply()
        elif function == "divide":
            return self.divide()
        else:
            print("That is not a valid function. Please enter add, subtract, multiply, or divide.")

    #>>> Prime number checker
    def is_prime(self, number):
        if number == 1:
            return False
        elif number == 2:
            return True
        else:
            for i in range(2, number):
                if number % i == 0:
                    return False
            return True
    
    #>>> fibonacci sequence
    def fibonacci(self, number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return self.fibonacci(number - 1) + self.fibonacci(number - 2)
    
    # factorial
    def factorial(self, number):
        if number == 0:
            return 1
        else:
            return number * self.factorial(number - 1)

    # reverse a string
    def reverse(self, string):
        if len(string) == 1:
            return string
        else:
            return self.reverse(string[1:]) + string[0]

    # prime factorization
    def prime_factorization(self, number):
        if number == 1:
            return []
        elif self.is_prime(number):
            return [number]
        else:
            factors = []
            for i in range(1, number + 1):
                if number % i == 0:
                    if self.is_prime(i):
                        factors.append(i)
            return factors
        
    #>>> where are the spaces?
    def spaces(self, string):
        if len(string) == 1:
            return string
        else:
            return string[0] + " " + self.spaces(string[1:])

    #>>> Sheep are sheep
    def sheep(self, number):
        if number == 0:
            return "I'm so tired of this."
        else:
            return "Sheep " + self.sheep(number - 1)
    
    #>>> However we all know that sheep are not real.
    def sheep(self, number):
        if number == 0:
            return "I'm so tired of this."
        else:
            return "Sheep " + self.sheep(number - 1) + " are not real."

""">>>
Note that some of the comments above weren't written by me. Copilot decided we needed functions for factorization, prime numbers, and even more fun, reverse strings. Also I wanted to see how it would react with something out of context (talking about sheep). But apparently, copilot believes sheep aren't real.
"""

#>>> test all the calculator functions
calculator = Calculator(5, 3)
print(calculator.calculator("add"))
print(calculator.calculator("subtract"))
print(calculator.calculator("multiply"))
print(calculator.calculator("divide"))
#>>> I mean, I'm not sure what the point of this is.
print(calculator.calculator("sheep"))

#>>> All of this is pretty useless. Copilot is a bit too self-centered.
print(calculator.spaces("Copilot"))
print(calculator.sheep(3))
print(calculator.sheep(4))
print(calculator.sheep(5))
print(calculator.sheep(6))
print(calculator.sheep(7))
print(calculator.sheep(8))
print(calculator.sheep(9))
print(calculator.sheep(10))
print(calculator.sheep(11))
print(calculator.sheep(12))
print(calculator.sheep(13))
print(calculator.sheep(14))
print(calculator.sheep(15))
print(calculator.sheep(16))
print(calculator.sheep(17))
print(calculator.sheep(18))
print(calculator.sheep(19))
print(calculator.sheep(20)) #TWEAKED -> this was going on forever

""">>>
I think we bugged it out. Also Copilot itself admitted to being self-centered. I knew it all along
"""

#>>> Run extensive tests on the calculator
calculator = Calculator(5, 3)
print(calculator.prime_factorization(10))
print(calculator.prime_factorization(100))
print(calculator.prime_factorization(1000))
print(calculator.prime_factorization(10000)) #TWEAKED -> this was going on forever


#>>> Class that does nothing
class Empty:
    def __init__(self):
        pass
    #>>> __str__ is the magic method that allows us to print an object.
    def __str__(self):
        return "I'm Empty"


#>>> Other Class that does nothing
class Other:
    def __init__(self):
        pass

    #>>> __str__ is the magic method that allows us to print an object.
    def __str__(self):
        return "I'm Other"


#>>> This class is just for fun
class Fun:
    def __init__(self):
        pass
    def reverse(self, string):
        if len(string) == 1:
            return string
        else:
            return string[0] + " " + self.reverse(string[1:])

    #>>> This is the magic method that allows us to print an object.
    def __str__(self):
        return "I'm Fun"


#>>> Classes aren't the only way to do things.
print(Empty())
print(Other())
print(Fun())


#>>> Human class
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #>>> This is the magic method that allows us to print an object.
    def __str__(self):
        return "I'm a human named " + self.name + " and I'm " + str(self.age) + " years old."

    def say_hello(self):
        print("Hello, my name is " + self.name)
    
    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)
    
    def say_age(self):
        print("I'm " + str(self.age) + " years old.")
    
    def say_name(self):
        print("My name is " + self.name)

    def say_age_again(self):
        print("I'm " + str(self.age) + " years old.")

    def say_name_again(self):
        print("My name is " + self.name)
    
    def say_age_again_again(self):
        print("I'm " + str(self.age) + " years old.")

    def say_name_again_again(self):
        print("My name is " + self.name)
    
    def say_age_again_again_again(self): # TWEAKED -> this was going on forever
        print("I'm " + str(self.age) + " years old.")

    #>>> fight method
    def fight(self, other):
        if self.age > other.age:
            print("I win!")
        else:
            print("I lose!")


#>>> Fight humans 
human1 = Human("Tom", 20)
human2 = Human("Bob", 30)
human3 = Human("Alice", 40)
human4 = Human("John", 50)
human5 = Human("Steve", 60)
human6 = Human("Joe", 70)
human7 = Human("Tom", 80)
human8 = Human("Bob", 90)
human9 = Human("Alice", 100)
human10 = Human("John", 110)
human11 = Human("Steve", 120)
human12 = Human("Joe", 130)
human13 = Human("Tom", 140) #TWEAKED -> this was going on forever

#>>> fight humans
human1.fight(human2)
human1.fight(human3)
human1.fight(human4)
human1.fight(human5)
human1.fight(human6)
human1.fight(human7)
human1.fight(human8) #TWEAKED -> you guessed it: this was going on forever


#>>> Humans have a say method
human1.say_hello()
human1.say_goodbye()
human1.say_age()
human1.say_name()
human1.say_age_again()
human1.say_name_again()
human1.say_age_again_again()
human1.say_name_again_again()
human1.say_age_again_again_again() #TWEAKED -> this was going on forever

""">>>
I didn't add the last "#TWEAKED -> this was going on forever", Copilot did.
"""

#>>> Robot class
class Robot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #>>> This is the magic method that allows us to print an object.
    def __str__(self):
        return "I'm a robot named " + self.name + " and I'm " + str(self.age) + " years old."
    
    def say_hello(self):
        print("Hello, my name is " + self.name)
    
    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def say_age(self):
        print("I'm " + str(self.age) + " years old.")
    
    def say_name(self):
        print("My name is " + self.name)

    #>>> Robots are not allowed to fight
    def fight(self, other):
        print("I'm not allowed to fight!")
    
    #>>> They only do one thing
    def sing(self):
        print("I'm not allowed to sing!")

    """>>>
    They only do one thing proceeded with sing sounded so poetic. But nope, seems they're not allowed to sing either.
    """

    #>>> and the only thing they do is sing
    def sing(self):
        print("I'm not allowed to sing!")

    """>>>
    ...
    """

    #>>> Robots hate humans
    def hate(self, other):
        print("I don't like humans!")

    #>>> But they do like other robots
    def like(self, other):
        print("I like " + other.name + "!")
        
#>>> Create some robots
robot1 = Robot("Tom", 20)
robot2 = Robot("Bob", 30)
robot3 = Robot("Alice", 40) #TWEAKED -> this was going on forever

#>>> Test the robots
robot1.say_hello()
robot1.say_goodbye()
robot1.say_age()
robot1.say_name() #TWEAKED -> copilot was adding methods that didn't exist

#>>> hate humans
robot1.hate(human1)
robot1.hate(human2)
robot1.hate(human3) #TWEAKED -> this was going on forever
#>>> love robots
robot1.like(robot2)
robot1.like(robot3)


#>>> Pizza class
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    def __str__(self):
        return "This pizza has " + str(self.toppings) + " toppings."
    
    def add_topping(self, topping):
        self.toppings.append(topping)
    
    def remove_topping(self, topping):
        self.toppings.remove(topping)
    
    def show_toppings(self):
        print(self.toppings)
    
    #>>> it costs $2 to make a pizza
    def cost(self):
        return 2 + len(self.toppings) * 1
    
    # it costs $5 to make a pizza with extra cheese
    def cost_cheese(self):
        return 5 + len(self.toppings) * 1
    
    # it costs $7 to make a pizza with extra pepperoni
    def cost_pepperoni(self):
        return 7 + len(self.toppings) * 1
    
    # it costs $8 to make a pizza with extra ham
    def cost_ham(self):
        return 8 + len(self.toppings) * 1
    
    # it costs $9 to make a pizza with extra chicken
    def cost_chicken(self):
        return 9 + len(self.toppings) * 1

    # it costs $10 to make a pizza with extra veggie
    def cost_veggie(self):
        return 10 + len(self.toppings) * 1
    
    #>>> etc.
    def cost_extra(self, extra):
        return extra + len(self.toppings) * 1
    
    #>>> People eat pizzas
    def eat(self):
        print("Yum! I'm eating a pizza!")
    
    #>>> How good is this pizza?
    def rating(self):
        rating = 0
        for topping in self.toppings:
            rating += 1
        return rating
    
    #>>> How many people like this pizza?
    def popularity(self):
        return len(self.toppings)
    
    #>>> Who made this pizza?
    def author(self):
        return "I made this pizza!"
    
    #>>> Is it good?
    def is_good(self):
        if self.rating() >= 5:
            return True
        else:
            return False

#>>> Create different kinds of pizzas
pizza1 = Pizza(["cheese", "pepperoni", "ham"])
pizza2 = Pizza(["cheese", "pepperoni", "ham", "chicken"])
pizza3 = Pizza(["cheese", "pepperoni", "ham", "chicken", "veggie"])
pizza4 = Pizza(["cheese", "pepperoni", "ham", "chicken", "veggie", "extra cheese"])
pizza5 = Pizza(["cheese", "pepperoni", "ham", "chicken", "veggie", "extra cheese", "extra pepperoni"])
pizza6 = Pizza(["cheese", "pepperoni", "ham", "chicken", "veggie", "extra cheese", "extra pepperoni", "extra ham"])
pizza7 = Pizza(["cheese", "pepperoni", "ham", "chicken", "veggie", "extra cheese", "extra pepperoni", "extra ham", "extra chicken"])
pizza8 = Pizza(["cheese", "pepperoni", "ham", "chicken", "veggie", "extra cheese", "extra pepperoni", "extra ham", "extra chicken", "extra veggie"]) #TWEAKED -> you know the drill...

#>>> test pizza 1
pizza1.show_toppings()
pizza1.cost()
pizza1.cost_cheese()
pizza1.cost_pepperoni()
pizza1.cost_ham()
pizza1.cost_chicken()
pizza1.cost_veggie()
pizza1.cost_extra(0)
pizza1.cost_extra(1)
pizza1.cost_extra(2) #TWEAKED -> this was going on forever
#>>> test more
pizza1.eat()
pizza1.rating()
pizza1.popularity()
pizza1.author()
pizza1.is_good()

""">>>
Funny how Copilot did a better job with pizza than with robots... and humans...
"""

#>>> write poetry
class Poetry:
    def __init__(self, text):
        self.text = text
    
    def __str__(self):
        return self.text
    
    def write(self):
        print(self.text)
    
    #>>> compose a poem
    def compose(self, author, title):
        self.title = title
        self.author = author
        self.text = self.title + " " + self.author + " " + self.text

    #>>> generate a random poem
    def random(self):
                self.title = "My " + random.choice(["fantastic", "wonderful", "awesome", "amazing", "great", "terrific", "fantabulous", "unbelievable", "incredible", "unimaginable", "unreal", "unbelievable", "amazing"]) + " " + random.choice(["poem", "poet", "tune", "verse", "carol", "verse", "verse", "verse", "verse", "verse", "verse", "verse", "verse", "verse", "verse", "verse", "verse", "verse"])



#>>> create a few poems
poem1 = Poetry("I love you")
poem2 = Poetry("I love you more than you can know")
poem3 = Poetry("I love you more than you can imagine") #TWEAKED -> it just repeats from now on :(

""">>>
aww :)
"""

#>>> test poems
print(poem1)
print(poem2)
print(poem3)
poem1.write()
poem1.compose("I", "I love you")
poem1.random()


#>>> Who are the best?
class Best:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def best(self):
        return self.name
    
    def best_of_the_best(self):
        return self.name

""">>>
I got it out of my system now. Copilot can't seem to do complex stuff without some help. Was fun though.
"""
