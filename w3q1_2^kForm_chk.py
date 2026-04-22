def is_form_2k(n):
    temp=n
    if n<=0:
        return False
    while n%2==0:
        n=n//2
    if n==1:
        print(temp, "is in the form of 2^k")
    else:
        print(temp, "is not in the form of 2^k")
    
num=int(input("Enter a number to be checked: "))
is_form_2k(num)