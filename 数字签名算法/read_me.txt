pyinstaller --onefile main.py可以生成软件、保存在dist中（-w取消窗口)，build、dist文件夹为pyinstaller生成软件的结果
生成的程序启动需要一段时间，大概一分钟左右。
我是基于python 3.11.5完成的，所需库可以通过requirements安装
本课设主要源码为main.py、windows.py、crypto_functions.py
mian.py主要是启动 GUI 应用程序
windows.py中主要是系统中的各图形化界面、也包括md5计算、文本、字符串等处理
crypto_funtions.py中定义了生成素整数，计算公私钥、签名、验证等函数
test文件夹中是我测试用的文本、测试结果。还有附录A中的文本、结果
也可以通过https://github.com/ZhenWusi/Implementation-of-Digital-Signature-Algorithm查看
生成的软件可以通过https://drive.google.com/drive/folders/1I8PivAoS73HakDHPhP_ssL9GlF1_d7Bv?usp=sharing下载

