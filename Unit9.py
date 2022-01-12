# Unit9: 문자열사용하기
# 1) 여러줄로 된 문자열
#   - """   """(3개의 따옴표/작은따옴표) -> 작은따옴표/따옴표 다 넣을수있음
#   - 줄마지막에 \를 넣어준다 
# 2) 문자열 안에 따옴표 
#   - 작은따옴표 안에 작은따옴표를 넣고 싶을때는 \(역슬레시)를 앞에 붙여줌.
#   - 문자열 안에 ', " 등의 특수 문자를 포함하기 위해 앞에 \를 붙이는 방법을 이스케이프(escape)라고 부름.
#   예시) '''Hello
#            Python''' 
#      -> 'Hello\nPython'
# 3) 한국문자열 출력 에러나는 경우: UTF-8로 저장 확인 

# 9.4 심사문제
s = ''''Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively. '''
print(s)

