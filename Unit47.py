#Unit 47: 부록
# 1) 실숫값 오차 
# a) 부동소수점 반올림 오차(rounding error)
# 예시1)
import math, sys
x = 0.1 + 0.2
print(math.fabs(x-0.3)<=sys.float_info.epsilon)
# 예시2) 
print(math.isclose(0.1+0.2, 0.3))
# b) Decimal으로 정확한 자릿수 표현하기 
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.2'))
# 3) Fraction으로 분수 표현하기 
from fractions import Fraction
print(Fraction('10/3'))