
# Korea 문자열을 리스트로 변환
# 문자열을 리스트로 변환시 어떻게 처리하는가

# a = 'korea'
# print(a,type(a))

# b = list(a)
# print(b, type(b))

#[1] 함수 작성 --> 리스트를 문자열로 변환 --> join
#------------------------------------------------
def convert_lst_str(str_):
    return '*'.join(str_)
#------------------------------------------------

sample = ['k','o','r','e','a']
print("샘플 값 : ",sample)
rs = convert_lst_str(sample)
print("함수 값 : ",rs)