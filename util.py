import os
import urllib
from http import cookiejar

import logger
import query_ip

ip_cache_path = "ip.cache"  # 保存IP到本地的路径


def http_opener(head={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    """
    create http opener

    :param head:
    :return:
    """
    cj = cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        item = (key, value)
        header.append(item)
    opener.addheaders = header
    return opener


def is_ip_changed(now_ip):
    if os.path.exists(ip_cache_path):
        cache_file = open(ip_cache_path, "r+", encoding='utf-8')
        cache_ip = cache_file.read()
        cache_file.close()

        if now_ip == cache_ip:
            logger.log("IP地址没变，不发送邮件通知")
            return False
        else:
            logger.log("IP地址已改变")
            return True
    else:
        logger.log("IP地址缓存不存在")

    return True


def cache_ip(ip):
    cache_file = open(ip_cache_path, "w+", encoding='utf-8')
    cache_file.write(ip)
    cache_file.close()
    logger.log("IP地址已缓存")


if __name__ == '__main__':
    # cachefilepath = "cache_ip.txt" # 保存

    ip_info = query_ip.query()
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
