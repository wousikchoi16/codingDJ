# Unit 12: 딕셔너리 사용 
# 1) 키,값
# - 딕셔너리 키: 문자열, 정수, 실수, bool (리스트, 딕셔너리 x)
# - 딕셔너리 값: 문자열, 정수, 실수, bool + 리스트,딕셔너리
# - *키의 개수: len(딕셔너리)
# 2) 생성: x={}, x=dict()
# 예시: dict(키1=값1, 키2=값2)      dict(zip([키1,키2],[값1,값2])) 
# 예시: dict([(키1,값1),(키2,값2)]) dict({키1:값1, 키2:값2})
# 3) 키 (not) in 딕셔너리 
# 예시: lux = {'health': 490} 'heal' not in lux -> False
# 4) key가 중복되면 가장 뒤에 있는 값만 사용함. 
# lux = {'health': 490, 'health': 800}
# print(lux)

# 12.5 심사문제 
x = list(input().split())
y = map(float,list(input().split()))
d = dict(zip(x,y))
print(d)

