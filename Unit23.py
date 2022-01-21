# Unit 23: 2차원 리스트 사용하기 
# 톱니형 리스트 생성가능: 가로크기가 불규칙한 톱니형 리스트
# p.314
# b = ([10,20], [30,40],[50,60])
# c = [(10,20), (30,40),(50,60)]
# a) 
# b[0] = (500,600) #에러
# b) 
# b[0][0] = 500 # 잘작동
# print(b)
# # c) 
# c[0][0] = 500
# print(c)
# # d) 
# c[0] = (500,600)
# print(c)
# -> 리스트 형식일때는 입력변경가능하지만, 튜플형식에선 입력변경 불가.

# # pprint모듈의 함수 
# from pprint import pprint 
# a = [[10,20],[30,40],[50,60]]
# pprint(a,indent=4, width=20)

# # sorted(반복가능한객체**, key=정렬함수, reverse=T/F)
# Students = [
#     ['john','C',19],
#     ['maria','A',25],
#     ['andrew','B',7]
# ]
# print(sorted(Students,key=lambda a:a[2]))

# 2차원이상의 다차원 리스트에서 복사를 하려면, deepcopy함수사용. 
# import copy 
# b = copy.deepcopy(a) 이런식으로 이용. 
