import smtplib
import ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'rommeldm87@gmail.com'
    password = 'xvvhisqbbdefimkz'
    receiver = 'rommeldm87@gmail.com'
    context = ssl.create_default_context()
#     message = """\
# Subject: Good Morning! Hope Your Having A Wonderful Day
# Hi!
# How are you?
# """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def main():
    pass


if __name__ == '__main__':
    pass
    # main()