# Unit 27 파일 사용하기
# 파일 객체는 이터레이터임. 따라서 unpacking도 가능. 
# file = open('he.txt','r')
# a,b,c = file 
# print(a,b,c)

# 1) 파일에 문자열 쓰기, 열기
# file = open('he.txt','w')
# file.write('Hello world!')
# file.close()

# 2) 파일에서 문자열 읽기
# file = open('he.txt','r')
# s = file.read()
# print(s)
# file.close()

# 3) 자동으로 파일 객체 닫기 
# with open(파일이름,파일모드) as 파일객체:
#   코드
# with open('he.txt','r') as file:
#     s = file.read()
#     print(s)

# 4) 문자열 여러줄을 파일에 쓰기, 읽기 
#  a) 반복문으로 문자열 여러 줄을 파일에 쓰기
# with open('he.txt','w') as file:
#     for i in range(3):
#         file.write('hello, world! {0}\n'.format(i))
#  b) 리스트에 들어있는 문자열을 파일에 쓰기 
#    - writelines를 사용할때에는 반드시 리스트의 각 문자열끝에 개행문자\n을 붙여주어야합니다.
#      그렇지 않으면 문자열이 모두 한줄로 붙어서 저장되므로 주의해야 합니다. 
# lines = ['안녕하세요\n', '파이썬\n','코딩도장입니다.\n']
# with open('he.txt','w') as file:
#     file.writelines(lines)
#  c) 파일의 내용을 한줄씩 리스트로 가져오기 
# with open('he.txt','r') as file:
#     lines = file.readlines()
#     print(lines)
#  d) 파일의 내용을 한줄씩 읽기 
# with open('he.txt','r') as file:
#     line = '초기화'
#     while line != '':
#         line = file.readline()
#         print(line.strip('\n'))
#  e) for반목문으로 파일의 내용을 줄 단위로 읽기 
# with open('he.txt','r') as file:
#     for line in file:
#         print(line.strip('\n'))

# 5) 파이썬 객체를 파일에 저장하기, 가져오기 
#    - 파이썬 객체를 파일에 저장하는 과정을 피클링(pickling)이라고 하고 
#      파일에서 객체를 읽어오는 과정을 언피클링(unpickling)이라고 함. 
#  a) 파이썬 객체를 파일에 저장하기 
# from dataclasses import field
# import pickle 
# name = 'james'
# age = 17
# address = '서울 서초구 반포동'
# scores = {'korean':90, 'english':95, 'math':85, 'science':82}
# with open('james.p','wb') as file: # wb는 바이너스쓰기모드로 열기 
#     pickle.dump(name, file)
#     pickle.dump(age, file)
#     pickle.dump(address, file)
#     pickle.dump(scores, file)
#  b) 파일에서 파이썬 객체 읽기: 저장된 개수를 넘어가면 에러발생 
# import pickle
# with open('james.p','rb') as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#     address = pickle.load(file)
#     scores = pickle.load(file)
#     print(name)
#     print(age)
#     print(address)
#     print(scores)