def function(x):
    total = 0
    if x > 0:
        for i in range(x + 1):
            total += i
    elif x < 0:
        for i in range(x, 1):
            total += i
    return total