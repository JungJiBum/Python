year = int(input("나이를 입력해주세요 : "))
if year <8:
    yogum = 0
elif year < 13:
    yogum = 500
elif year < 20:
    yogum = 750
else:
    yogum = 1300
print("요금은 {} 입니다.".format(yogum))
won = int(input("버스비를 입력해주세요 : "))
if won >= yogum:
    won = won-yogum
    print("요금지불 완료 잔돈 {} 원".format(won))
else:
    print("버스에 승차할 수 없습니다.")