#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:42:32 2019
Area do trapézio
@author: ghostborn67
"""

maior = float(input('Digite a base maior do trapézio em m: '))
menor = float(input('Digite a base menor do trapézio em m: '))
altura = float(input('Digite a altura do trapézio em m: '))

if maior > 0 and menor > 0:
    area = ((maior + menor) * altura) / 2
    print('A area do trapézio é de {}m²'.format(area))
else:
    print('Numero Invalidos.')
