# Unit20: FizzBuzz 문제 
# 20.5 코드 단축하기***
# print문 내부: 문자*T/F와 or
for i in range(1,101):
    print('Fizz'*(i%3==0)+'Buzz'*(i%5==0) or i)
