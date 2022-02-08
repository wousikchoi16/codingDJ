# Unit37 두점사이의 거리구하기 
# import math
# class Point2D:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# p1 = Point2D(x=30,y=20)
# p2 = Point2D(x=60,y=50)
# print(f'p1:{p1.x},{p1.y}')
# print(f'p2:{p2.x},{p2.y}')
# a = p2.x - p1.x
# b = p2.y - p1.y
# c = math.sqrt((a*a)+(b*b))
# c = math.sqrt((math.pow(a,2))+(math.pow(b,2)))
# print(c)

# 1) namedtuple: 각 요소에 이름을 지정해 줄 수 있는 튜플
# 클래스 = collections.namedtuple('자료형이름',['요소이름1','요소이름2'])
import math
import collections
from sunau import Au_read
Point2D = collections.namedtuple('Point2D',['x','y'])
p1 = Point2D(x=30,y=20)
p2 = Point2D(x=60,y=50)
a = p2.x - p1.x
b = p2.y - p1.y
c = math.sqrt((a*a)+(b*b))
c = math.sqrt((math.pow(a,2))+(math.pow(b,2)))
print(c)

# 37.2 연습문제: 사각형의 넓이 구하기 
class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
rect = Rectangle(x1=20, y1=20, x2=40, y2=30)
width = abs(rect.x2-rect.x1)
height = abs(rect.y2-rect.y1)
area = width * height
print(area)
