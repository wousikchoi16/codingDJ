# # 예시1
# a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
# print(a + b)

# # 예시2
# a, b = input('숫자 두개를 입력하세요').split()
# a = int(a) 
# b = int(b)
# print(a+b)

# p.82
a, b, c = map(int,input('정수 세 개를 입력하시오').split())
print(a+b+c)

# 6.8 심사문제
korean, english, mathematics, science = map(int, input().split() )
print(int((korean + english + mathematics + science)/4))