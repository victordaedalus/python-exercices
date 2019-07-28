"""
Calcular qual numero é divisivel pelos numeros de 1 a 10 sem sobrar resto
authon:ghostborn67

(num % 1 == 0) and (num % 2 == 0) and (num % 3 == 0) and (num % 4 == 0) and
(num % 5 == 0) and (num % 6 == 0) and (num % 7 == 0) and (num % 8 == 0) and
(num % 9 == 0) and (num % 10 == 0)
"""

num = 10
while True:
    if num % 1 == 0:
        if num % 2 == 0:
            if num % 3 == 0:
                if num % 4 == 0:
                    if num % 5 == 0:
                        if num % 6 == 0:
                            if num % 7 == 0:
                                if num % 8 == 0:
                                    if num % 9 == 0:
                                        if num % 10 == 0:
                                            print(
                                                '{} é o numero escolhido.'
                                                .format(num))
                                            break

    print('{} não é.'.format(num))
    num += 1
