import math
def order_modulo(r, n):
    if math.gcd(r, n) !=1:
        return "Order does not exist, as r and n are not coprime"
    k=1
    val= r%n

    while val!=1:
        val=(val*r) % n
        k+=1
    return k
    
r=int(input("Enter the value of r: "))
n=int(input("Enter the value of n: "))
print("The order of" , r ,"modulo ",n,"is: ", order_modulo(r, n))