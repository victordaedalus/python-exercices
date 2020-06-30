def algarism_sum(num1, num2):
    num1 = list(str(num1))
    num2 = list(str(num2))
    total = 0

    for alg in num1:
        total += int(alg)
    for alg in num2:
        total += int(alg)
    
    return total

numA = int(input('> '))
numB = int(input('> '))

print(algarism_sum(numA, numB))
