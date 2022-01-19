# Unit 22: 리스트와 튜플 응용하기 
# 리스트에 요소추가/요소삭제/정보조회
# 1) 리스트 요소추가: append() 리스트길이가 1씩 증가. 
# 2) 리스트 확장: extend() 리스트에 추가요소가 많은경우 사용. 
# 3) 리스트의 특정인덱스에 요소 추가하기: insert(위치,값) 리스트길이 1씩 증가
a = [10,20,30]
a[1]=[500,600]
print(a)
a = [10,20,30]
a[1:1]=[500,600]
print(a)
# 4) 리스트에서 요소 삭제하기: pop() 마지막요소 삭제 (del())
a = [10,20,30]
a.pop()
print(a)
a = [10,20,30]
del a[1]
print(a)
# 5) 리스트에서 특정값을 찾아서 삭제하기 
a = [10,20,30,20]
a.remove(20) #처음찾은 20을 삭제한다. 
print(a)
# 6) 리스트로 Stack: append() pop()
# 7) 리스트로 Queue: append() pop(0) -> 덱(deque)이용하자!
from collections import deque
a = deque([10,20,30])
print(a)
a.append(500)
print(a)
a.popleft()
print(a)
# 오른쪽입력 append, 왼쪽제거 popleft()
# 왼쪽입력 appendleft, 오른쪽제거 pop()

# 8) 리스트에서 특정값의 인덱스 구하기 
a = [10,20,30,15,20,40]
print(a.index(20))
# 9) 특정값의 개수 구하기 
a = [10,20,30,15,20,40]
print(a.count(20))
# 10) 리스트의 순서를 뒤집기 
a = [10,20,30,15,20,40]
a.reverse()
print(a)
# 11) 리스트의 요소를 정렬하기: sort() 작은순서대로 정렬
# sorted()는 새로운 리스트를 생성하기 때문에 a = sorted(a)써야함.
a = [10,20,30,15,20,40]
a.sort()
print(a)
# 12) 리스트의 모든요소를 삭제하기 
a = [10,20,30,15,20,40]
a.clear()
print(a)
a = [10,20,30,15,20,40]
del a[:]
print(a)
# 13) 리스트를 슬라이스로 조작하기 
a = [10,20,30,15,20,40]
a[len(a):] = [500,600]
print(a)
# 14) 리스트가 비어있는지 확인 
# PEP 8 권장 코드 
# if not seq: pass #리스트가 비어있다면 True
# if seq: pass #리스트에 내용이 있다면 True
# 권장하지 않는 방법
# if not len(seq): pass #리스트가 비어있다면 True
# if len(seq): pass #리스트에 내용이 있다면 True
# 예시
seq = []
if seq:
    print(seq[-1])

# 15) 리스트의 할당과 복사 
# a) 할당 
a = [0,0,0,0,0]
b = a
print(a is b)
b[2] = 99
print('a:', a)
print('b:', b)
# b) 복사
a = [0,0,0,0,0]
b = a.copy()
print(a is b)
b[2] = 99
print('a:', a)
print('b:', b)

# 16) for반복문으로 요소출력하기 
# for 인덱스,요소 in enumerate(a):
#     print(인덱스,요소)
# 인덱스를 1부터 시작하고 싶다면. 
# for 인덱스,요소 in enumerate(a,start=1):
#     print(인덱스,요소)

# 17) 리스트 표현식(list comprehension)
a = [i for i in range(10)] # 추천: 대괄호
print(a)
a = list(i for i in range(10)) # 비추천
print(a)
# 조건문추가한 리스트컨프리헨션
a = [i for i in range(10) if i%2==0]
print(a)
# 여러 for문이 들어간 리스트컨프리헨션
# ** 앞의 for문이 느리게 숫자변하고, 뒤의 for문이 먼저 돌아서 계산됨. 
a = [(j,i,k) for j in range(10) for i in range(5) for k in range(3)]
print(a)

# 18) 리스트에 map사용하기 
# map함수는 원본리스트를 변경하지 않고, 새로운 리스트 생성함. 
# list(map(함수,리스트))
# tuple(map(함수,튜플))
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int,a))
print(a)

# 19) input().split()과 map
a = map(int,input().split()) # a는 map객체임. 
print(list(a)) #이렇게 해줘야 입력값이 보임. 
print(a)

# 튜플 응용하기 
# 1) 튜플에서 특정 값의 인덱스 구하기 
a = (38,21,53,62,19.53)
print(a.index(53))
# 2) 특정값의 개수 구하기 
a = (38,21,53,62,19.53)
print(a.count(21))

# 3) 튜플 표현식 사용하기 
# tuple(식 for 변수 in 리스트 if 조건식)
a = tuple(i for i in range(10) if i%2 ==0)
print(a)
print((i for i in range(10) if i%2 ==0)) # 제너레이터**1
