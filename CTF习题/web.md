## 1.攻防世界

### 2.robots

[Robots协议（爬虫协议、机器人协议）](https://www.cnblogs.com/sddai/p/6820415.html)

站点下会有robots.txt

于是

![image-20200327221622463](/home/qzj/.config/Typora/typora-user-images/image-20200327221622463.png)

然后

![image-20200327221653261](/home/qzj/.config/Typora/typora-user-images/image-20200327221653261.png)

### 3.backup

[备份文件](https://mayi077.gitee.io/2020/03/04/%E5%A4%87%E4%BB%BD%E6%96%87%E4%BB%B6/)

![image-20200327221808291](/home/qzj/.config/Typora/typora-user-images/image-20200327221808291.png)

输入`index.php.bak`后

![image-20200327222455087](/home/qzj/.config/Typora/typora-user-images/image-20200327222455087.png)

使用文本编辑器打开

![image-20200327222521753](/home/qzj/.config/Typora/typora-user-images/image-20200327222521753.png)

### 4.cookie

![image-20200327224549435](/home/qzj/.config/Typora/typora-user-images/image-20200327224549435.png)

![image-20200327224612064](/home/qzj/.config/Typora/typora-user-images/image-20200327224612064.png)

然后

![image-20200327224656720](/home/qzj/.config/Typora/typora-user-images/image-20200327224656720.png)

抓包，查看响应

![image-20200327224757100](/home/qzj/.config/Typora/typora-user-images/image-20200327224757100.png)

### 5.disabled_button

![image-20200328111206474](/home/qzj/.config/Typora/typora-user-images/image-20200328111206474.png)

查看页面源代码

![image-20200328111242217](/home/qzj/.config/Typora/typora-user-images/image-20200328111242217.png)

最初增加true，false都不行，最后删除这个属性，再点击

![image-20200328111340092](/home/qzj/.config/Typora/typora-user-images/image-20200328111340092.png)

### 6.weak_auth

![image-20200328111532005](/home/qzj/.config/Typora/typora-user-images/image-20200328111532005.png)

查看页面源代码

![image-20200328111606186](/home/qzj/.config/Typora/typora-user-images/image-20200328111606186.png)

打开check.php后

![image-20200328111708431](/home/qzj/.config/Typora/typora-user-images/image-20200328111708431.png)

随意猜测用户名密码

![image-20200328111818815](/home/qzj/.config/Typora/typora-user-images/image-20200328111818815.png)

真的太。。。。

猜测用户名admin，密码123456

![image-20200328112052425](/home/qzj/.config/Typora/typora-user-images/image-20200328112052425.png)

### 7.simple_php

[PHP  浅谈 == 和=== 中，数字和字符串比较的问题。](https://blog.csdn.net/auuuuuuuu/article/details/79621635)

[PHP is_numeric() 函数](https://www.runoob.com/php/php-is_numeric-function.html)

![image-20200328112157154](/home/qzj/.config/Typora/typora-user-images/image-20200328112157154.png)

直接在搜索框中输入

![image-20200328113801865](/home/qzj/.config/Typora/typora-user-images/image-20200328113801865.png)

### 9.xff_referer

[http中的XFF（X-Forwarded-For）](https://blog.csdn.net/wssmiss/article/details/96719215)

![image-20200328121009455](/home/qzj/.config/Typora/typora-user-images/image-20200328121009455.png)

![image-20200328121055878](/home/qzj/.config/Typora/typora-user-images/image-20200328121055878.png)

### 10.webshell

[webshell利用原理](https://blog.csdn.net/Jack0610/article/details/88087703)

[中国菜刀使用简介](https://www.cnblogs.com/RM-Anton/p/9445680.html)

[CTF-web 第十部分  webshell基础与免杀](https://blog.csdn.net/iamsongyu/article/details/84104397)

![image-20200328123500519](/home/qzj/.config/Typora/typora-user-images/image-20200328123500519.png)

使用菜刀

![image-20200328123606022](/home/qzj/.config/Typora/typora-user-images/image-20200328123606022.png)

![image-20200328123658130](/home/qzj/.config/Typora/typora-user-images/image-20200328123658130.png)

![image-20200328123713750](/home/qzj/.config/Typora/typora-user-images/image-20200328123713750.png)

## 2.i春秋

### 1.爆破-1

[$_REQUEST](https://www.php.net/manual/zh/reserved.variables.request.php)

[preg_match](https://www.php.net/manual/zh/function.preg-match.php)

[var_dump](https://www.php.net/var_dump)

[$GLOBALS](https://www.php.net/manual/zh/reserved.variables.globals.php)

[php变量前加两个$是什么意思?](https://zhidao.baidu.com/question/495400125864413524.html)

![image-20200328205401213](/home/qzj/.config/Typora/typora-user-images/image-20200328205401213.png)

![image-20200328205435338](/home/qzj/.config/Typora/typora-user-images/image-20200328205435338.png)

![image-20200328210550476](/home/qzj/.config/Typora/typora-user-images/image-20200328210550476.png)

### 2.爆破-2

[file_get_contents](https://www.php.net/function.file-get-contents)

![image-20200328210806962](/home/qzj/.config/Typora/typora-user-images/image-20200328210806962.png)

![image-20200328211532548](/home/qzj/.config/Typora/typora-user-images/image-20200328211532548.png)

![image-20200328211553725](/home/qzj/.config/Typora/typora-user-images/image-20200328211553725.png)