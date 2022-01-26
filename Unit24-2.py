# Unit 24-2 다양한 방법으로 문자열 만들기 
# 1) 서식 지정자로 문자열 넣기 
#  a) '%s' % '문자열'
print('I am %s' % 'james') # s = string
#  b) '%d' % 숫자 
print('I am %d years old.' % 20) # d = decimal integer
#  c) '%f' % 숫자   
#  변형 '%.자리수f' % 숫자 
print('%f' % 2.3) # f = fixed point 기본 소수점 6자리
print('%.2f' % 2.3) # 소수점이하 자릿수 지정! 
print('%.4f' % 2.3) # 소수점이하 자릿수 지정! 
#  d) %길이s : 문자열을 지정된 길이로 만든뒤 오른쪽으로 정렬하고 남는 공간을 공백으로 채움. 
print('%10s' % 'python') # 왼쪽4칸은 공백, python 6칸오른쪽정렬 
#  e) %길이d
print('%10d' % 150)
#  f) %길이.자릿수f
print('%10.2f' % 2.3)
print('%10.2f' % 2000.3)
#  g) 왼쪽 정렬: %-길이s
print('%-10s' % 'python')
#  j) 서식지정자로 문자열 안에 값 여러개 넣기: '%d %s' % (숫자,문자열)
print('Today is %d %s.' % (3,'April'))
print('Today is %d%s.' % (3,'April'))

# 2) format 메서드 사용하기 
#  a) '{인덱스}'.format(값)
print('Hello, {0}'.format('world'))
#  b) 여러 값을 넣기 
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.3))
print('{0} {0} {1} {1}'.format('Python', 'Script'))
print('Hello, {} {} {}'.format('Python', 'Script', 3.4))
print('Hello, {lang} {version}'.format(lang='Python',version='3.5'))

# 3) 문자열 포메팅에 변수를 그대로 사용하기 
language1 = 'Python'
version1 = '3.7'
print(f'Hello, {language1} {version1}')
# 중괄호 자체를 출력하기: 두번 사용하면 됨.
print('{{ {0} }}'.format('Python'))

# 4) format메서드로 문자열 정렬하기(p.344): '{인덱스:<길이}'.format(값)
print('{0:<10}'.format('python'))
print('{:<10}'.format('python'))
print('{0:>10}'.format('python'))
print('{:>10}'.format('python'))

# 5) 숫자개수 맞추기
#  a) 정수: '%0개수d' % 숫자  '{인덱스:0개수d}'.format(숫자)
print('%03d' % 1)
print('{0:04d}'.format(35))
#  b) 실수: '%0개수.자릿수f' % 숫자  '{인덱스:0개수.자릿수f}'.format(숫자)
# 만약 개수<자릿수이면, 자릿수만큼은 보장되고 출력된다. 즉 자릿수이상으로 숫자가 출력됨. 
# 개수 = 소수점이하자릿수 + 소수점(1) + 정수자릿수 
print('%09.3f' % 1) # 개수 = 총자릿수
print('{0:09.4f}'.format(35)) # 개수 = 총자릿수

# 6) 채우기와 정렬을 조합해서 사용하기 
# 문자열 포메팅은 채우기와 정렬을 조합해서 사용할 수 있습니다. 
# 식: '{인덱스:[[채우기]정렬][길이][.자릿수][자료향]}'
print('{0:0<10}'.format(15))
print('{0:0>10}'.format(15))
print('{0:0>10.2f}'.format(15))
print('{0: >10}'.format(15))# 채우기 부분을 공백으로 넣어도 됨
print('{0:>10}'.format(15))# 채우기 부분을 공백으로 넣어도 됨
print('{0:x>10}'.format(15))# 채우기 부분을 공백으로 넣어도 됨

# 7) 금액에서 천단위로 콤마 넣기: format(숫자,',')
print(format(149780,','))
print('%20s' % format(1459300,','))
print('{0:,}'.format(14963000))
print('{0:>20,}'.format(14953000))
print('{0:0>20,}'.format(14953000))

# 8) raw문자열 사용하기 
# 문자열 앞에 r 또는 R을 붙이면 raw문자열이 됩니다. 
# 이 raw문자열은 이스케이프 시퀀스를 그대로 저장할때 사용됩니다.
# 즉, \\을 \로 두번 쓰지 않고 한번만 써도 됩니다. 
