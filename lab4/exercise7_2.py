def my_sqrt(x,a=4.0,epsilon=0.00000001):
    x = 3.0
    y = (x + a/x) / 2
    while (abs(y-x)>epsilon):
        x = y
        y = (x + a/x) / 2
    return y
    
