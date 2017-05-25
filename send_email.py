import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart




def sendmail(Subject,Receivers,Pictures):
    msg = MIMEMultipart('related')
    msg['From'] = email_sender
    msg['Subject'] = Subject
    msg['To'] = Receivers
    Raw_Content=['<html>','</html>']
    for fid,f in enumerate(Pictures):
        print(fid,f)
        with open(f,'rb')as fb:
            img=MIMEImage(fb.read())
            img.add_header('Content-ID','image%s'%fid)
            msg.attach(img)
            Tmp_Content='<img src="cid:image%s"><br>'%fid
            Raw_Content.insert(-1,Tmp_Content)
    Content = MIMEText(''.join(Raw_Content), 'html', 'utf-8')
    msg.attach(Content)
    try:
        server=smtplib.SMTP()
        server.connect('mail.travelzen.com',25)
        server.starttls()
        server.login(email_sender,passwd)
        server.sendmail(email_sender,Receivers,msg.as_string())
        server.quit()
        print('email send sucess')
    except Exception as e:
        print('Error : %s'%e)




if __name__ == '__main__':
    email_sender = 'xuecheng.geng'
    passwd = '123456'
    Receivers = '2394567570@qq.com'
    Subject = 'test pictures mail'
    Pictures = ['tools.jpg', 'someone.jpg']
    sendmail(Subject,Receivers,Pictures)












