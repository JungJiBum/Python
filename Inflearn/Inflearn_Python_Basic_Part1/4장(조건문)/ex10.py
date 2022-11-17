# 쇼핑몰에서 물건을 구매할때 구입액이 5만원 이상이면 5%의 할인을 해준다고 하자.
# 사용자에게 구입금액을 입력받아 최종적으로 할인금액과 지불 금앨을 출력하는 프로그램 만들기

total_price = int(input("구입 금액을 입력하세요 : "))

if total_price >= 50000:
    discount = total_price * 0.05 # 할인 금액
    sales_price = total_price - discount # 지불 금액
    print(f"구입금액은 {total_price}원 이며, 할인금액은 {discount}원 입니다. 총 지불 금액은 {sales_price} 원 입니다.")
else:
    print("할인 금액 대상이 아닙니다.",total_price,"원을 결제해주세요.")

