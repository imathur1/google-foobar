M = "15"
F = "5"
def answer(M, F):
    M = int(M)
    F = int(F)
    gen = 0
    
    while M != 1 or F != 1:

        if M % 2 == 0 and F % 2 == 0:
            return "impossible"
        
        if M == 1:
            gen += F - 1
            return str(gen)
        elif F == 1:
            gen += M - 1
            return str(gen)
        
        if M > F:
            if M % F == 0:
                return "impossible"
            div = M // F
            M -= F * div
            if M == 0:
                M = 1
                gen -= 1
            gen += div
            
        elif F > M:
            if F % M == 0:
                return "impossible"
            div = F // M
            F -= M * div
            if F == 0:
                F = 1
                gen -= 1  
            gen += div

        else:
            return "impossible"

    return str(gen)

print(answer(M, F))
