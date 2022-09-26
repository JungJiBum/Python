#반복문
#[1] 0 ~ 9까지 출력
# 가로 출력
# for i in range(10):
#     print(i,end= '\t')

print("\n")
#[2]가로 출력 , 표시

# n = 0
# for i in range(10):
#     if i < 9:
#         print(i, end=', ')
#     else:
#         print(i)
#     # n += 1

#[3] 4부터 21까지 홀수들의 합
# num = 0
# for i in range(4, 22):
#     if i % 2 == 1:
#         num += i
# print(num)

#[4] 짝수 1~100 반복문
# for i in range(1, 101):
#     if i %2 ==0:
#         print(i, end=" ")

# print("\n")

# for i in range(2, 101, 2):
#     print(i, end=" ")


#[5] 구구단
# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i} * {j} = {i*j}")
#     print()

#[6] 리스트 요소 반복 출력
# lst = ['dog','hippo','elephant','lion','tiger','alligator']
# cnt = len(lst)
# for i in lst:
#     print(i,end= "\t")
# print(f"총 {cnt}개의 요소")

#[7] 리스트 거꾸로
# lst = ['dog','hippo','elephant','lion','tiger','alligator']

# for i in lst[::-1]:
#     print(i, end = "\t")

# print()

# for i in reversed(lst):
#     print(i, end= "\t")


# for i in lst:
#     for j in reversed(i):
#         print(j, end = " ")
#     print()