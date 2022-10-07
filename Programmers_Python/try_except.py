# text = '100%'

# try:
#     number = int(text)
# except ValueError:
#     print("{}is not number".format(text))

# def safe_pop_print(list,index):
#     # try:
#     if(index<len(list)):
#         print(list.pop(index))
#     # except IndexError:
#     else:
#         print("{} index의 값을 가져올 수 없습니다.".format(index))

# try:
#     import my_module
# except ImportError:
#     print("No Module")

# try:
#     list=[]
#     print(list[0])

#     text='abc'
#     number=int(text)
# except Exception as ex:
#     print('Error',ex)

# def rsp(mine,yours):
#     allowed = ['rock','sissor','paper']
#     if mine not in allowed:
#         raise ValueError
#     if yours not in allowed:
#         raise ValueError

# try:
#     rsp('rock','p')
# except ValueError:
#     print("Wrong input data")

school = {'1반':[172,185,198,177,165,199],'2반':[165,177,167,180,191]}
try:
    for class_number, students in school.items():
        for student in students:
            if student > 190:
                print(class_number,'반에 190 넘는 학생이 있다.')
                raise StopIteration
except StopIteration:
    print("정상 종료")
