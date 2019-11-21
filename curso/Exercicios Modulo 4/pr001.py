#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 09:27:39 2019
@author: ghostborn67
"""

a = [1, 0 , 5, -2, -5, 7]
soma = a[0] + a[1] + a[5]
print(f'A soma foi de {soma}')
a.insert(4, 100)
for i in a:
    print(i)
