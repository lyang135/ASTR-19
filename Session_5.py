# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:32:31 2026

@author: Administrator
"""

import numpy as np

def main():
    x_values = np.linspace(0, 2*np.pi, 1000)
    sin_values = np.sin(x_values)
    
    for x, s in zip(x_values, sin_values):
        print(f"{x:10.4f},{s:10.4f}")
        
if __name__ == "__main__":
    main()