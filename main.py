import configparser

import logger
import mailsender
import util
from query_ip import query


def send_mail(subject, content):
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')

    smtphost = config['smtp']['SmtpHost']
    port = config['smtp']['Port']
    user = config['smtp']['User']
    pwd = config['smtp']['Password']

    receiver = config['smtp']['Receiver']
    subject = subject
    content = content

    result = mailsender.send_starttls(smtphost, port, user, pwd, receiver, subject, content)
    if result:
        logger.log('邮件发送成功')
        return True
    else:
        logger.log('邮件发送失败')
        return False


def main():
    """
    程序入口
    """
    ip_dict = query()
    if ip_dict != None:
        now_ip = ip_dict['ip']
        if util.is_ip_changed(now_ip):
            if send_mail('public-ip', ip_dict['info']):
                util.cache_ip(now_ip)
    else:
        print("获取外网IP地址失败")



if __name__ == '__main__':
    main()