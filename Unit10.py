# Unit10 
# 리스트
# - 문자열, 정수, 실수, 불 등 모든 자료형을 저장할 수 있음.
# - 자료형을 섞어서도 저장이 가능함. 
# - 보통 빈 리스트를 만들어 놓은 뒤에 새 값을 추가하는 방식을 사용함. 
# 예시 list(range(값)) list(range(시작,끝)) list(range(시작,끝,증가폭))

# 튜플 
# - 저장된 요소를 변경, 추가, 삭제할 수 없음. 
# - 한개짜리 튜플은 튜플=(값,)  튜플=값, 이렇게 만든다. 
# - 일반적인 튜플은  튜플=(값,값) 튜플=값,값 이렇게 만든다. 
# 예시 tuple(range(값)) tuple(range(시작,끝)) tuple(range(시작,끝,증가폭))

# 튜플 <-> 리스트 변환 가능 
# tuple(a), list(a)
# list/tuple unpacking / packing

# 10.5 심사문제 
step = int(input())
print(tuple(range(-10,10,step)))