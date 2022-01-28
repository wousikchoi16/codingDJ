# Unit25: 딕셔너리 응용하기 

# 자주묻는 질문1: 딕셔너리 더하기 
x = {'a':1,'b':2}
y = {'c':3,'d':4}
x.update(y)
print(x)

x = {'a':1,'b':2}
y = {'c':3,'d':4}
print({**x, **y})

# 1) setdefault(키): 키-값추가만 가능.(값수정 불가)
x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x)
x.setdefault('a') # 기존의 키의 값을 바꾸지는 않음.
print(x)
x.setdefault('e') 
print(x)
x.setdefault('f', 100) 
print(x)

# 2) update: 키-값추가/ 값수정 가능
# update(반복가능한객체), update(딕셔너리), update(리스트), update(튜플), update(zip객체)
# update(키=값): 키가 문자열일 때만 사용가능! 
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.update(a=90)
print(x)
x.update(e=50)
print(x)
x.update(a=900, f=60)
print(x)

y = {1:'one', 2:'two'}
y.update({1:'ONE', 3:'THREE'})
print(y)
y.update(zip([1,2],['one','two']))
print(y)

# 3) pop(키): 키값 쌍을 삭제한뒤 삭제한값을 반환. 
# pop(키,값): 해당 키값쌍을 삭제한뒤 값을 반환하지만, 키가없으면 pop안의 값을 반환
x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x.pop('a'))
print(x)
print(x.pop('z',6))
# del로도 키값쌍을 삭제할 수 있음. 
x = {'a':10, 'b':20, 'c':30, 'd':40}
del x['b']
print(x)

# 4) popitem(): 임의의 키값쌍을 삭제한뒤, 삭제한 키값쌍을 반환
x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x.popitem())
print(x)

# 5) 딕셔너리의 모든 키값쌍을 삭제하기
x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x.clear())
print(x)

# 6) get(키,기본값),  get(키,기본값), 
x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x.get('a'))
print(x.get('z',8)) #키가 없으면 기본값을 반환함. 

# 7) 딕셔너리에서 키값쌍을 모두 가져오는 것.
# items(): 키-값 모두 가져옴
# keys(): 키를 모두 가져옴
# values(): 값을 모두 가져옴
x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x.items())
print(x.keys())
print(x.values())

# 8) 리스트와 튜플로 딕셔너리 만들기 
keys = ['a','b','c','d']
x = dict.fromkeys(keys)
print(x)
y = dict.fromkeys(keys,100)
print(y)

# 9) defaultdict: 처음 키를 지정할때 값을 주지 않으면 해당 키에 대한 디폴트 값을 지정하겠다. 
# 없는 키값을 호출하면, default값을 반환한다. 
# 참고자료: https://dongdongfather.tistory.com/69
from collections import defaultdict
from unicodedata import name
y = defaultdict(int) # int로 기본값생성 
print(y)

name_list = [('kim','sungsu'),('kang','hodong'),('park','jisung'),('kim','yuna'),('park','chanho'),('kang','hodong')]
nset = defaultdict(set)
for k,v in name_list:
    nset[k].add(v)
print(nset)

# 10) 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기 
x = {'a':10, 'b':20, 'c':30, 'd':40}
for i in x:
    print(i,end=' ')
print("finished")

for key, value in x.items():
    print(key,value)

# 11) 딕셔너리 표현식 
keys = ['a','b','c','d']
x = {key:value for key, value in dict.fromkeys(keys).items()}
print(x)
y = {key:0 for key, value in dict.fromkeys(keys).items()}
print(y)
z = {value:key for key, value in dict.fromkeys(keys).items()} # 값이 None이 key값이 됨으로, 딕셔너리z는 {None:'d'}나옴
print(z)

# 11-2) 딕셔너리 표현식: 특정값 삭제할때!!
# 딕셔너리는 for반복문으로 반복하면서 키-값쌍을 삭제하면 안된다.(p.368)
# 이때는 딕셔너리 표현식에서 if조건문을 사용하여 삭제할 값을 제외하면 됨. 
x = {'a':10, 'b':20, 'c':30, 'd':40}
x = {key: value for key, value in x.items() if value !=20} # 딕셔너리를 새로 만든다.
print(x)

# 12) 중첩 딕셔너리 
# 사용법1: 딕셔너리[키][키]
# 사용법2: 딕셔너리[키][키] = 값

# 13) 딕셔너리 할당과 복사(p.370)
x = {'a':10, 'b':20, 'c':30, 'd':40}
y = x
print("check1:", x is y)
print("check2:", x == y)
y['a'] = 99
print(x)
print(y)

x = {'a':10, 'b':20, 'c':30, 'd':40}
y = x.copy()
print("check3:", x is y)
print("check4:", x == y)
y['a'] = 99
print(x)
print(y)
 
# a) 중첩 딕셔너리의 할당과 복사 
x = {'a': {'python':'2.7'}, 'b':{'python':'3.6'} }
y = x.copy()
y['a']['python'] = '2.7.15'
print(x)
print(y)
# 중첩 딕셔너리를 완전히 복사하려면, deepcopy함수를 사용. 
x = {'a': {'python':'2.7'}, 'b':{'python':'3.6'} }
import copy
y = copy.deepcopy(x)
y['a']['python'] = '2.7.15'
print(x)
print(y)