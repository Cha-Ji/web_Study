# #Ex_1
# menu = "짜장면","우동","짬뽕","볶음밥"
#
# print(menu)
# print(menu[0])
# print(menu[2])
# print(menu[0:-1])
# print(menu[1:])
# print(menu[-1])
#
# #Ex_2
# tup1 = 10,20,30
# tup2 = 40,50,60
#
# tup3 = tup1+tup2
#
# print(tup3)
# print(len(tup3))
#
# #Ex_3
# dans = 2,3,4,5,6,7,8,9
#
# print("="*50)
# print("구구단표")
# print("="*50)
#
# for dan in dans:
#     print(str(dan) + "단")
#
#     for i in range(1,10):
#         print("%d x %d = %d"%(dan,i,dan*i))
#     print("-"*30)
#
# #Ex_4
# members = {"name":"홍길동","age":22,"email":"gildong@korea.com"}
#
# print(members)
# print(members["name"])
# print(members['email'])
# print(members['age'])
#
# #Ex_5
# members = {"name":"홍길동","age":22,"email":"gildong@korea.com"}
#
# for x in members:
#     print("%s => %s"%(x,members[x]))
#
# #Ex_6
# members = {"name":"홍길동","age":22,"email":"gildong@korea.com"}
#
# for x,y in members.items():
#     print("%s => %s"%(x,y))
#
# #Ex_7
# members = {"name":"홍길동","age":22,"email":"gildong@korea.com"}
#
# members["age"] = 33
# print("%s의 나이 : %d"%(members['name'],members['age']))
#
# #Ex_8
# members = {"name":"홍길동","age":22,"email":"gildong@korea.com"}
#
# members["age"] = 33
# print("%s의 나이 : %d"%(members['name'],members['age']))
#
# #Ex_9
# members = {"name":"홍길동","age":22,"email":"gildong@korea.com"}
#
# members['phone']='010-1234-5678'
#
# print(members)
#
# #Ex_10
# members = {"name":"홍길동","age":22,"email":"gildong@korea.com",'phone':'010-1234-5678'}
#
# del members['age']
#
# print(members)
#
# #Ex_11
# members = {"name":"홍길동","age":22,"email":"gildong@korea.com",'phone':'010-1234-5678'}
#
# members.clear()
#
# print("딕셔너리(members)의 요소 : %s"%members)
#
# #Ex_12
# phones = {'갤럭시 S5':2014,'갤럭시 S7':2016,'갤럭시 노트8':2017,'갤럭시 S9':2018}
# print(phones)
#
# for key in phones.keys():
#     print("%s => %s"%(key,phones[key]))
#
# #Ex_13
# scores = {'김채린':85,'박수정':98,'함소희':94,'안예린':90,'연수진':93}
#
# sum = 0
#
# for key in scores:
#     sum = sum + scores[key]
#
#     print("%s : %d"%(key,scores[key]))
#
# avg = sum/len(scores)
# print("합계 : %d, 평균 : %.2f"%(sum,avg))
#
# #Ex_14
# ad = {'id':'admin','password':'12345'}
#
# in_id = input("아이디를 입력하세요:")
# in_password = input("비밀번호를 입력하세요:")
#
# if (in_id==ad['id'] and in_password==ad['password']):
#     print('모든 정보에 접근 권한이 있습니다!')
# else:
#     print('정보에 접근 권한이 없습니다!')

#Ex_15
words = {'꽃':'flower','나비':'butterfly','학교':'school',"자동차":'car','비행기':'airplane'}

print("<영어 단어 맞추기 퀴즈>")

for kor in words:
    in_word = input("%s에 해당되는 영어 단어를 입력해주세요:"%kor)
    if words[kor] == in_word:
        print('정답입니다!')
    else:
        print("틀렸습니다!")
