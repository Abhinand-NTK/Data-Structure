# #Multi Dimamentional List

# List = [[1,2],[2,3]]

# print(List[1][1])

# lst = [1,2,3,4,5,6,7]

# print(lst[-1])
# print(len(lst))

# string = input("Enter elements (Space-Separated): ")
 
# # split the strings and store it to a list
# lst = string.split()

# print(string)
# print('The list is:', lst)   # printing the list


# n = int(input("Enter the size of list : "))
# lst = list(map(int, input("Enter the integer\
# elements:").strip().split()))[:n]

# print('The list is:', lst) 

# n = int(input("Enter the number of  input:--"))
# lst = list(map(int,input("Enter the input values:-").strip().split()))[:4]


# lst = []

# lst.extend([2,4,56,7,3])

# lst.remove(2)
# print(lst[::-1])

result = [i**2 for i in range(1,11) if i % 2 == 1]
print(result)

s = "Abhinand"
upper = lambda res:s.upper()
print(upper(s))

format_of_numeric = lambda num: "integer" if isinstance(num,int) else "floating value"

print(format_of_numeric(7.6))

cube = lambda x:x*x*x 
print(cube(3))

is_list = [lambda arg=x:arg*10 for x in range(1,5) ]

for i in is_list:
    print(i())



sentence = "Abhiannd!"
vowels = [char for char in sentence if char.lower() in 'aeiou']
print(vowels)

sentence = "Abhiannd!"
res = [char for char in sentence if char.lower() in 'aeiou']
print(res)

limit = 20

Prime = [x for x in range(2,limit) if all(x % i != 0 for i in range(2,int((x**.5)+1)))]

print("The proime no is the result is",Prime)


max = lambda x,y : x if x > y else y

print(max(3,4))

lst = [3,35,6,6,2,2,4,34,34,4,5,6]

allelements = list(map(lambda x : x*2,lst))

print(allelements)

ls = [i*2 for i in lst]

print(ls)

from functools import reduce
s = ["The world is nor enough for me" ,"", "brillent"]
res = reduce(lambda x,y :x+y,s )
print(res)

MAX = 1000


