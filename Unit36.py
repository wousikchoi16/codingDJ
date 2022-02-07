# Unit36 클래스 상속 사용하기 
# 기반클래스(base/parent/super) - 파생클래스(derived/child/sub class)

# 1) 상속관계
# 상속은 명확하게 같은 종류이며 동등한 관계일 때 사용합니다. 
# 즉, "학생은 사람이다(Student is a Person)"라고 했을때 말이 되면 동등한 관계입니다. 
# Student(파생클래스)-Person(기반클래스)

# 2) 포함관계 
# 사람목록과 사람은 동등한 관계가 아니라 포함관계입니다. 
# 즉, "사람목록은 사람을 가지고 있다.(PersonList has a Person.)"
# 같은종류에 동등한 관계일 때는 상속을 사용하고, 그 이외에는 파생클래스의 속성에 기반클래스의 인스턴스를 넣는 포함방식을 사용하면 됩니다. 

# 3) 기반클래스의 속성 사용하기: super().__init__()
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요'
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__() # 동일함: super(Student,self).__init__()
        self.school = '파이썬코딩도장'
james = Student()
print(james.school)
print(james.hello)
#   a) 파생클래스에서 __init__메서드를 생략한다면, 기반클래스의 __init__이 자동으로 호출되므로 super()는 사용하지 않아도됨. 

# 4) 메서드오버라이딩 사용하기 
#   - 메서드오버라이딩은 원래 기능을 유지하면서 새로운 기능을 덧붙일때 사용함. 
#   - 오버라이딩(overriding)은 무시하다, 우선하다라는 뜻이 있는데 말 그대로 기반클래스의 메서드를 무시하고 새로운 매세드를 만든다는 뜻.
#   def greeting(self):
#       print("안녕하세요")
#   def greeting(self):
#       super().greeting()
#       print("저는 파이썬학생입니다.")

# 5) 다중상속 사용하기 
#   - 파이썬에서 메서드탐색순서(MRO:method resolution order): 클래스.mro()
#   - 다중상속받는 클래스목록의 왼쪽에서 오른쪽순서로 메서드를 찾습니다. 아래예시는 B->C임.
# class A:
#   def greeting(self):
#       print("A")
# class B(A):
#   def greeting(self):
#       print("B")
# class C(A):
#   def greeting(self):
#       print("C")
# class D(B,C):
#   pass
# x = D()
# x.greeting()

# 6) 추상클래스(abstract class) 사용하기 
#   - 추상클래스는 메서드의 목록만 가진 클래스이며 "상속받는 클래스에서 메서드 구현을 강제하기 위해 사용함."
#   - 즉, 추상클래스는 파생클래스가 반드시 구현해야하는 메서드를 정해줄 수 있습니다. 
#   - 추상글래스의 추상메서드를 모두 구현했는지 확인하는 시점은 "파생클래스가 인스턴스를 만들때" 입니다. 구현하지 않았다면 TypeError발생시킴.
#   - * 추상클래스는 인스턴스로 만들수가 없다. 오로지 상속에만 사용합니다. 
# from abc import *
# class 추상클래스이름(metaclass=ABCMeta):
#     @abstractmethod
#     def 메서드이름(self):
#         코드 
