# #Ex_1
# color = ["red","green","blue","black","white"]
#
# print(color[0])
# print(color[4])
# print(color[1:-1])
#
# #Ex_2
# num = list(range(1,21,2));print(num)
#
# #Ex_3
# colors = ["빨간색","파란색","노란색","검정색","초록색"]
#
# for color in colors:
#     print("나는 %s을 가장 좋아합니다~~~"%color)
#
# #Ex_4
# animals = ["사자","호랑이","사슴","곰"]
#
# i = 0
# while i< len(animals):
#     print(animals[i])
#
#     i = i+1
#
# #Ex_5
# mylist = ["사과","바나나","파인애플","포도"]
# print(mylist[2])
#
# #Ex_6
# mylist = ["사과","바나나","파인애플","포도","오렌지","배"]
# print(mylist[-3:-1])
#
# #Ex_7
# mylist = ["사과","바나나","파인애플","포도","오렌지","배"]
# print(mylist[-2:])
#
# #Ex_8
# mylist = ["사과","바나나","파인애플","포도","오렌지","배"]
# if "포도" in mylist:
#     print("예, '포도'는 리스트 내에 있어요!")
#
# #Ex_9
# mylist = ["사과","바나나","파인애플","포도","오렌지","배"]
# mylist.append("키위")
#
# for a in mylist:
#     print(a)
#
# #Ex_10
# mylist = ["사과","바나나","파인애플","포도","오렌지","배"]
# mylist.insert(3,"딸기")
#
# for a in mylist:
#     print(a)
#
# #Ex_11
# mylist = ["사과","바나나","파인애플","포도","오렌지","배"]
# mylist.remove("바나나")
#
# for a in mylist:
#     print(a)
#
# #Ex_12
# mylist = ["사과","바나나","파인애플","포도","오렌지","배"]
# del mylist[4]
#
# for a in mylist:
#     print(a)
#
# #Ex_13
# mylist = ["사과","바나나","파인애플","포도","오렌지","배"]
# mylist.clear()
#
# if len(mylist)==0:
#     print("리스트 내 요소가 없습니다.")
#
# #Ex_14
# mylist = ["사과","바나나","파인애플","포도","오렌지","배"]
# mylist2 = mylist.copy()
#
# for a in mylist2:
#     print(a)
#
# #Ex_15
# mylist = ["사과","바나나","파인애플","포도","오렌지","배"]
# mylist.sort()
#
# for a in mylist:
#     print(a)
#
# #Ex_16
# mylist = ["사과","바나나","파인애플","포도","오렌지","배"]
# mylist.reverse()
#
# for a in mylist:
#     print(a)
#
# #Ex_17
# questions = ["tr_in","b_s","_axi","air_lane"]
# answers = ["a","u","t","p"]
#
# for i in range(len(questions)):
#     q = "%s에서 밑줄(_)안에 들어갈 알파벳은?"%questions[i]
#     ans = input(q)
#
#     if ans==answers[i] :
#         print("정답입니다!")
#     else:
#         print("틀렸습니다!")
#
# #Ex_18
# scores = []
#
# while True:
#     score = int(input("성적을 입력하세요(종료 시 -1 입력):"))
#
#     if score == -1:
#         break
#     else:
#         scores.append(score)
#
# print("%s"%scores)
#
# #Ex_19
# person1 = ["kim",24,"kim@naver.com"]
# person2 = ["lee",35,"lee@hanmail.net"]
#
# person = person1 + person2
#
# print(person)
#
# #Ex_20
# numbers = [[10,20,30],[40,50,60,70,80]]
#
# for i in range(len(numbers)):
#     for j in range(len(numbers[i])):
#         print("numbers[%d][%d] = %d"%(i,j,numbers[i][j]))
#
# #Ex_21
# scores = [[75,83,90],[86,86,73],[76,95,83],[89,96,69],[89,76,93]]
#
# for i in range(len(scores)):
#     sum = 0
#     for j in range(len(scores[i])):
#         sum =sum + scores[i][j]
#
#     avg = sum/len(scores[i])
#
#     print("%d번째 학생의 합계 : %d, 평균 : %.2f"%(i+1,sum,avg))
#
# #Ex_22
# strings = [["잠자리","풍뎅이","여치"],["짜장면","파스타","피자",'국수']]
#
# for i in range(len(strings)):
#     for j in range(len(strings[i])):
#         print(strings[i][j])
#
#     print()

#Ex_23
s = [64,89,100,85,77,58,79,67,96,87,
     87,36,82,98,84,76,63,69,53,22]

count_su,count_woo,\
count_mi,count_yang,\
count_ga = 0,0,0,0,0

i = 0
while i<len(s):
    if 90<=s[i]<=100:
        count_su +=1

    elif 80<=s[i]:
        count_woo +=1

    elif 70<=s[i]:
        count_mi +=1

    elif 60<=s[i]:
        count_yang +=1

    else:
        count_ga +=1

    i +=1

print("수 : %d명"%count_su)
print("우 : %d명"%count_woo)
print("미 : %d명"%count_mi)
print("양 : %d명"%count_yang)
print("가 : %d명"%count_ga)
