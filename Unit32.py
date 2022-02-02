#Unit32 람다표현식 사용하기
# 람다표현식 = 이름없는 함수, 익명함수(anonymous function) 
# 다른 함수의 인수로 넣을 때, 주로 사용함. 
# 예를 들어, map(함수,반복가능한객체), filter(함수,반복가능한객체)에서 함수부분에 사용됨.

# 람다표현식:           lambda 매개변수들:식
# 람다표현식 자체호출:  (lambda 매개변수들:식)(인수들)
# 람다표현식으로 매개변수가 없는 함수 만들기: (lambda:10)() 또는 x=10 (lambda:x)() ->결과 10
# 람다표현식에서 조건부 표현식1: lambda 매개변수들: 식1 if 조건식 else 식2 
# 람다표현식에서 조건부 표현식2: lambda 매개변수들: 식1 if 조건식1 else 식2 if 조건식2 else 식3 
# 주의사항
# 1) 람다표현식 안에 새 변수를 만들 수 없다. 
# 2) 직관적이지 않거나 복잡해지는 경우 def로 작성

# 32.4 연습문제 
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))