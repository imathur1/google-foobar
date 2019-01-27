total_lambs = 2
def answer(total_lambs):
    x = 0
    y = 1
    num = 1
    min_sum = 1
    max_sum = 1
    min_henchmen = 1
    max_henchmen = 1
    while min_sum < total_lambs:
        num *= 2
        if min_sum + num > total_lambs:
            value = total_lambs - min_sum
            if value >= (num / 2 + num / 4):
                min_sum += value
            else:
                break
        else:
            min_sum += num

        min_henchmen += 1

    while max_sum < total_lambs:
        alt = x + y
        
        if max_sum + alt > total_lambs:
            break
        else:
            max_sum += alt
            
        x = y
        y = alt
        max_henchmen += 1

    return max_henchmen, min_henchmen  
        
print(answer(total_lambs))

