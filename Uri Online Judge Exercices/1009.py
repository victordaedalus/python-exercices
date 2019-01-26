# Imports

# Variables 
name = str
sal = float
sell = float

# Execution
name = input()
sal = float(input())
sell = float(input())
comit = ((sell / 100) * 15) + sal
print('TOTAL = R$ {:0.2f}'.format(comit))
