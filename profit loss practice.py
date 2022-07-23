"""find largest number in three numbers"""

# a=int(input("enter the first nuber:"))
# b=int(input("enter the second nuber:"))
# c=int(input("enter the third nuber:"))
# max=a
# if a < b:
#     max=b
# if c > b:
#     max=c
# print(max) 


"""  swap two numbers """

# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# temp=a
# a=b
# b=temp
# print("value of a:",a)
# print("value of b:",b)
 
 
"""  leap or not """

# n=float(input("enter the number of year:")) 

# if (n % 400==0) and (n%100==0):
#     print("enter the leap year")
# elif(n % 4==0)and (n%100==0):
#     print("entered leap year")    
# else:
#     print("not a leap year")       

""" profit or loss  """
# cp=float(input("enter the cost price:"))
# sp=float(input("enter the seling price:"))
# if cp > sp:
#   amount=cp-sp
#   print("loss:" ,amount)
# else:
#   amount= sp-cp  
#   print("profit:" ,amount)    


""" simple interest """


# p=int(input("enter the total amount:"))
# t=float(input("enter the time in years:"))
# r=float(input("enter the rate of interest"))
# si= p*t*r/100
# print("enter the simple interest is:" , si)
# amount=si+p
# print("your amount is a:" ,amount)


""" calculate volume of cylinder"""

# r=float(input("enter the radious:"))
# h=float(input("enter the height:"))
# v=(3.14*r*r)*h
# print("enter the volume of cylinder:",v)
# cost=v/1000*40
# print("your cost is:" ,'Rs',cost)



""" area of circle"""
r=float(input("enter the radious:"))
PI=22/7
area=PI*r*r
print("enter the area of circle is:%.2f "%area)