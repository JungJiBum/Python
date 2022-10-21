a = '■'
row1 = [a,a,a]
row2 = [a,a,a]
row3 = [a,a,a]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("보물을 어디에 둘까?")
x,y = int(position[0]), int(position[1]) # x는 행 y는 열

# selected_row = map[x-1]
# selected_row[y-1]="X"
map[x-1][y-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
