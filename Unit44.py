# Unit44 모듈과 패키지 사용하기
# 모듈
# - 각종 변수, 함수, 클래스를 담고 있는 파일 
# - 특정기능을 .py파일 단위로 작성한 것
# 패키지
# - 여러 모듈을 묶은 것으로 모듈에 네임스페이스(namespace,이름공간)를 제공. 
# 파이썬 표준 라이브러리(Python Standard Library, PSL)
# - 파이썬에 기본으로 설치된 모듈과 패키지, 내장함수를 묶어서 파이썬 표준 라이브러리라 부른다. 

# 1) import로 모듈 가져오기 
# 예시1) import로 모듈가져오기 
# import 모듈
# import 모듈1, 모듈2
# 모듈.변수
# 모듈.함수()
# 모듈.클래스()
# 예시2) import as로 모듈 이름 지정하기 
# import 모듈 as 이름
# 이름.함수()
# 예시3) from import로 모듈의 일부만 가져오기 
# from 모듈 import 변수 # 모듈이름을 붙이지 않고 변수를 바로 사용가능. 
# from 모듈 import 함수 
# from 모듈 import 클래스 
# from 모듈 import 변수,함수,클래스  # 한번에 여러개 지정 가능
# 예시4) from import로 모듈의 모든 변수,함수,클래스 가져오기 
# from 모듈 import * # from math import *
# 예시5) from import로 모듈의 일부를 가져온 뒤 이름 지정하기 
# from 모듈 import 변수 as 이름 
# from 모듈 import 함수 as 이름 
# from 모듈 import 클래스 as 이름 
# from 모듈 import 변수 as 이름1, 함수 as 이름2, 클래스 as 이름3
# 예시6) 가져온 모듈 해제하기
# - import math 
# - del math

# 2) import로 패키지 가져오기 
# 예시1)
# import 패키지.모듈
# import 패키지.모듈1, 패키지.모듈2
# 패키지.모듈.변수
# 패키지.모듈.함수()
# 패키지.모듈.클래스()
# 예시2) import as로 패키지 모듈 이름 지정하기 
# import 패키지.모듈 as 이름 
# 이름.함수()
# 예시3) from import로 패키지의 모듈에서 일부만 가져오기
# from 패키지.모듈 import 변수
# from 패키지.모듈 import 함수 
# from 패키지.모듈 import 클래스  
# from 패키지.모듈 import 변수,함수,클래스
# 예시4) 패키지의 모듈에서 모든 변수,함수,클래스를 가져오기
# from 패키지.모듈 import * 
# 예시5) from import로 패키지의 모듈의 일부를 가져온 뒤 이름 지정하기 
# from 패키지.모듈 import 변수 as 이름 
# from 패키지.모듈 import 변수 as 이름, 함수 as 이름, 클래스 as 이름

# 3) 파이썬 패키지 인덱스에서 패키지 설치하기 
#   a) pip로 패키지 설치하기
#   - pip install 패키지 : 반드시 명령프롬프트, 콘솔, 터미널에서 입력 
#   - python -m pip install 패키지 : -m옵션은 모듈을 실행하는 옵션이며 pip도 모듈임. 

# 4) import로 패키지 가져오기 
# 예시1) 
# import 패키지 # 보통pip로 설치한 패키지는 import 패키지, import 패키지.모듈 형식으로 사용. 패키지마다 구성다르니 웹사이트확인. 

# 5) 패키지 검색, 버전지정, 목록출력, 삭제 
# 예시1) 
# pip search 패키지: 패키지 검색
# pip install 패키지==버전: 특정 버전의 패키지를 설치(pip install requests==2.9.0)
# pip list 또는 pip freeze: 패키지 목록 출력
# pip uninstall 패키지: 패키지 삭제 

# 44.5 연습문제: 소수점 이하 올림, 버림 구하기 
# from math import *
from math import ceil, floor
x = 1.5
print(ceil(x),floor(x))