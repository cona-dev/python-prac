# import traval.thailand # class, function은 직접 import 못함
# trip_to = traval.thailand.ThailandPackage()
# trip_to.detail()

from traval import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()


# module의 위치를 알 수 있는 함수 inspect
print("\n >>>>> module의 위치를 알 수 있는 함수 inspect <<<<<")

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))