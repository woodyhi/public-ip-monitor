import configparser

import logger
import mailsender
import util
import query_ip


def send_mail(subject, content):
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')

    smtphost = config['smtp']['SmtpHost']
    port = config['smtp']['Port']
    user = config['smtp']['User']
    pwd = config['smtp']['Password']

    receiver = config['smtp']['Receiver']
    s = subject
    c = content

    result = mailsender.send_starttls(smtphost, port, user, pwd, receiver, s, c)
    if result:
        logger.log('邮件发送成功')
        return True
    else:
        logger.log('邮件发送失败')
        return False


def template(param):
    content = 'Dear Woody：\n'
    content += param

    content += '''
    
秦时明月汉时关，万里长征人未还。
但是龙城飞将在，不教胡马度阴山。

Best Regards!
'''
    print(content)
    return content


def main():
    """
    程序入口
    """
    ip_dict = query_ip.query()
    if ip_dict is not None:
        now_ip = ip_dict['ip']

        if util.is_ip_changed(now_ip):
            # 构建邮件内容 尽量避免spam
            subject = 'public-ip'  # 主题

            content = template(ip_dict['info'])

            if send_mail(subject, content):
                util.cache_ip(now_ip)
    else:
        print("获取外网IP地址失败")


def main2():
    ip_address = query_ip.check_ip()
    if ip_address is not None:
        if util.is_ip_changed(ip_address):
            # 构建邮件内容 尽量避免spam
            subject = 'public-ip'  # 主题

            content = template(ip_address)

            if send_mail(subject, content):
                util.cache_ip(ip_address)
    else:
        print("获取外网IP地址失败")


if __name__ == '__main__':
    main2()