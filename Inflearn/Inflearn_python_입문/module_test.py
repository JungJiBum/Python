# 모듈 사용 실습

import sys
import time

print(sys)
print(sys.path)
print(type(sys.path))


# 모듈 경로 삽입

sys.path.append('C:/math')

# for i,j in enumerate(sys.path):
#     print(i,j)


# import test_module
from chap06_02 import add
# print(test_module.power(10,3))
print(add(10,10))

