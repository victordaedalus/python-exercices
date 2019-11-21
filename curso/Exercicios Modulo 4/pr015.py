"""
Vetor com 20 elementos e eliminar elementos repetidos da lista.
author:ghostborn67
"""
# Var
vetor = []
check = []

# Run
for i in range(20):
    vetor.append(int(input(f'{i + 1}° &> ')))

for i in vetor:
    if i in check:
        pass
    else:
        if vetor.count(i) > 1:
            check.append(i)

vetor = set(vetor)
vetor = list(vetor)
for i in check:
    vetor.remove(i)

print(vetor)
