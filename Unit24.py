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


