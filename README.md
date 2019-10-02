o0o.hk VPN 是动态IP地址，当服务器IP地址变动时，经常会由于域名解析滞后导致无法连接

这里使用一段简单的python程序，查询国外的域名服务器获取IP地址，并修改hosts文件，快速连接VPN

注意：hosts文件中仅仅保留了 localhost 项目，其他都会删除

## 使用方法

1. 安装python，pip，执行pip install requests

2. 建立VPN o0o.hk 服务器名字为 o0o.hk 输入用户名和密码

3. 使用文本编辑器打开 %APPDATA%\Microsoft\Network\Connections\Pbk\rasphone.pbk 
   找到[o0o.hk]把其中的
   ```PreviewUserPw=1 改为 PreviewUserPw=0```
   保存文件
   
4. 把o0ovpn.py放在桌面，单击就可以连接VPN
