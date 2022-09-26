import pandas as pd
import pymysql

class DB_CONNECT:

    def __init__(self,host,database,username,password):
        print("생성자 호출됨")
        self.host = host
        self.database = database
        self.username = username
        self.password = password
        self.charset = 'utf8'
        self.cursorclass = pymysql.cursors.DictCursor

    def print_infO(self):
        print(f"입력 정보 : host : {host}, DB : {db}, name : {id}, pw : {pw}")
    

    def query(self,code):
        con = pymysql.connect(host = self.host,
        user=self.username,
        password=self.password,
        db=self.database,
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
        
        cur = con.cursor()
        
        cur.execute(code)
        rows = cur.fetchall()
        df_rows = pd.DataFrame(rows)
        print(df_rows)

        # con.close()
        print("연결종료")


host,db,id,pw = input("정보 입력 : ").split()


test = DB_CONNECT(host,db,id,pw)
# test.print_infO()
test.query(input("명령어 입력 : "))
