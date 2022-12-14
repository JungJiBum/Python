# csv 파일은 split() 메서드를 이용하여 파싱할 수 있다.
# csv 파일을 읽는 프로그램을 작성해보자.

def main():
    f_name = open(file="c://Temp//sample1.csv",mode="r",encoding='cp949')
    # read() : 파일을 처음부터 끝까지 읽을 때 사용
    # readline() : 파일의 내용을 한줄씩 읽어들일때 사용
    # readlines() : 파일을 읽으면 한 줄 , 한 줄이 각각 리스트 원소로 들어감.

    for line in f_name.readlines():
        line = line.strip()
        print(line, type(line))

        # 한 라인을 단어로 분리한다.
        words = line.split(",")
        for word in words:
            print("  ",word)
    f_name.close()

if __name__ == "__main__":
    main()
