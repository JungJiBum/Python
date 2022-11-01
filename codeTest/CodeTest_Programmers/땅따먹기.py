input_land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]



# def solution(land):
#     for i in range(0,len(land)):
#         for j in range(len(land[0])):
        #     print(land[i][j])
        # print("=====")
        
            
# print(solution(input_land))

for i in range(len(input_land)):
    for j in range(len(input_land[0])):
        input_land[i][j] = max(input_land[i-1][:j] + input_land[i-1][j+1:])+ input_land[i][j]
    print(input_land[i][j])