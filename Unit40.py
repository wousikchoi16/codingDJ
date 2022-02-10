# Unit40 제네레이터(발생자) 사용하기 (금요일)
# 제너레이터는 이터레이터를 생성해주는 함수임. 함수안에 yield라는 키워드만 사용하면 끝임. #이터레이터=값을 차례대로 꺼낼수 있는 객체.
# yield에 무엇을 지정하든 결과만 바깥으로 전달합니다.(함수의 반환값, 식의 결과)
# 제너레이터는 함수끝까지 도달하면 StopIteration예외가 자동으로 발생하고 반복을 끝냄.
# 제너레이터표현식(메모리절약/필요할때 요소를 생성): (식 for 변수 in 반복가능한객체) 

# 1) 제너레이터와 yield 알아보기 
#   - 함수 안에서 yield를 사용하면 함수는 제너레이터가 되며 yield에는 값(변수)를 지정합니다. 
# 예시
def number_generator():
    yield 0
    yield 1
    yield 2
for i in number_generator():
    print(i)
#   a) 제너레이터 객체가 이터레이터인지 확인하기 
#       - dir(제너레이터객체) -> __iter__, __next__메서드가 들어있다.

# 2) 제너레이터 만들기 
# # 예시1
# def number_generator(stop):
#     n = 0
#     while n < stop:
#         yield n
#         n += 1
# for i in number_generator(13):
#     print(i)
# 예시2
def upper_generator(x):
    for i in x:
        yield i.upper()
fruits = ['apple','pear','grape','pineapple']
for i in upper_generator(fruits):
    print(i)

# 3) yield from으로 값을 여러번 바깥으로 전달하기 
#   - 표시방법1: yield from 반복가능한객체(리스트)
#   - 표시방법2: yield from 이터레이터
#   - 표시방법3: yield from 제너레이터객체
