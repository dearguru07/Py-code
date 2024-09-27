# def Prime(n):
#     tem=True
#     er=n//2
#     for i in range(2,er+1):
#         if n%i==0:
#             tem=False
#             break
#     if tem==True:
#         print('prime')    
#     else:
#         print('not prime')    
# n=int(input('enter a number'))        
# Prime(n)


# def Count(n):
#     countD=0
#     while n!=0:
#         n//=10
#         countD+=1
#     return countD
# n=int(input('enter a number'))    
# res=Count(n)
# print(res)


# def Poly(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n//=10
#     return rev
# n=int(input('enter a number'))    
# res=Poly(n)
# if res==n:
#     print('polyndrm')  
# else:
#     print('not polydrm')    


# def Reves(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     return rev
# n=int(input('enter a nuumber'))    
# res=Reves(n)
# print(res)


# def Fibb(n):
#     n1=int(input('enter a sr number'))
#     n2=int(input('enter a er number'))
#     for i in range(1,n+1):
#         print(n1)
#         n3=n1+n2
#         n1,n2=n2,n3
# n=int(input('enter a number'))        
# Fibb(n)    
    
    
# def countD(n):
#     count=0
#     while n!=0:
#         n//=10
#         count+=1
#     return count
# def Amstrng(n):
#     tem=n
#     sum=0
#     power=countD(n)
#     while n!=0:
#         rem=n%10
#         sum=(sum+rem**power)
#         n//=10
#     if tem==sum:
#         return True
#     else:
#         return False
# n=int(input('enter a number'))            
# float=Amstrng(n)
# if float==True:
#     print('amstrng')
# else:
#     print('not a amstrng')    


# def Leep(n):
#     if (n%400!=0 and n%100==0) or n%4==0:
#         print('leep year')
#     else:
#         print('not a leep year') 
# n=int(input('enter a number'))           
# Leep(n)        


# def reverse_string(s):
#     reversed_s = ''
#     for char in s:
#         reversed_s = char + reversed_s
#     return reversed_s
# input_string = input('enter a strg')
# reversed_string = reverse_string(input_string)
# print(reversed_string)
# if input_string==reversed_string:
#     print('poly')
# else:
#     print('not poly')



def Reverse(n):
    str=''
    for i in n:
        str=i+str
    return str
n=str(input('enter a string'))    
Reversed=Reverse(n)
print(Reversed)
if n==Reversed:
    print('polyndrome')
else:
    print('not a polyndrm')    