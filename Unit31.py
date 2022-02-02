# Unit31 함수에서 재귀호출 사용하기 
# 함수안에서 함수 자기자신을 호출하는 방식
# 파이썬에서는 최대재귀깊이(maximum recursion depth)가 1000으로 정해져 있음. 
# -> 최대재귀깊이를 초과하면 RecursionError발생. 

# # 예제
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

# 31.4 연습문제: 재귀호출로 회문판별하기
def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0]!=word[-1]:
        return False
    return is_palindrome(word[1:-1])

print(is_palindrome('hello'))
print(is_palindrome('level'))