
# x = 6
# y = 2
# print(x ** y)
# print(x // y)

# x = 0
# y = 0.6
# print(x and y)

# x = 100
# y = 50
# print(x and y)

# print(-18 // 4)

# y = 10
# y+=2
# x=y
# print(x)

# print(2%6)
# x=10
# y=50
# if x**2>=100 and y<100:
#     print(x,y)

# print(2 ** 3 ** 2)

# print(36 // 4)

# for num in range(1,11):
#     print(num)

# num=1
# while num<=10:
#     print(num)
#     num+=1

# row=6
# for i in range(1,row+1,1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print("")

# number=int(input('Enter the number:'))
# x=sum(range(1,number+1,1))
# print(x)

# s=0
# num=int(input('Enter the number:'))
# for i in range(1,num+1,1):
#     s+=i
# print("\num")
# print(s)


# n=3
# for i in range(1,11,1):
#     product=n*i
#     print(product)

# numbers=[12,23,400,450,390,34,56]
# for i in numbers:
#     if i>500:
#         break
#     elif i>150:
#         continue
#     elif i%5==0:
#         print(i)




# numbers = [12, 75, 150, 180, 145, 525, 50]
# # iterate each item of a list
# for item in numbers:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     # check if number is divisible by 5
#     elif item % 5 == 0:
#         print(item)

# for i in range(5):
#     print(i)
# else:
#     print('done!!')

# start=25
# end=60
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#             print(num)


# num1,num2=0,1
# for i in range(10):
#     print(num1,end="  ")
#     res=num1+num2
#     num1=num2
#     num2=res

# num=6
# factorial=1
# if num<0:
#     print('factorial does not exist for negative numbers')
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(factorial)


# num=234567
# reverse_num=0
# while num>0:
#     reminder=num%10
#     reverse_num=(reverse_num*10)+reminder
#     num=num//10
# print(reverse_num)



# for i in range(9):
#     if i < 5:
#         for j in range(i + 1):
#             print("*", end=" ")
#     else:
#         for l in range(9 - i):
#             print("*", end=" ")
#     print()

# rows = 5
# for i in range(1, rows + 1):
#     print('*' * i)

# for i in range(rows - 1, 0, -1): 
#     print('*' * i)


# rows = 5
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))

# for i in range(rows - 1, 0, -1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))
# import datetime
# x=datetime.datetime.now()
# print(x)

# import datetime
# x=datetime.datetime.now()
# print(x.month)
# print(x.strftime("%B"))

# import math
# x=math.sqrt(49)
# print(x)

# import math
# x=math.ceil(2.6)
# y=math.floor(2.6)
# print(x)
# print(y)

# import re
# text = "The quick brown fox jumps over the lazy dog."
# new_text = re.sub(r'fox', 'cat', text)
# print(new_text)

# string = "apple,banana,cherry,date"
# fruits = re.split(',', string)
# print(fruits)


# import re
# txt="i have 69 phones"
# x=re.findall("\d",txt)
# print(x)

# list1=[1,2,3,4,5,6,7]
# list2=[8,9,10,11,12,13,14]
# res=list()
# odd_elements=list1[1::2]
# print(odd_elements)

