# 1) Print: 숫자는 그냥 씀
# a) 제어문자: \이후 n(다음줄이동) t(tab) \(\문자자체출력)
# 예제: \n \t \\
print(1,2,3, sep='\n') # sep='\n' sep='\\' sep='\t' sep=',' sep=', '
print('1\n2')
print('Hello', '\n', 'Python', sep='') # print(Hello\nPython)
# b) end: print문 끝에는 end='/n' default임. 
print(1, end='.')
print(2, end='\n')
# c) 숫자 
print(3.1, 'Python', 100)
print(16, 9, sep=':')
# d) 큰 숫자를 콤마로 표현 
print(100_000_000)

# 2) is
x = 1000
y = 1000
print(x is y) # True

# 3) 행렬곱 @
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a@b)

