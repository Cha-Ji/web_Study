# #Ex_1
# i = 1
# while i<101:
#     print(i)
#     i= i+1
#
# #Ex_2
# i = 100
# while i<=200:
#     if i %2 == 1:
#         print(i)
#     i+=1
#
# #Ex_3
# i = 200
# count=0
# while i<=600:
#     if i % 3 != 0:
#         count +=1
#         print(i,end=" ")
#     if count%8==0:
#         print()
#     i+=1
#
# #Ex_4
# i = 1
# total = 0
# while i<=10:
#     total +=i
#     i+=1
# print(total)
#
# #Ex_5
# i = 1000
# total = 0
# while i<=5000:
#     if i % 5 ==0:
#         total+=i
#     i+=1
#
# #Ex_6
# C = -20
# while C<=50:
#     F = C*9/5 + 32
#     print(F)
#     C+=2
#
# #Ex_7
# print("-"*60)
# print("%7s \t % 7s \t %7s \t %7s"%("cm","mm","m","inch"))
# print("-"*60)
# cm = 1
# while cm<=100:
#     mm=cm * 10.0
#     m= cm * 0.01
#     inch = cm * 0.3937
#     print("%7d \t %7.0f \t %7.2f \t %7.1f"%(cm,mm,m,inch))
#     cm+=2
#
# #Ex_8
# Eng = input("영어 문장을 입력해주세요 : ")
# index,count = 0,0
# Vowel = ['a','e','i','o','u']
# while index<len(Eng):
#     if Eng[index] in Vowel:
#         count+=1
#     index+=1
# print("모음의 개수 : %d"%count)
#
# #Ex_9
# total_odd = 0
# i = 300
# while i<=500:
#     if i % 2 == 1:
#         total_odd+=i
#     i+=1
# print(total_odd)
#
# #Ex_10
# dollar = 10
# while dollar<=100:
#     won = dollar*1158.93
#     euro = dollar*0.9
#     print("%3d달러 : %10.2f원 %5.2f유로"%(dollar,won,euro))
#     dollar+=10
#
# #Ex_11
# input_str = list(input("문장을 입력하세요. : "))
# i = 0
# while i<len(input_str):
#     if input_str[i]==" ":
#         input_str[i]="-"
#     i+=1
# for j in input_str:
#     print(j,end="")
