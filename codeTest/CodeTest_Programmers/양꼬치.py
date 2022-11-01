
def sol(n,k):
    # 꼬치개수 * 꼬치금액 + 음료개수*음료금액 - (서비스음료값(꼬치10개당 1개서비스))
    answer = 12000*n + 2000*k - (n//10 * 2000)
    return answer

print(sol(n=10,k=3))
print(sol(n=64,k=6))