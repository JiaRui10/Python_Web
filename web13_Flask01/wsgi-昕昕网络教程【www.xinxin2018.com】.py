#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname

# 设置当前目录为工作目录
sys.path.insert(0, abspath(dirname(__file__)))

# 引入 app.py
import app

# 必须有一个叫做 application 的变量
# gunicorn 就要这个变量
# 这个变量的值必须是 Flask 实例
# 这是规定的套路(协议)
application = app.app

# 这是把代码部署到 apache gunicorn nginx 后面的套路
"""
➜  ~ cat /etc/supervisor/conf.d/xx.conf

[program:todo]
command=/usr/local/bin/gunicorn wsgi --bind 0.0.0.0:2000 --pid /tmp/todo.pid
directory=/root/web13
autostart=true
"""

# 流程
# apt-get install gunicorn  # 安装服务器
# 要让web程序在gunicorn服务器中跑，要将上面的代码写入xsgi.py文件中
# 运行web程序：gunicorn wsgi --bind 0.0.0.0:2000
#监控web程序（如果程序挂了，也会帮忙重启）
"""
➜  ~ cat /etc/supervisor/conf.d/xx.conf

[program:todo]
command=/usr/local/bin/gunicorn wsgi --bind 0.0.0.0:2000 --pid /tmp/todo.pid
directory=/root/web13
autostart=true
"""
#service supervisor restart
# or
# supervisorctl restart todo