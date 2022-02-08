# Unit38 예외처리 사용하기
# -> 예외처리는 에러가 발생하더라도 스크립트의 실행을 중단하지 않고 계속 실행하고자 할때 사용한다는 점 꼭 기억하세요.

# 1) try-except사용하기 
# 예외(exception)란 코드를 실행하는 중에 발생한 에러를 뜻함. 
# 예외처리: 예외가 발생했을 때도 스크립트 실행을 중단하지 않고 계속 실행하게 해주는 것 
#   - 여러개의 예외가 발생하는 경우, 먼저 발생한 예외의 처리코드만 실행됩니다.(또는 예외 중에서 높은 계층의 예외부터 처리됩니다. 기반클래스>파생클래스 순)
#       Python Built-in Exceptions
#   - 예외처리는 에러가 발생하더라도 스크립트의 실행을 중단시키지 않고 계속 실행하고자 할때 사용합니다.
#   - try안에서 만든 변수는 try바깥에서 사용할 수 있다. try는 함수가 아니다.
# 예시1) 
# try:
#   실행코드
# except:
#   예외가발생했을때처리하는코드
# else: # 
#   try코드에서 에러가 발생하지 않았을때 실행될 코드
# finally:
#   예외발생여부와 상관없이 항상 실행할 코드 
# 예시2) 
# try:
#   실행코드
# except 예외이름: 
#   예외가발생했을때처리하는코드
y = [10,20,30]
try: 
    index, x = map(int, input('인덱스와 나눌숫자를 입력하세요:').split())
    a = y[index]/x
except ZeroDivisionError as e:
    print('ZeroDivisionError',e)
except IndexError as e:
    print('IndexError', e)
else:
    print(a)

# 2) 예외 발생시키기
#   - 표현방법1: raise 예외(에러메세지)
#   - 표현방법2: raise 
#   a) assert로 예외 발생시키기: assert는 디버깅모드에서만 실행(p.565)
#   - 표현방법3: assert 조건식
#   - 표현방법4: assert 조건식, 에러메세지

# 3) 예외 만들기 
#   - 프로그래머가 직접만든 예외를 '사용자 정의예외'라고 함.
# 예시1)
# class 예외이름(Exception):
#   def __init__(self):
#       super().__init__('에러메세지')
# 예시2) 
# class 예외이름(Exception):
#   pass # 아무것도 구현하지 않음. 
# raise 예외이름('에러메세지')
