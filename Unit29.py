# Unit 29 함수 사용하기 
# 함수 사용 이점: 1) 코드용도 구분 2) 코드 재사용 3) 실수 감소
# def 함수이름(매개변수1,매개변수2):
#   return 반환값1, 반환값2 
# -> return을 여러개 반환하면 튜플형식임. 리스트로 변경 가능.

# 1) 함수 독스트링 사용하기: """ """
def add(a,b): # a, b는 인수(argument)
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수임."""
    return a+b
x = add(10,20)
print(x)
print(add.__doc__)
print(help(add))

# 2) 함수 중간에 return으로 빠져 나오기. 
def not_ten(x):
    if x == 10:
        return 
    print(x, '입니다.', sep='')
print(not_ten(5))
print(not_ten(10))
