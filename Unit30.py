# # Unit30 함수에서 위치인수와 키워드인수 사용하기 
# # 1) 위치인수를 사용하는 함수
# def print_numbers(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# print_numbers(10,20,30)
# #   a) 언패킹 사용하기: 함수(*리스트), 함수(*튜플)
# #      주의사항: 함수의 매개변수와 리스트의 요소 개수는 같아야 함.  
# x = [10,20,30] # 4개넣으면 에러발생
# print_numbers(*x)

# # 2) 가변 인수 함수 만들기: 인수의 개수가 정해지지 않은 가변인수(variable argument)사용
# #   def 함수이름(*매개변수):
# #       코드
# #   -> *매개변수: 리스트/튜플에서 사용! 가변인수함수를 만들 수 있음. 
# #   -> 이런 함수를 호출할 때, (1) 인수를 각각 넣거나, (2) 리스트/튜플 언패킹을 사용하면 됨. 
# #   -> 매개변수이름은 원하는대로 지어도 되지만, arguments를 줄여서 args로 사용함. 
# def print_numbers(*args):
#     for arg in args:
#         print(arg)
# print_numbers(10)
# print_numbers(10,20,30,40)
# x = [10]
# print_numbers(*x)
# y = [10,20,30,40]
# print_numbers(*y)
# #   c) 고정인수와 가변인수를 함께 사용하기: 고정인수를 먼저 지정하고, 그다음 매개변수에 *를 붙여주면 됨. 
# def print_numbers2(a,*arg):
#     print(a)
#     print(arg)
# print_numbers2(1) 
# print_numbers2(1,10,20)
# print_numbers2(*[10,20,30])


# # 2) 키워드 인수 사용하기: 함수(키워드=값)
# def personal_info(name,age,address):
#     print('이름:', name)
#     print('나이:', age)
#     print('주소:', address)
# # print(personal_info('홍길동',30,'서울시 용산구'))
# # print(personal_info(name='홍길동',address='서울시 용산구',age=30))


# # 3) 키워드 인수와 딕셔너리 언패킹 사용하기: 함수(**딕셔너리)
# #   -> 매개변수**: 딕셔너리에서 사용! 키워드인수를 사용하는 가변인수함수를 만들수 있음. 
# #   -> 딕셔너리의 키는 "문자열"형태이어야 함! 
# #   -> 딕셔너리의 키 이름 = 함수의 매개변수 이름 , 개수도 맞아야 함. 
# x = {'name':'홍길동','address':'서울시 용산구', 'age':30}
# personal_info(**x)
# personal_info(*x) # 1번만 *쓰면, 딕셔너리의 키값이 들어가서 출력된다. 
# #   def 함수이름(**매개변수):
# #       코드 
# #   -> 매개변수이름을 관례로 keyword arguments를 줄여서 kwargs로 사용함. 
# #   -> 
# def personal_info2(**kwargs):
#     for kw, arg in kwargs.items():
#         print(kw,':', arg, sep='')


# # 4) 고정인수와 가변인수(위치인수/키워드인수)를 함께 사용: 
# # -> 고정인수-가변인수(위치인수)-가변인수(키워드인수) 순서로 사용함. 

# # 5) 매개변수에 초깃값 지정하기 
# #   def 함수이름(매개변수=값):
# #       코드
# #   -> 초기값이 있는 매개변수는 맨 뒤로 배치. 

# 30.6 연습문제: 가장 높은 점수를 구하는 함수 만들기 
korean, english, mathematics, science = 100, 86, 81, 91
def get_max_score(*args):
    return max(args)
max_score = get_max_score(korean, english, mathematics, science)
print("높은점수:", max_score)
max_score = get_max_score(english,science)
print("높은점수:", max_score)