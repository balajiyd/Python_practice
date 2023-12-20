import math

def lcm(x,y):
    return x*y // math.gcd(x,y)

def gcd(x,y):
    return math.gcd(x,y)

num1 = 12
num2 = 9

lcm_r = lcm(num1,num2)
gcd_r = gcd(num1, num2)
print("The LCM of",num1,"and",num2,"is", lcm_r)
print("The GCD of",num1,"and",num2,"is", gcd_r)
