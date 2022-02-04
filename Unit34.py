# Unit34 클래스 사용하기
# 객체를 만들때 사용하는 것이 클래스임.(객체=인스턴스 같지만, 클래스얘기할때는 인스턴스)
# 객체지향프로그래밍: 복잡한 문제를 잘게 나누어서 객체로 만들고, 객체를 조합해서 문제를 해결. 
# int, list, dict등도 사실 클래스임. a=int(10)처럼 인스턴스를 만들어 사용함. 
# type(객체): 객체가 어떤 클래스인지 확인

# class 클래스이름: # 클래스이름은 대문자로 시작.
#   def 매서드(self): # 매서드=클래스 안에 들어있는 함수. 매서드의 첫번째 매개변수는 반드시 self.
#       코드
# 예시
class Person:
    def greeting(self):
        print("hello")
    def hello(self):
        self.greeting() # self.메서드()형식으로 클래스안의 메서드를 호출

# 1) 인스턴스 만들기
james = Person() # james는 Person의 인스턴스(instance)입니다. 클래스는 특정 개념을 표현만 할뿐 사용하려면 인스턴스를 생성해야 함. 
# a) 메서드 호출하기: 메서드는 클래스가 아니라 인스턴스를 통해 호출해야 함. 
#   인스턴스.메서드()
james.greeting()
# b) 빈 클래스 만들기 
# class Person:
#   pass
# c) 메서드안에서 메서드 호출하기: self.메서드() 형식으로 클래스안의 메서드를 호출
# d) 특정 클래스의 인스턴스인지 확인: isinstance(인스턴스,클래스)
#   예시: isinstance(james, Person) -> True
#   예시: isinstance(n, int) -> 정수면True/아니면False

# 2) 속성사용하기
#   - 속성은 __init__메서드에서 만들고, self.속성에 값을 할당함.  
#   - 속성(attribute)을 만들 때는 __init__메서드 안에서 self.속성에 값을 할당
#   - __init__메서드는 Person()처럼 인스턴스를 만들 때 호출되는 특별한 메서드입니다.
#   (참고) 앞뒤에 밑줄2개__가 붙은 메서드는 파이썬이 자동으로 호출해 주는 메서드=special method, magic method임.
# class 클래스이름:
#   def __init__(self):
#       self.속성 = 값
# a) self 의미: 인스턴스 자기자신
#   - 메서드를 호출할때, 현재 인스턴스가 메서드(self)의 self자리에 자동으로 들어감. 
# b) 인스턴스를 만들 때 값을 받기
#   - 인스턴스를 만들때 값을 넣어줄 수 있다
#       - maria = Person('마리아',20,'서울시 서초구')
#       - def __init__(self,*args):    -> maria = Person(*['마리아',20,'서울시 서초구']) 
#       - def __init__(self,**kwargs): -> maria = Person(**{'name':'마리아','age':20,'address':'서울시 서초구'}) 
# 예시
# class 클래스이름:
#   def __init__(self,매개변수1,매개변수2):
#       self.속성1 = 매개변수1
#       self.속성2 = 매개변수2
# c) 인스턴스를 생성한 뒤에 속성추가하기
#   - 추가한 속성은 해당 인스턴스에서만 생성됨. 다른 인스턴스는 추가한 속성이 생성되지 않음. 
#   - 메서드를 통해서 속성을 추가할 수도 있고, 직접 입력할수도 있다. 
#   - __slots__ = ['name', 'age'] # 허용할 속성 이름을 리스트로 넣어준다. 속성 이름은 반드시 문자열로 지정! 
# 예시1
# class Person:
#   __slots__ = ['name', 'age']
# maria = Person()
# maria.address = "서초구" -> 에러발생!
# 예시2
# class Person:
#   pass
# maria = Person()
# maria.name = '마리아'
# maria.name -> 결과 '마리아'
# james = Person()
# print(james.name) -> 결과: 에러발생 

# 3) 비공개 속성 사용하기 
#   - 비공개 속성은 클래스 바깥으로 드러내고 싶지 않은 값에 사용함. 중요한 값인데 바깥에서 함부로 바꾸면 안됨. 
#   - 비공개 속성은 "클래스 안의 메서드에서만 접근/수정할 수 있습니다."
# class 클래스이름: 
#   def __init__(self,매개변수):
#       self.__속성 = 값

# 4) 비공개 메서드 사용하기: 이름앞에 __(밑줄2개)로 시작
#   - 예시: def __greeting(self):