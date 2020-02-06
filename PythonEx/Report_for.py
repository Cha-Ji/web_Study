# #Ex_1
# for i in range(100):
#     print("안녕!")
#
# #Ex_2
# for i in range(100):
#     print("%d" %(i+1))
#
# #Ex_3
# for i in range(1,100,2):
#     print("%d" %(i))
#
# #Ex_4
# for i in range(1,101):
#     if i%2==0:
#         print("%d" %(i))
#
# #Ex_5
# for i in range(1,1000):
#     if i%5==0:
#         print("%d" %i)
#
# #Ex_6
# count = 1
#
# for i in range(1,1001):
#     if i % 3==0:
#         print("%d"% i,end=" ")
#
#         if count%10 == 0:
#             print()
#
#         count = count + 1
#
# #Ex_7
# n = int(input("n을 입력하세요 : "))
#
# print("%d의 배수"%n)
# for i in range(100,201):
#     if i % n == 0:
#         print("%d"%i)
#
# #Ex_8
# sum = 0
#
# for i in range(1,10):
#     sum = sum + i
# print("합계 : %d"%sum)
#
# #Ex_9
# sum = 0
# for i in range(200,301):
#     if i % 2 == 1:
#         sum = sum+i
#
# print("200~300의 홀수 합계 : %d"%sum)
#
# #Ex_10
# sum = 0
# for i in range(500,1001):
#     if i % 3 !=0:
#         sum = sum + i
#
# print("500~1000의 3의 배수가 아닌 수의 합계 : %d"%sum)
#
# #Ex_11,12
# word = input("영어 문장을 입력하세요")
#
# for i in word:
#     print(i)
#
# #Ex_13
# phone = input("하이픈(-)을 포함한 휴대폰 번호를 입력하세요:")
#
# for x in phone:
#     if x != "-":
#         print("%s" %x,end="")
#
# #Ex_14
# phone = input("하이픈(-)을 뺀 11자리의 휴대폰 번호를 입력하세요:")
#
# number =""
# for i in range(0,11):
#     if i==2:
#         number = number + (phone[2]+"-")
#     elif i == 6:
#         number = number + (phone[6]+"-")
#     else:
#         number = number + phone[i]
#
# print(number)
#
# #Ex_15
# print("-"*30)
# print("%7s \t % 7s" % ("섭씨","화씨"))
# print("-"*30)
#
# for c in range(-20,31,5):
#     f = c* 9.0/5.0 + 32.0
#     print("%8d \t %8.1f"%(c,f))
#
# #Ex_16
# print("-"*30)
# print("%7s \t %7s"%("인치","센티미터"))
# print("-"*30)
#
# for inch in range(10,51,5):
#     cm = inch*2.54
#     print("%8d \t %8.2f"%(inch,cm))
#
# print("-"*30)
#
# #Ex_17
# print("-"*30)
# print("%7s \t %7s"%("마일","킬로미터"))
# print("-"*30)
#
# for mile in range(10,81,10):
#     km = mile * 1.609
#     print("%8d \t %8.2f"%(mile,km))
#
# print("-"*30)
#
# #Ex_18
# print("-"*60)
# print("%7s \t % 7s \t %7s \t %7s"%("cm","mm","m","inch"))
# print("-"*60)
#
# for cm in range(1,100,2):
#     mm=cm * 10.0
#     m= cm * 0.01
#     inch = cm * 0.3937
#     print("%7d \t %7.0f \t %7.2f \t %7.1f"%(cm,mm,m,inch))
#
# #Ex_19
# print("-"*60)
# print("%7s \t %7s \t %7s \t %7s"%("킬로그램","그램","파운드","온스"))
# print("-"*60)
#
# for kg in range(10,201,5):
#     g = kg * 1000
#     pound = kg * 2.204623
#     ounce = kg * 35.273962
#     print("%8d \t %8d \t %8.1f \t %8.1f"%(kg,g,pound,ounce))
#
# print("-"*60)
#
# #Ex_20
# number = input("숫자를 입력하세요 : ")
#
# total = 0
#
# for a in number:
#     a = int(a)
#     if a%2 == 1:
#         total = total + 1
#
# print("입력된 숫자 중 홀수의 개수 : %d 개"% total)
#
# #Ex_21
# for i in range(1,11):
#     print("%10s"%("*"*i))
#
# #Ex_21_2
# for i in range(1,11):
#     for j in range(10,i,-1):
#         print(" ",end="")
#     for k in range(0,i):
#         print("*",end="")
#     print()
#
# #Ex_22
# a = 2
#
# for b in range(1,10):
#     c = a*b
#     print("%d x %d = %d"%(a,b,c))
#
# #Ex_23
# for a in range(2,10):
#     for b in range(1,10):
#         c = a*b
#         print("%d x %d = %d"%(a,b,c))
#
# #Ex_24
# n = int(input("수를 입력해주세요 : "))
#
# for a in range(2,n+1):
#     prime_yes = True
#     for i in range(2,a):
#         if a%i == 0:
#             prime_yes = False
#             break
#     if(prime_yes):
#         print(a)
