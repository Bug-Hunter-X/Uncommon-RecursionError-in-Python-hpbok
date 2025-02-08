def function(x):
    if x == 0:
        return 0
    else:
        return x + function(x - 1)