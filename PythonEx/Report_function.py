# #Ex_1
# def hello():
#     print("안녕하세요!")
#
# hello()
# hello()
# hello()
#
# #Ex_2
# def hello(name):
#     print("%s님 반갑습니다!"%name)
#
# hello("안지영")
# hello("홍지수")
# hello("황동진")
#
# #Ex_3
# def my_func(food):
#     for x in food:
#         print(x)
#
# fruits = ["오렌지","바나나","파인애플"]
#
# my_func(fruits)
#
# #Ex_4
# def my_func(x):
#     return x*x
#
# print(my_func(3))
# print(my_func(5))
# print(my_func(7))
#
# #Ex_5
# def even_odd(n):
#     if n%2==0:
#         print("%d -> 짝수"%n)
#     else:
#         print("%d -> 홀수"%n)
#
# even_odd(22)
# even_odd(37)
#
# #Ex_6
# def sum(start,end):
#     total = 0
#     for i in range(start,end+1):
#         total = total + i
#     print("%d ~ %d의 정수의 합계 : %d"%(start,end,total))
#
# sum(1,10)
# sum(100,200)
# sum(200,300)
#
# #Ex_7
# def inch2cm(inch):
#     cm = inch * 2.54
#     return cm
#
# num = int(input('인치를 입력하세요 : '))
# result = inch2cm(num)
# print("%d inch => %.2f cm"%(num,result))
#
# #Ex_8
# def besu5(n):
#     if n % 5 == 0:
#         rel = True
#     else:
#         rel = False
#     return rel
# num = int(input("양의 정수를 입력하세요 :"))
# result = besu5(num)
#
# if result == True:
#     print("%d -> 5의 배수이다."%num)
# else:print("%d-> 5의 배수가 아니다."%num)
#
# #Ex_9
# def sum_besu3(n):
#     sum = 0
#     for i in range(1,n+1):
#         if i %3 == 0:
#             sum = sum+i
#
#     return sum
# num = int(input("양의 정수를 입력하세요 : "))
# result = sum_besu3(num)
#
# print("1 ~ %d 까지의 3의 배수의 합 : %d"%(num,result))
#
# #Ex_10
# def cir_area(radius):
#     area = radius * radius * 3.14
#     return area
#
# def cir_circum(radius):
#     circum = 2*3.14*radius
#     return circum
#
# r = float(input("반지름을 입력하세요:"))
# a = cir_area(r)
# b = cir_circum(r)
# print("원의 면적 : %.2f, 원주의 길이 :%.2f"%(a,b))
