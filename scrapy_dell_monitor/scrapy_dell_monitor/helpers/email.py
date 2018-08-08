import smtplib


class Email:
    GMAIL_USER = "kuanghaochina@gmail.com"
    GMAIL_PASSWORD = "!Kh59851800"

    def __init__(self):
        self.sent_from = self.GMAIL_USER
        self.__init_server()

    def __init_server(self):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.server.ehlo()
        self.server.login(self.GMAIL_USER, self.GMAIL_PASSWORD)

    def __del__(self):
        try:
            self.server.close()
        except:
            pass

    def send(self, to, subject, content):
        try:
            self.server.sendmail(self.sent_from, to, content)
        except:
            pass
