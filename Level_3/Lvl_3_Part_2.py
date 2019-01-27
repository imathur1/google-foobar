start = 17 # 18 # 4 # 4
length = 4 # 143 # 3 # 7

def answer(start, length):
    output = 0
    alt = length
    
    while length > 0:
        for i in range(1, length + 1):
            output ^= start
            start += 1
    
        start += alt - length
        length -= 1
          
    return output

def no(start, length):
    output = 0
    alt = length
    
    while length > 0:

        value = length
        new = start
        
        # Even Even
        if new % 2 == 0 and (new + value - 1) % 2 == 0:
            output ^= (new + value - 1)
            value -= 1
            if (value - 2) % 4 == 0 or (value - 2) == 0:
                output ^= 1

        # Even Odd
        elif new % 2 == 0 and (new + value - 1) % 2 != 0:
            if (value - 2) % 4 == 0 or (value - 2) == 0:
                output ^= 1

        # Odd Even  
        elif new % 2 != 0 and (new + value - 1) % 2 == 0:
            output ^= new
            output ^= (new + value - 1)
            new += 1
            value -= 2
            if (value - 2) % 4 == 0 or (value - 2) == 0:
                output ^= 1

        # Odd Odd
        else:
            output ^= new
            new += 1
            value -= 1
            if (value - 2) % 4 == 0:
                output ^= 1

        start += alt
        length -= 1
          
    return output

print(answer(start, length))
print(no(start, length))
