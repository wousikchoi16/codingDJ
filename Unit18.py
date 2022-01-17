# Unit 18: break, continue로 반복문 제어하기
# break: 제어흐름중단
# continue: 제어흐름유지, 코드 실행만 건너뜀
# break, continue 모두 :(콜론)을 붙이지 않는다. 
# 18.5 연습문제 
i = 0 
while True:
    if i%10 != 3: 
        i += 1
        continue
    if 73 < i:
        break
    print(i,end=' ')
    i += 1
