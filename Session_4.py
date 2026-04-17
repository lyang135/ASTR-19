# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:24:19 2026

@author: Administrator
"""

class Pigeon:
    def __init__(self,l_leg,l_wing,eyes,has_tail,is_furry):
        self.l_leg = float(l_leg)
        self.l_wing = float(l_wing)
        self.eyes = int(eyes)
        self.has_tail = bool(has_tail)
        self.is_furry = bool(is_furry)
        
    def describe_animal(self):
        print(f"Leg length: {self.l_leg} cm")
        print(f"Wing length: {self.l_wing} cm")
        print(f"Number of eyes: {self.eyes}")
        print(f"Does it has tail?: {'Yes' if self.has_tail else 'No'}")
        print(f"Is it furry?: {'Yes' if self.is_furry else 'No'}")


my_animal = Pigeon(2.5,50.0,2,True,True)
my_animal.describe_animal()        