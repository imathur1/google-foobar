data = [5, 10, 15, 10, 10]
n = 2

def answer(data, n):
    output = []

    for i in data:
        count = 0
        for j in data:
            if i == j:
                count += 1
        if count <= n:
            output.append(i)

    return output

print(answer(data, n))
