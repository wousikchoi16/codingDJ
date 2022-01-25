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
print('{0:>10}'.format('python'))