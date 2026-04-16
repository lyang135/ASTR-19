# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:38:27 2026

@author: Administrator
"""

def f(x):
    return x**3+8

def main():
    result = f(9)
    print(f"f(9) is equal to {result}")
    
    if result > 27:
        print("YAY")
    
if __name__ == "__main__":
    main()