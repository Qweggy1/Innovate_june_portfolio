from person import Person

liam = Person("liam", 31, "6'7''")

new_person = Person("Will", 31, "6'0''")

katy = Person("Katy", 30, "5'6''")

demi = Person("Demi", 29, "5'4''")

demi.set_hair("Red")

demi.get_hair()
#________________________________________________________________________________________
                    #/  Abstraction
# Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user. This is one of the core concepts of object-oriented programming (OOP) languages. That enables the user to implement even more complex logic on top of the provided abstraction without understanding or even thinking about all the hidden background/back-end complexity. Basically, Abstraction focuses on hiding the internal implementations of a process or method from the user. In this way, the user knows what he is doing but not how the work is being done.
#________________________________________________________________________________________
                    #! Inheritants
# Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class. It refers to defining a new class with little or no modification to an existing class. The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.
#________________________________________________________________________________________
                    #? Encapsulation
# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.
# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc. Encapsulation in Python describes the concept of bundling data and methods within a single unit. So, for example, when you create a class, it means you are implementing encapsulation. A class is an example of encapsulation as it binds all the data members (instance variables) and methods into a single unit.
#_________________________________________________________________________________________
                    #* Polymorphism
# The literal meaning of polymorphism is the condition of occurrence in different forms.
# Polymorphism is a very important concept in programming. It refers to the use of a single types of data such as method, operator or object to represent different types in different scenarios. It means that the same function name can be used for different types. This makes programming more intuitive and easier. Python uses two different class types in the same way. Example: you have to create a for loop that iterates through a tuple of objects. Next, you have to call the methods without being concerned about which class type each object is. We assume that these methods actually exist in each class.

# An analogy would be that although a truck and golf cart are two different vehicles (different objects in our case), we can drive them in the same way because they both have a gas pedal, brake, and steering wheel.
#_________________________________________________________________________________________
