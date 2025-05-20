#!/usr/bin/env python3
SIZES_LIST = ["Small", "Medium", "Large"]

class Coffee:

    def __init__(self, size, price):
        self.size = size
        self.price = price
    
    @property
    def size(self):
        return self._size
        
    @property
    def price(self):
        return self._price

    @size.setter
    def size(self, value):
        if value in SIZES_LIST:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
            
    @price.setter
    def price(self, value):
        if type(value) in (int, float):
            self._price = value
        else:
            raise ValueError("price must be a number")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self._price += 1