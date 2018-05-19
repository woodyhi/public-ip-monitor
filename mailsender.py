import configparser
import smtplib
from email.header import Header
from email.mime.text import MIMEText

import logger


def send_ssl(smtp_server, smtp_port, from_user, from_password, receiver, subject, content):
    """
    SSL加密

    :param smtp_server: smtp服务器
    :param smtp_port: # smtp服务器端口
    :param from_user: # 发件人邮箱账号
    :param from_password: # 发件人邮箱密码
    :param receiver: # 收件人
    :param subject: 主题
    :param content: 内容
    :return:
    """

    msg = MIMEText(content, 'plain', )
    msg['from'] = Header(from_user)
    msg['to'] = Header(receiver)
    msg['subject'] = Header(subject)

    try:
        smtpObj = smtplib.SMTP_SSL(smtp_server, smtp_port)
        smtpObj.set_debuglevel(1)
        smtpObj.login(from_user, from_password)
        smtpObj.sendmail(from_user, receiver, msg.as_string())
        return True
    except smtplib.SMTPException as e:
        logger.log(e)
        return False


def send_starttls(smtp_server, smtp_port, from_user, from_password, receiver, subject, content):
    """
    STARTTLS加密

    :param smtp_server: smtp服务器
    :param smtp_port: # smtp服务器端口
    :param from_user: # 发件人邮箱账号
    :param from_password: # 发件人邮箱密码
    :param receiver: # 收件人
    :param subject: 主题
    :param content: 内容
    :return:
    """

    msg = MIMEText(content, 'plain', )
    msg['from'] = Header(from_user)
    msg['to'] = Header(receiver)
    msg['subject'] = Header(subject)

    try:
        smtpObj = smtplib.SMTP(smtp_server, smtp_port)
        smtpObj.starttls() # 只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接
        smtpObj.set_debuglevel(1)
        smtpObj.login(from_user, from_password)
        smtpObj.sendmail(from_user, receiver, msg.as_string())
        return True
    except smtplib.SMTPException as e:
        logger.log(e)
        return False


if __name__ == '__main__':
    # test
    config = configparser.ConfigParser()
    config.read('config.ini')

    smtphost = config['smtp']['SmtpHost']
    port = config['smtp']['Port']
    user = config['smtp']['User']
    pwd = config['smtp']['Password']

    receiver = config['smtp']['Receiver']
    subject = '出塞' # 主题
    content = '''
    你好：

        秦时明月汉时关，万里长征人未还。
        但是龙城飞将在，不教胡马度阴山。

    好好学习
    '''

    if send_starttls(smtphost, port, user, pwd, receiver, subject, content):
        print("send mail successfully")