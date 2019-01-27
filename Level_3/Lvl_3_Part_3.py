def is_power2(a):
    a = int(a)
    return ((a & (a - 1)) == 0)

def answer(n):
    n = int(n)
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            if is_power2(n - 1) == True:
                n -= 1
            elif is_power2(n + 1) == True:
                n += 1
            else:
                trial1 = n + 1
                trial2 = n - 1
                t1 = 0
                t2 = 0
                
                while trial1 % 2 == 0:
                    trial1 //= 2
                    t1 += 1
                while trial2 % 2 == 0:
                    trial2 //= 2
                    t2 += 1
                    
                if t1 > t2:
                    n += 1
                else:
                    n -= 1
                              
        count += 1
    return count

print(answer("15"))

# evaluate adding all times solves test cases 1, 2, 3, 4, 6, 10
# find pattern to see when adding is better than subtracting
# 123
# 122, 61, 60, 30, 15, 16, 8, 4, 2, 1
# 124, 62, 31, 32, 16, 8, 4, 2, 1

# 369
# 368, 184, 92, 46, 23, 22, 11, 10, 5, 4, 2, 1
# 368, 184, 92, 46, 23, 24, 12, 6, 3, 2, 1

# 363
# 362, 181, 180, 90, 45, 44, 22, 11, 10, 5, 4, 2, 1

# 23
# 24 12 6 3 2 1

#124 - 62 31 
#122 - 61 becomes odd sooner!!!!?!??

