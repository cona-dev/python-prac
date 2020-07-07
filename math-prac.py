#abs(), pow(), max(), min(), round()

print(abs(-5)) # 5
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) # 12
print(min(3,12)) #3

print(round(3.14)) # 3
print(round(4.6)) # 5
print(round(4.5)) #4

# math
# floor(), ceil(), sqrt()

from math import *

print(floor(4.99)) #내림, 4
print(ceil(3.14)) #올림, 4
print(sqrt(16)) #제곱근 4 4.0

# ----------------------------------------------------

# random

from random import *

print(random() * 10) # 0.0 ~ 10.0
print(int(random() * 10)) # 0 ~ 10
print(int(random() * 10) + 1) # 1 ~ 10

# ----------------------------------------------------

# 로또 예측하기

print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print(randrange(1, 46)) # 1 ~ 부터 46 미만의 값

