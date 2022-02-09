# Unit39 이터레이터(반복자) 사용하기 (목)
# 이터레이터(iterator)는 값을 차례대로 꺼낼 수 있는 객체(object)입니다
#   - 파이썬에서는 이터레이터만 생성하고 값이 필요한 시점이 되었을때 값을 만드는 방식을 사용합니다. 
#   - 즉, 데이터 생성을 뒤로 미루는 것인데 이런 방식을 지연평가(lazy evaluation)라고 합니다. 
#   - 반복가능한객체에서 __iter__메서드로 이터레이터를 얻습니다. 
#   (참고) 반복가능한객체: 요소의 순서와는 상관없이 요소를 한번에 하나씩 꺼낼 수 있으면 반복가능한 객체
#       -> 리스트, 튜플, range, 문자열 + 딕셔너리,세트
#   (참고) 시퀀스객체:요소의 순서가 정해져있고 연속적으로 이어져있음 
#       -> 리스트, 튜플, range, 문자열

# 1) 반복 가능한 객체 알아보기 
#   - 객체가 반복 가능한 객체인지 알아보는 방법은 객체에 __iter__메서드가 들어있는지 확인해 보면 됩니다
#   - 객체의 메서드 확인: dir(객체)
#   - 반복가능한객체(iterable)와 이터레이터(iterator)는 별개의 객체이므로 둘은 구별해야함. 
#   - 클래스에 __iter__와 __next__메서드를 모두 구현하면 이터레이터를 만들 수 있습니다. 
#   - 특히, __iter__, __next__를 가진 객체를 이터레이터 프로토콜(iterator protocol)을 지원한다고 말합니다.
# print(dir([1,2,3]))
# print([1,2,3].__iter__())
# it = [1,2,3].__iter__()
# it = range(3).__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# 2) 이터레이터 만들기 
it = iter(range(3))
print(next(it))
print(next(it))
print(next(it))
#   - 반복 가능한 객체에서 __init__를 호출하고 이터레이터에서 __next__메서드를 호출한 것과 똑같다
#   - 즉, iter는 반복가능한객체에서 이터레이터를 반환하고 next는 이터레이터에서 값을 차례대로 꺼냅니다. 
#   a) iter: iter(호출가능한객체,반복을끝낼값)
#   - 반복을 감시하다가 특정값이 나오면 반복을 끝낸다고 해서 sentinel
# 예시1
import random
for i in iter(lambda: random.randint(0,5),2):
    print(i, end=' ')
# 예시2
import random
while True:
    i = random.randint(0,5)
    if i ==2:
        break
    print(i,end=' ')
#   b) next: next(반복가능한객체,기본값) 반복이 끝나더라도 StopIteration이 발생하지 않고 기본값을 출력합니다. 
# 예시
it = iter(range(3))
print(next(it,10))
print(next(it,10))
print(next(it,10))
print(next(it,10))

# 39.6 연습문제: 배수 이터레이터 만들기 
class MultipleIterator:
    def __init__(self,stop,multiple):
        self.current = 0
        self.multiple = multiple
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        self.current = self.current +1
        if self.current*self.multiple < self.stop:
            return self.current*self.multiple
        else: 
            raise StopIteration
        
for i in MultipleIterator(20,3):
    print(i,end=' ')
print()
for i in MultipleIterator(30,5):
    print(i,end=' ')