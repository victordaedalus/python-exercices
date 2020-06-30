def prime_amount(num):
    count = 0
    for x in range(1, num + 1):
        if x == 2 or x == 3 or x == 5 or x == 7 or x == 11:
            count += 1
        elif x != 1 and x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0 and x % 11 != 0:
            count += 1
    return count


print(prime_amount(11)) 