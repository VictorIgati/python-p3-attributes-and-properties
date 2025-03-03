#!/usr/bin/env python3
#/python-p3-attributes-and-properties/lib/dog.py
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.set_name(name)
        self.set_breed(breed)
   

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            return  # Prevent setting invalid name
    name = property(get_name, set_name) 

    def validate_name(self, name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        return False  # Do not set default name if validation fails

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return False  # Do not set default breed if validation fails
        self._breed = breed
      

    def validate_breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        return False  # Do not set default breed if validation fails
        
    breed = property(get_breed, set_breed)  

    def __str__(self):
        return f"{self._name} is a {self._breed}"         


dog1 = Dog()
print(dog1)
