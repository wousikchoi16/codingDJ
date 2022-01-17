# Unit 19: 계단식으로 별 출력하기 
# 19.5 연습문제 
# for i in range(5):
#     for j in range(5):
#         if j-i>=0:
#             print('*' ,end='')
#         else:
#             print(' ',end='')
#     print()
# 19.6 심사문제 
# height = int(input('산의 높이:'))
height = 15
for i in range(height):
    for j in range(-height+1,height,1):
        k = i
        if -k<=j<=k: 
            print('*',end='')
        else:
            print(' ', end='')
    print()
