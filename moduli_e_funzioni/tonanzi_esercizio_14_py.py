import trapezio

b = int(input("inserire base minore: "))
B = int(input("inserire base maggiore: "))
h = int(input("inserire altezza: "))
print(f"area  e perimetro = {trapezio.trap(B,h,b)}")