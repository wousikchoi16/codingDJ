# Unit 26: Set
# 세트 = {값1,값2,값3}
# 세트는 
# - 중복될수없음
# - 요소의 순서가 정해져 있지 않습니다. 
# - []대괄호로 특정 요소만 출력할 수 없음. 
# - 세트안에 세트 넣는 것은 안됨. 단 frozenset(반복가능한객체)는 가능함. 

# 1) 세트에 특정값이 있는지: 값 in 세트 
fruits = {'strawberry','grape','orange','pineapple'}
print('orange' in fruits)
print('peach' in fruits)
print('orange' not in fruits)
print('peach' not in fruits)

# 2) set를 사용하여 세트만들기: set(반복가능한객체)
a = set('aaple')
print(a)

# 3) 형식주의1 
c = {}
print(type(c))
c = set()
print(type(c))

# 4) frozenset
print(frozenset({frozenset({1,2}), frozenset({3,4})}))

# 5) 집합연산 사용하기: | & 
a = {1,2,3,4}
b = {3,4,5,6}
print(a|b)
print(set.union(a,b))
print(a&b)
print(set.intersection(a,b))
print(a-b)
print(set.difference(a,b))
print(a^b)
print(set.symmetric_difference(a,b))

# 6) 집합 연산후 할당 연산자 사용하기 
a = {1,2,3,4}
a |={5}
print(a)
a = {1,2,3,4}
a.update({5})
print(a)
a = {1,2,3,4}
a &= {0,1,2,3,4}
print(a)
a = {1,2,3,4}
a.intersection_update({0,1,2,3,4})
print(a)
a = {1,2,3,4}
a -= {3}
print(a)
a = {1,2,3,4}
a.difference_update({3})
print(a)
a = {1,2,3,4}
a ^={3,4,5,6}
print(a)
a = {1,2,3,4}
a.symmetric_difference_update({3,4,5,6})
print(a)

# 7) 부분집합과 상위집합 확인하기 
a = {1,2,3,4}
print(a <= {1,2,3,4})
print(a.issubset({1,2,3,4}))
a = {1,2,3,4}
print(a <= {1,2,3,4,5})
a = {1,2,3,4}
print(a >= {1,2,3,4,5})
print(a.issuperset({1,2,3,4,5}))

# 8) 세트가 겹치지 않는지 확인하기 
a = {1,2,3,4}
print(a.isdisjoint({5,6,7,8}))
print(a.isdisjoint({1,5,6,7,8}))

# 9) 세트조작하기 
a = {1,2,3,4}
a.add(5)
print(a)
a.remove(3)
print(a)
a.discard(2)
print(a)
a.discard(3)
print(a)

# 10) 세트에서 임의의 요소를 삭제하기 
a = {1,2,3,4}
print(a.pop())
print(a)

# 11) 세트의 모든 요소를 삭제하기 
a = {1,2,3,4}
a.clear()
print(a)

# 12) 세트의 요소 개수 구하기 
a = {1,2,3,4}
print(len(a))

# 13) 세트의 할당과 복사 
a = {1,2,3,4}
b = a
print(a is b)
b.add(5)
print(a)
print(b)
a = {1,2,3,4}
b = a.copy()
print(a is b)
print(a == b)

a = {1,2,3,4}
b = a.copy()
b.add(5)
print(a)
print(b)

# 14) 세트표현식 사용하기 
# {식 for 변수 in 반복가능한객체}
# set(식 for 변수 in 반복가능한객체)
# {식 for 변수 in 반복가능한객체 if 조건식}
# set(식 for 변수 in 반복가능한객체 if 조건식)
a = {i for i in 'apple'}
print(a)
a = {i for i in 'pineapple' if i not in 'apl'}
print(a)