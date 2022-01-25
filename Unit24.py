# Unit24: 문자열 응용하기 
# 1) 문자바꾸기
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))
# 2) 문자열 분리하기: split()는 분리해서 list로 만든다. 
print('apple pear grape '.split())
# 3) 구분자 문자열과 문자열 리스트 연결하기: join(리스트)
print('-'.join(['apple', 'pear', 'grape']))
# 4) 소문자를 대문자로 바꾸기: upper() vs lower()
# 5) 공백 삭제하기: lstrip(), rstrip(), strip()
# 6) 특정문자 삭제하기: lstrip(',.'), rstrip(',.'), strip(',.')
# 예시 
import string
print(', python. '.strip(string.punctuation + ' '))
print(string.punctuation)
print(', python. '.strip(string.punctuation).strip())
print(', python. '.strip(',.').strip()) # 왜.사라지지 않는가?
# 7) 문자열을 정해진 칸맞춰서 정렬하기: ljust(10), rjust(10), center(10)왼쪽을더많이비움
print('python'.ljust(10))
print('python'.rjust(10))
print('python'.center(10))

# 8) 메서드 체이닝(method chaining): 문자열method는 처리한 결과를 반환하기 때문에 method chaining가능.
print('pyhton'.rjust(10).upper())
# 또다른 예시: input().split()도 input()이 반환한 문자열에 split을 호출하는 메서드 체이닝입니다. 

# 9) 문자열 왼쪽에 0 채우기: zfill(길이)
#  a) 문자열길이가 zfill의 길이보다 길다면, 문자열 그대로 출력
#  b) 문자열의 소수점은 하나의 문자로 인식하여 zfill길이를 맞춤.
print('hello'.zfill(10))
print('hello'.zfill(3))
print('35'.zfill(6))
print('3.5'.zfill(6))

# 10) 문자열 위치 찾기: find('찾을문자열')
print('apple pineapple'.find('ap'))
print('apple pineapple'.find('pl'))
print('apple pineapple'.find('xy')) # 찾을문자열이 없는 경우는 -1임. 
# 11) 오른쪽에서 부터 문자열 위치 찾기: rfind('찾을문자열')
# 동일한 문자열이더라도 오른쪽에 있는 문자열을 찾게되고, 리턴은 위치자리수를 함(왼쪽자리0을 기준으로 계산)
print('apple pineapple'.rfind('pl'))
print('apple pineapple'.find('xy')) # 찾을문자열이 없는 경우는 -1임. 