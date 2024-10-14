import math

def trap(B,h,b):
    cat = (B-b)/2
    l = math.sqrt((cat**2)+(h**2))
    Area = ((B+b)*h)/2
    per = B+b+cat+cat
    return A, p