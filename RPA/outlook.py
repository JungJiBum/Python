import win32com.client

def send_mail(to,subject,content,atch=[]):
    # outlook obj model 불러오기
    new_Mail = win32com.client.Dispatch("Outlook.Application").CreateItem(0)

    # 메일 수신
    new_Mail.To = to
    # 메일 참조
    # new_Mail.CC = "mail-add-for-cc@testadd.com"
    # 메일 제목
    new_Mail.Subject = subject
    # 메일 내용
    new_Mail.HTMLBody = content

    # 첨부파일 추가
    if atch:
        for file in atch:
            new_Mail.Attachments.Add(file)
    
    # 메일 발송
    print("메일발송전")
    new_Mail.Send()
    print("메일발송후")




if __name__ =="__main__":

    to = "dlflsp153@tfo.co.kr"
    subject = "python to outlook TEST"
    content = """
    <h1>테스트 '메일' 입니다.</h1>
    <h2>테스트 '메일' 입니다.</h2>
    <h3>테스트 '메일' 입니다.</h3>
    <h4>테스트 '메일' 입니다.</h4>
    <h5>테스트 '메일' 입니다.</h5>
    <h6>테스트 '메일' 입니다.</h6>
    <p> p 태그</p>
    <br> br 태그 </br>    
    """

    send_mail(to, subject, content)