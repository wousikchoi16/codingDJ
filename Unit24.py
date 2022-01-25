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