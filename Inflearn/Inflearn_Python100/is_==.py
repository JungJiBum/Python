# a = [1,2,3,4,5]
# b= a
# c = [1,2,3,4,5]

# print('[2-1] a is b =',a is b)
# print('[2-2] a is c =',a is c)
# print('[2-3] b is c =',b is c)

# print('[2-1] a == b =',a == b)
# print('[2-2] a == c =',a == c)
# print('[2-3] b == c =',b == c)

# a = 101
# b = 100 + 1
# print('[1-1] a is b', a is b)
# print('[1-2] a == b', a == b)
# c='korea'
# d='korea'

# print('[2-1]c is d',c is d)
# print('[2-2] c == d', c == d)

# e=[1,2,3,4,5]
# f=[1,2,3,4,5]
# print('[3-1] e is f ', e is f)
# print('[3-2] e == f', e == f)

a = "korea"
print( '[1]', a, id(a) )
b = "korea"
print( '[2]', b, id(b) )
print( 'a is b = ', a is b )
b += "!"
print( '[3]', b, id(b) )
print( 'a is b = ', a is b )
c = b[:-1]
print( '[4]', c, id(c) )
print( 'a is c = ', a is c )