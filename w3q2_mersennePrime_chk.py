def is_prime(n):
    if n<=1:
        return False
    
    for i in range(2, (n//2)+1):
        if n%i==0:
            return False
    return True

def is_mersenne_prime(n):
    if not is_prime(n):
        return False
    
    #n=2^p - 1   => 2^p = n+1
    m=n+1        #where m = 2^p
    while m%2==0:
        m=m//2
    if m==1:
        return True
    else:
        return False
    
num=int(input("Enter  number to be checked: "))
if (is_mersenne_prime(num)):
    print(num, "is a Mersenne prime")
else:
    print(num, "is not a Mersenne prime")