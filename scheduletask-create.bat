
@echo off
cd /d %~dp0
schtasks /create /tn "PublicIp" /ru system /tr "%~dp0start.bat" /sc hourly /st 00:00
schtasks /run /tn "PublicIp" /i
@rem start %systemroot%\tasks

pause
