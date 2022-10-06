from ctypes import wintypes
from email import message


wintable={
    '가위':'보',
    '바위':'가위',
    '보':'바위'
}

def rsp(mine,yours):
    if mine == yours:
        return 'DRAW'
    elif wintable[mine] == yours:
        return 'WIN'
    else:
        return 'LOSE'

result = rsp('가위','바위')

messages = {
    'WIN':'이겼다.',
    'DRAW':'비겼다.',
    'LOSE': '졌다.'
}

# print(messages[result])

ages = {'Tod':35,'Jane':23,'Paul':62}

for k,v in ages.items():
    print(k,v)
