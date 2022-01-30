# Unit 28: 회문판별과 N-gram만들기 
# 28.1 회문 판별하기

# 1) 반복문으로 문자검사하기 
# word = input("단어를 입력하세요")
# is_palindrome = True
# for i in range(len(word)//2):
#     if word[i] != word[-1-i]:
#         is_palindrome = False
#         break
# print(is_palindrome)

# 2) 시퀀스 뒤집기로 문자 검사하기 
# word = input("단어를 입력하세요")
# print(word == word[::-1])

# 3) 리스트와 reversed 사용하기 
# word = 'level'
# print(list(word) == list(reversed(word)))
# print(word == ''.join(reversed(word)))

# 28.2 N-gram만들기
# 1) 반복문으로 2-gram만들기
# text = 'hello'
# for i in range(len(text)-1):
#     print(text[i],text[i+1],sep='')
# 2) zip으로 2-gram만들기
#  - zip함수는 반복 가능한객체의 각요소를 튜플로 묶어줌
#    모자른 자리는 묶지 않는다. 
# text = 'hello'
# two_gram = zip(text, text[1:]) 
# for i in two_gram:
#     print(i[0],i[1],sep='')
# # 3) zip으로 3-gram만들기
# text = 'hello'
# three_gram = zip(text, text[1:], text[2:]) 
# for i in three_gram:
#     print(i[0],i[1],i[2], sep='')
# text = 'hello'
# a = list(zip(*[text[i:] for i in range(3)]))
# print(a)
# # 기타) zip사용 
# print(list(zip(['abc','erf','oip','ijn'])))
# print(list(zip(['a,b,c','e,r,f','o,i,p','i,j,n'])))
# print(list(zip(*['abc','erf','oip','ijn'])))

# 연습문제 28.3
n = int(input())
text = input()
words = list(text.split(' '))
if len(words)<n:
    print('wrong')
else:
    n_gram = zip(*[words[i:] for i in range(n)]) 
    for i in n_gram:
        print(i)



