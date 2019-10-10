import math

def is_approx(value, comparision=0):
    diff = abs(value-comparision)
    if comparision !=0:
        error = diff/max(abs(value),abs(comparision))
        return error<0.01
    else:
        return diff<0.001
        
x = input("please enter a number: ")
x = float(x)
print("close to zero? ", is_approx(x))
print("close to Pi? ", is_approx(x, math.pi))
