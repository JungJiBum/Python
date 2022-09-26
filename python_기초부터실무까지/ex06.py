# 초를 입력받아서 시, 분, 초로 변경해보자

time = int(input("초를 입력 : "))

# 60으로 나눈 나머지는 초를 의미
sec = time % 60

# 60으로 나눈 몫을 다시 60으로 나눈 나머지는 분을 의미
min = (time // 60) % 60
#  min = sec % 60

# 60으로 나눈 몫을 다시 60으로 나눈 몫은 시간을 의미
hour = (time // 60) // 60

print(f"입력한 시간은 {time} 이며, sec는 {sec}, min은 {min}, hour은 {hour}")
