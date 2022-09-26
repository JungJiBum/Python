'''
전체 청구 금액 입력
몇 퍼센트의 팁을 줄건지
몇명이 계산하는지
'''
total_price = float(input("총 금액 : "))
tips = int(input("팁은 10, 12 or 15? : "))
peoples = int(input("몇 명이 계산 ? : "))
pay_tip = tips/ 100 * total_price + total_price
# pay_tip = total_price * ( 1 + tips / 100)
print(pay_tip)
each_pays = round(pay_tip / peoples, 2)
each_pays = "{:.2f}".format(each_pays)

print("총 금액은 : {}이고, 팁은 {}이며, 인원은 {}명으로 각자 낼 금액은 : {}".format(total_price, tips, peoples, each_pays))