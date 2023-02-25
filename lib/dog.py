#!/usr/bin/env python3

class Dog:
    # Class body goes here

    #Instance method definition
    #By defining bark() within the Dog class, 
    #bark becomes a method of all instances of Dogs
    def bark(self): # this is instance method
        print('Woof!')
    def sit(self):
        print('The dog is sitting.')

# dot notation to access 
# the variable or functino defined inside an object
# instance variables are called attributes
# instance functions are called methods
# if Dog class wasn't provided attributes or methods such as bark,
# it has many by default! such as __dir__()
fido = Dog() # 1st instance of Dog
fido.bark() # Dog object knows how to bark
fido.sit()

snoopy = Dog() # 2nd instance of Dog
snoopy.bark() # Dog object knows how to bark too

# fido.sleep() 
# returns AttributeError: 'Dog' object has no attribute 'sleep'
# 'Dog' object doesn't have sleep attribute defined

# bark() 
# returns NameError: name 'bark' is not defined
# can't call bark without fido
