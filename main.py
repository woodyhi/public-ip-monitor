import configparser

import mailsender
import util
import logger


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

    external_ip_info = util.get_public_ip_info();
    if external_ip_info != None:
        now_ip = util.find_ip_from(external_ip_info)
        if util.is_ip_changed(now_ip):
            if send_mail('public-ip', external_ip_info):
                util.cache_ip(now_ip)
    else:
        print("获取外网IP地址失败")



if __name__ == '__main__':
    main()