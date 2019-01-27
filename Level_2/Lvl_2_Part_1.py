xs = [-1]

def answer(xs):
    biggest_negative = -1000
    output = 1

    if len(xs) == 1:
        return str(xs[0])
    
    positives = 0
    negatives = 0
    for i in xs:
        if i > 0:
            positives += 1
        if i < 0:
            negatives += 1
            
    if 0 in xs and positives == 1 and negatives == 1:
        return "0"
    
    if 0 in xs and positives == 1 and negatives == 0:
        return "0"
        
    if 0 in xs and positives == 0 and negatives == 1:
        return "0"
    
    for i in xs:
        if i < 0 and i > biggest_negative:
            biggest_negative = i
        
    for j in xs:
        if j == 0:
            pass
        else:
            output *= j
        
    if output < 0:
        output //= biggest_negative
        
    return str(output)

print(answer(xs))
