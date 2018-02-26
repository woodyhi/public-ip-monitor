import configparser

import mailsender
import ip_util
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
    if (result):
        logger.log('邮件发送成功')
        return True
    else:
        logger.log(result)
        logger.log('邮件发送失败')
        return False


def main():
    """
    程序入口
    """

    external_ip_info = ip_util.get_external_ip_info();
    now_ip = ip_util.find_ip(external_ip_info)
    if ip_util.is_ip_changed(now_ip):
        if send_mail('public-ip', external_ip_info):
            ip_util.cache_ip(now_ip)


if __name__ == '__main__':
    main()