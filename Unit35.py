# Unit35 클래스 속성과 정적, 클래스 메서드 사용하기
# 인스턴스를 만들지 않고 클래스로 호출하는 '정적메소드'와 '클래스메소드'도 사용

# 35.1.1 클래스 속성 사용하기
#   - 클래스속성은 클래스에 속해 있으며 모든 인스턴스에서 공유합니다. 
#   - 파이썬은 속성/메서드를 찾을 때, (1)인스턴스-> (2)클래스 순으로 찾음. 
# class 클래스이름:
#   속성 = 값
class Person:
    bag = []
    def put_bag(self, stuff):
        Person.bag.append(stuff) # 클래스이름으로 클래스속성에 접근
james = Person()
james.put_bag('책')
maria = Person()
maria.put_bag('열쇠')
print(james.bag)
print(maria.bag)
print(Person.bag)
print(james.__dict__)
print(Person.__dict__)

# 35.1.2 인스턴스 속성 사용하기 
class Person:
    def __init__(self):
        self.bag = []
    def put_bag(self,stuff):
        self.bag.append(stuff)
james = Person()
james.put_bag('책')
maria = Person()
maria.put_bag('열쇠')
print(james.bag)
print(maria.bag)
# 클래스속성: 모든 인스턴스가 공유. 인스턴스 전체가 사용해야 하는 값을 저장할때 사용 
# 인스턴스속성: 인스턴스별로 독립되어있음. 각 인스턴스가 값을 따로 저장해야 할 때 사용

# 35.1.3 비공개 클래스 속성 사용하기 
#   - 비공개 클래스속성은 '클래스 바깥으로 드러내고 싶지 않은 값에 사용합니다. 
# class 클래스이름:
#   __속성 = 값 # 비공개 클래스속성
class Knight:
    __item_limit = 10 #비공개 클래스 속성
    def print_item_limit(self):
        print(Knight.__item_limit) # 클래스 안에서만 접근할 수 있음. 
x = Knight()
x.print_item_limit() # 인스턴스에서 메소드 실행을 통해서 접근은 가능
# print(Knight.__item_limit) # 클래스 바깥에서는 접근할 수 없음
# 참고) 클래스와 메서드의 독스트링 사용하기: 콜론(:)다음줄에 """ """, ''' '''을 이용함. 
#       클래스.__doc__, 클래스.메서드.__doc__, 인스턴스.메서드.__doc__


# === 정적메서드와 클래스 메서드: 인스턴스를 통하지 않고, 클래스에서 바로 메서드호출 ===
# 35.2 정적 메서드 사용하기: 크래스.메서드()
#   - 정적메서드를 호출할때는 다음과 같이 클래스에서 바로 메서드를 호출하면 됩니다.(클래스에 접근할 필요도 없을때 사용)
#   - 메서드 위에 @staticmethod를 붙입니다. 
#   - 정적메서드는 매개변수에 self를 지정하지 않습니다. 
#   - 정적메서드는 self를 받지 않으므로 인스턴스 속성에는 접근할 수 없습니다. 그래서 보통 정적메서드는 인스턴스속성, 인스턴스메서드가 필요없을때 사용.
#   - (용도) 인스턴스의 상태를 변화시키지 않는 메서드를 만들때 사용함 !! 
# class 클래스 이름:
#     @staticmethod # @: 데코레이터라고 하며 메서드(함수)에 추가기능을 구현할 때 사용합니다. 
#     def 메서드(매개변수1, 매개변수2):
#         코드
class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)
    
    @staticmethod
    def mul(a,b):
        print(a*b)
Calc.add(10,20)
Calc.mul(10,20)

# 35.3 클래스 메서드 사용하기: @classmethod
#   - 클래스메서드는 메서드 안에서 클래스속성, 클래스메서드에 접근해야 할 때 사용합니다. 
#   - 특히, cls를 사용하면 메서드 안에서 현재 클래스의 인스턴스를 만들 수도 있음. 즉, cls는 클래스이므로 cls()는 Person()과 같다. 
#   - 클래스매서드는 첫 매개변수에 cls를 지정해야 함
# @classmethod
# def create(cls):
#   p = cls() # cls()로 인스턴스 생성
#   return p
class Person:
    count = 0 
    def __init__(self):
        Person.count += 1
    @classmethod
    def print_count(cls):
        print(f'{cls.count}명 생성되었습니다.')
james = Person()
maria = Person()
Person.print_count()


# 35.5 연습문제: 날짜 클래스 만들기 
class Date: 
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int,date_string.split('-'))
        return month<=12 and day<=31
if Date.is_date_valid('2000-10-31'):
    print("올바른 날짜 형식임")
else: 
    print('잘못된 날짜 형식임')
