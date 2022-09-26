# STEP 1 임포트
from telnetlib import IP
import pandas as pd
import pymysql

class DB_CONNECT:


    #생성자
    def __init__(self,host,database,username,password):
        self.host = host
        self.database = database
        self.username = username
        self.password = password
    
    #출력
    def print_info(self):
        print("=====접속정보=====")
        print(f"HOST : {self.host} / username : {self.username} / password : {self.password}")
    
    # # STEP 2 MySQL Connection 연결
    def connect_db(self):
        con = pymysql.connect(host = self.host,
        user=self.username,
        password=self.password,
        db=self.database,
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
        
        #  STEP 3 Connection 으로부터 Cursor 생성
        cur = con.cursor()

        # STEP 4 SQL문 실행 및 Fetch
        sql = "SELECT * FROM SIGN"
        cur.execute(sql)
        # 데이터 Fetch
        rows = cur.fetchall()
        df_rows = pd.DataFrame(rows)
        print(df_rows)

        # STEP 5 DB 연결 종료
        con.close()
        print("연결종료")
    
    # 테이블 생성
    def create_tbl(self):
        con = pymysql.connect(host = self.host,
        user=self.username,
        password=self.password,
        db=self.database,
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

        cur = con.cursor()
        sql = "create table User_INFO("\
            "Name varchar(10),"\
            "Age int,"\
            "Address varchar(20))"
        cur.execute(sql)
        con.commit()
        con.close()




IP = input("입력 주소 ? : ") 
DB = input("DB 명 ? : ") 
users = input("user명 ? : ") 
pw = input("pw ? : ") 

test = DB_CONNECT(IP,DB,users,pw)
test.print_info()
test.connect_db()
# test.create_tbl() 테이블 생성