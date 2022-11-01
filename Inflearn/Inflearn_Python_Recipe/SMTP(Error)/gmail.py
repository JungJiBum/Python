import smtplib
from email.mime.text import MIMEText

sendEmail = input("보내는 메일 입력 : ")
recvEmail = input("받는 메일 입력 : ")
password = input("보내는 메일 비밀번호 : ")

smtpName = "smtp.gmail.com" #smtp 서버 주소
smtpPort = 587 # smtp 포트 번호

text = "메일 내용"
msg = MIMEText(text) #MIMEText(text, _charset="utf8")

msg["Subject"] = "이것은 메일 제목"
msg["From"] = sendEmail
msg["To"] = recvEmail
print(msg.as_string())

s = smtplib.SMTP(smtpName,smtpPort) # 메일 서버 연결
s.starttls() # TLS보안처리
s.login(sendEmail,password) # 로그인
s.sendmail(sendEmail,recvEmail,msg.as_string()) # 메일 전송, 문자열로 변환
s.close() # smtp 서버 연결 종료


