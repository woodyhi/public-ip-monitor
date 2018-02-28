
获取外网IP地址并且在IP地址有变化时发送邮件通知

### 编辑config.ini配置邮件
以outlook为例
```
[smtp]
SmtpHost = smtp-mail.outlook.com
Port = 587
User = your@outlook.com
Password = yourpwd
Receiver = dest@xxx.com
```

### windows下设置计划任务执行start.bat
```
start.bat
```