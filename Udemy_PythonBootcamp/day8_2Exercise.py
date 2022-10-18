# 소수 확인하기
# def prime_checker(number):
#     is_prime = True
#     for i in range(2,number):
#         #i = 2 ~ (number-1)
#         if number % i ==0:
#             is_prime=False
#             # 소수아님
#     if is_prime:
#         print(is_prime, "소수임")
#     else:
#         print(is_prime,"소수아님")
    

# n = int(input("Check this number : "))
# prime_checker(number=n)


ls=[3,4,5,6,7,11,12,13,15]
is_prime = True
for i in range(len(ls)):
    for j in range(2,ls[i]):
        # print(f"{ls[i]} % {j} = {ls[i] % j}")
        if ls[i] % j == 0:
            is_prime=False
            #소수인지 판별하는 bool을 초기화를 해줘야되는구나.
    if is_prime:
        print(f"{ls[i]}는 소수")
    else:
        print(f"{ls[i]}는소수x")
    is_prime=True