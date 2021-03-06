import re

from pip._vendor.requests.packages import chardet

import logger
import util


def get_public_ip_info():
    """
    请求ip138来返回外网ip地址和地址信息

    :return:
    """
    url = 'http://2019.ip138.com/ic.asp'

    try:
        opener = util.http_opener()
        response = opener.open(url, timeout=2000)

        # 字节码
        resp_bytes = response.read()

        charset = chardet.detect(resp_bytes)['encoding']

        # 转成字符串
        html = resp_bytes.decode(charset)

        if 'html' in response.getheader('Content-Type'):
            info_reg = r'(?<=<center>).*?(?=</center>)'
            info_all_match = re.findall(info_reg, html, re.S | re.M)
            info = info_all_match[0]
            # logger.log(info)

            ip_reg = r'(?<=\[).*?(?=\])'
            ip_matched = re.findall(ip_reg, info, re.S | re.M)

            dict = {'ip': ip_matched[0], 'info': info}
            return dict

    except Exception as e:
        print(e)
        logger.log(e)


def get_public_ip_info_2():
    url = 'http://ip.chinaz.com'
    try:
        opener = util.http_opener()
        response = opener.open(url, timeout=2000)

        # 字节码
        resp_bytes = response.read()
        # print("A\n")
        # print(resp_bytes)

        charset = chardet.detect(resp_bytes)['encoding']
        # print("B\n")
        # print(charset)

        # 转成字符串
        html = resp_bytes.decode(charset)
        # print(html)

        if 'html' in response.getheader('Content-Type'):
            # 解析html
            # re_comp = re.compile('(?<=<dl class="IpMRig-tit">).*?(?=</dl>)')
            # all_match = re_compfindall(html)

            info_reg = r'(?<=<dl class="IpMRig-tit">).*?(?=</dl>)'
            info_all_match = re.findall(info_reg, html, re.S | re.M)
            info = info_all_match[0]
            # logger.log(info)

            ip_reg = r'(?<=<dd class="fz24">).*?(?=</dd>)'
            ip_matched = re.findall(ip_reg, info, re.S | re.M)

            dict = {'ip': ip_matched[0], 'info': info}
            return dict

    except Exception as e:
        print(e)
        logger.log(e)


def check_public_ip_info():
    url = 'https://checkip.amazonaws.com'
    try:
        opener = util.http_opener()
        response = opener.open(url, timeout=2000)

        # 字节码
        resp_bytes = response.read()
        # print("A\n")
        # print(resp_bytes)

        charset = chardet.detect(resp_bytes)['encoding']
        # print("B\n")
        # print(charset)

        # 转成字符串
        # html = resp_bytes.decode(charset)
        content = str(resp_bytes, charset)
        if content is not None:
            _content = content.replace('\n','')
            if is_ipv4_address(_content):
                return _content

    except Exception as e:
        print(e)
        logger.log(e)


def query():
    ip_dict = get_public_ip_info()
    if ip_dict is None:
        ip_dict = get_public_ip_info_2()

    if ip_dict is not None:
        logger.log(ip_dict)

    return ip_dict


def check_ip():
    ip = check_public_ip_info()
    return ip


def is_ipv4_address(ip):
    """
    精确的匹配给定的字符串是否是IP地址
    """
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
        return True
    else:
        return False


if __name__ == '__main__':
    # cachefilepath = "cache_ip.txt" # 保存

    # ip = query()
    # print(ip)

    # if ip_info != None:
    #     now_ip = find_ip_from(ip_info)
    #
    #     if now_ip != None:
    #         print(now_ip)
    #
    #         if is_ip_changed(now_ip):
    #             cache_ip(now_ip)
    #
    # else:
    #     print("获取外网IP地址失败")
    ip = check_public_ip_info()
    print(ip)
