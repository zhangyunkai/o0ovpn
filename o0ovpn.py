# 使用方法
# 1. 安装python，pip，执行pip install requests
# 2. 建立VPN o0o.hk 服务器名字为 o0o.hk 输入用户名和密码
# 3. 使用文本编辑器打开 %APPDATA%\Microsoft\Network\Connections\Pbk\rasphone.pbk 
#  找到[o0o.hk]把其中的
#   PreviewUserPw=1 改为 PreviewUserPw=0
#  保存文件
# 把o0ovpn.py放在桌面，单击就可以连接VPN

import requests
import time
from subprocess import check_output

my_headers = {'Accept' : 'application/dns-json'}
dns_url  = "https://cloudflare-dns.com/dns-query?name=o0o.hk&type=A"
print ("1. 正在查询o0o.hk域名，请稍等")
r = requests.get (dns_url, headers = my_headers)
print ("2. 域名查询返回数据：")
print (r.content)

if r.status_code == requests.codes.ok:
    ret = r.json()
    print ("域名查询IP：" + ret["Answer"][0]["data"])
    print ("3. 修改hosts文件(仅仅保留localhost)")
    fo = open(r"C:\windows\System32\drivers\etc\hosts", "w")
    fo.write( "127.0.0.1 localhost\n")
    fo.write( ret["Answer"][0]["data"] + " o0o.hk" )
    fo.close()
    print("4. 开始连接VPN")
    check_output("rasphone -d o0o.hk", shell=True).decode(encoding='gb2312')
    print("5. VPN连接正常")
    time.sleep(2)
