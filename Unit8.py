# 계산 순서: 비교연산자  -> 논리연산자 
# (is, is not, ==, !=, <, >, <=) -> (and, not, or)

# 객체가 같은지 다른지 비교하기 
print( 1 == 1.0 ) # 값 비교 True
print( 1 is 1.0 ) # 객체 비교 False
print(2*3 is 3+3) # True ***
print(id(2*3), id(3+3)) # 같은 주소가 나온다. ***
# id: 객체 고유값 
print(id(1))
print(id(1.0))

# bool(값)
print(bool(1)) # True
print(bool(1.5)) # True
print(bool('False')) # True

# 단락평가(short-circuit evaluation)
print(True and 'Python')
print('Python' and True)
print('Python' and False)
print(False and 'python')
print('python' and False)
print(0 and 'python')
print(False or 'Python') # 두번째 값까지 판단
print(0 or False) # 두번째 값까지 판단
