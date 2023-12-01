# def fibinoci(n):    
#     if n<=0:
#         return None
#     elif n == 1 or  n==2:
#         return n-1
#     else:
#         return fibinoci(n-1) + fibinoci(n-2)


# n = int(input("Enter the no to find the factorial : - "))
# f =  fibinoci(n)
# if f is not None:
#     print(f"The {n} th fibinoci number is :- ",f)
# else:
#     print("invalid input please enter a posative integer greater than - 0") 

# def power(base,exponet):
#     if exponet == 0:
#         return 1
#     elif exponet > 0:
#         return base*power(base,exponet - 1)
#     else:
#         return 1 / base * power(base,exponet + 1)
# base = float(input('Enter the base:-'))
# n = float(input('Enter the exponent:-'))

# result = power(base,n)

# print("The result is :--",result)

def factoril(n):
    if n == 1:
        return 1 
    return n*factoril(n-1)

n = int(input("Enter the input :-"))
result = factoril(n)
print("The result is :---",result) 