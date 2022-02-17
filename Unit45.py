# Unit45 모듈과 패키지 만들기 
# 공통된 코드부분을 빼서 모듈과 패키지로 만들면 사용이 편리함
# 모듈
# - 변수,함수,클래스 등을 모아 놓은 스크립트 파일(간단한 기능을 담아 놓은 것)
# 패키지
# - 여러 모듈을 묶은 것으로 코드가 많고 복잡할때 사용
# - 기능들이 모듈 여러개로 잘게 나누어져 있고, 관련된 모듈끼리 폴더에 모여 있는 형태. 

# 1) 모듈 만들기 
# - 사용법1) 
#   import 모듈
#   모듈.변수 
#   모듈.함수()
#   모듈.클래스()
# - 사용법2) 
#   from 모듈 import 변수, 함수
# - 사용법3) 
#   from 모듈 import 클래스

# 2) 모듈과 시작점 알아보기 
#   if __name__ == '__main__': 으로 시작점을 알수 있음
#   - 현재 스크립트 파일이 프로그램의 시작점이 맞는지 판단하는 작업임. 
#   - 즉, 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도임. 

# 3) 패키지 만들기 
# - 패키지는 폴더(디렉토리)로 구성되어 있습니다. 
#   폴더 안에 __init__.py 파일도 들어있음. __init__.py안에 내용이 없어도 되고, 필요한 내용(__all__,from~import~)을 적어도 됨 
#   a) 패키지에 모듈 만들기 
#   b) 패키지 사용하기 
#   사용법1) 
#   import 패키지.모듈
#   패키지.모듈.변수
#   패키지.모듈.함수()
#   패키지.모듈.클래스()
#   사용법2) 
#   from 패키지.모듈 import 변수
#   from 패키지.모듈 import 함수
#   from 패키지.모듈 import 클래스 
#   c) 하위패키지 사용하기(p.682~683)
#   d) 모듈과 패키지의 독스트링