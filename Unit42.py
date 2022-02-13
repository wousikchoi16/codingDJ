# Unit42 데코레이터 사용하기 
#   - 데코레이터(장식자)는 장식하다/꾸미다라는 뜻인데 장식하는 도구 정도로 설명할 수 있습니다. 
#   - 데코레이터는 기존 함수를 수정하지 않으면서 추가기능을 구현할 때 사용합니다(1-a)
#   - 데코레이터를 사용할때는 @으로 함수위에 지정해주면 됨. 

# 1) 데코레이터 만들기
from tkinter import E


def trace(func):
    def wrapper():
        print(func.__name__,'함수시작')
        func()
        print(func.__name__,'함수끝')
    return wrapper
def hello():
    print('hello')
def world():
    print('world')
trace_hello = trace(hello)
trace_hello()
trace_world = trace(world)
trace_world()

#   a) @으로 데코레이터 사용하기 
#       예시) 
#       @데코레이터 
#       def 함수이름():
#           코드
def trace(func):
    def wrapper():
        print(func.__name__,'함수시작1')
        func()
        print(func.__name__,'함수끝1')
    return wrapper

@trace
def hello():
    print('hello')

@trace
def world():
    print('world')

hello()
world()

#   예시)
#   @decorator1
#   @decorator2
#   def hello():
#       print('hello')
#   hello()
#   예시2=예시1)
#   decorated_hello = decorator1(decorator2(hello))
#   decorated_hello()

# 2) 매개변수와 반환값을 처리하는 데코레이터 만들기
def trace(func): # func(a,b) -> def trace("func") + def wrapper("a,b") 
    def wrapper(a,b):
        r = func(a,b)
        print('{0}(a={1},b={2})->{3}'.format(func.__name__,a,b,r))
        return r
    return wrapper
@trace
def add(a,b):
    return a+b
print(add(10,20))

#   a) 가변인수 함수 데코레이터
def trace(func):
    def wrapper(*args,**kwargs):
        r = func(*args,**kwargs)
        print('{0}(args={1},kwargs={2})->{3}'.format(func.__name__,args,kwargs,r))
        return r
    return wrapper
@trace
def get_max(*args):
    return max(args)
@trace
def get_min(**kwargs):
    return min(kwargs.values())
@trace
def add(a,b):
    return a+b
print(add(10,20))
print(get_max(10,20))
print(get_min(x=10,y=20,z=30))

#   b) 클래스를 만들고 안에 메서드에 데코레이터를 사용할 때는 self입력부분을 확인하여 코드 작성필요. 
#   - 만약 클래스 안에 메서드를 만들때 def add(self,a,b)로 쓴 경우-> 데코레이터 코드부분에 def wrapper(self,a,b)로 써야 함. 


# 3) 매개변수가 있는 데코레이터 만들기 
# 예시) 
# @데코레이터(인수)
# def 함수이름():
#   코드: 

# 예시) 
# def is_multiple(x): # 데코레이터가 사용할 매개변수를 지정
#   def real_decorator(func): # 호출할 함수를 매개변수로 받음
#       def wrapper(a,b): # 호출할 함수의 매개변수와 똑같이 지정 
#           return r # 예시로 계산한 값
#       return wrapper
#   return real_decorator

#   a) 매개변수가 있는 데코레이터를 여러개 지정하기 
#   예시1)
#   @데코레이터1(인수)
#   @데코레이터2(인수)
#   def 함수이름():
#       코드
#   예시2)
#   decorated_add = is_multiple(3)(is_multiple(7)(add))
#   decorated_add(10,20)
#   632page다시보기

# 4) 클래스로 데코레이터 만들기 
class Trace:
    def __init__(self,func):
        self.func = func
    def __call__(self):
        print(self.func.__name__,'함수시작2')
        self.func()
        print(self.func.__name__,'함수끝2')
@Trace
def hello():
    print('hello')
hello()

# 5) 클래스로 매개변수와 반환값을 처리하는 데코레이터 만들기 
class Trace:
    def __init__(self, func):    # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func         # 호출할 함수를 속성 func에 저장

    def __call__(self, *args, **kwargs):    # 호출할 함수의 매개변수를 처리
        r = self.func(*args, **kwargs) # self.func에 매개변수를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
                                            # 매개변수와 반환값 출력
        return r                            # self.func의 반환값을 반환
@Trace    # @데코레이터
def add(a, b):
    return a + b
print(add(10, 20))
print(add(a=10, b=20))

# 정리: 데코레이터가 기존 함수를 수정하지 않으면서 추가 기능을 구현할 때 사용한다는 점만 기억하면 됩니다. 
#       보통 데코레이터는 프로그램의 버그를 찾는 디버깅, 함수의 성능 측정, 함수 실행전에 데이터 확인 등에 활용합니다. 
#       (앞에서 만든 함수의 시작과 끝을 출력하는 데코레이터, 매개변수와 반환값을 출력하는 데코레이터는 디버깅에 활용할 수 있습니다)