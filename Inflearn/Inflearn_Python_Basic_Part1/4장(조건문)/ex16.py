# 중첩 (nested) if ~ else 구문

appleQuality = input("사과 상태 입력(신선, 이상) : ")


if appleQuality == "신선":
    applePrice = int(input("사과 1개당 가격을 입력하세요 : "))
    if applePrice < 1000: # 중첩 if 구문
        print("10개를 산다.")
    else:
        print("5개를 산다.")
else:
    print("사과를 사지 않는다.")