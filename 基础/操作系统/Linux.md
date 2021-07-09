# **8.网络编程**

常用网络相关命令和配置文件

计算机网络基础知识

套接字编程

域名解析

# **7.信号与管道**

信号与管道是两种传统的进程的通信方式

信号

信号的产生

信号的响应

信号集

管道

创建管道

管道通信

# **6.线程控制与通信**

## **1.线程控制**

创建线程

获取线程ID

线程等待

线程退出

## **2.线程通信**

实现共享资源访问时的同步和互斥

互斥锁

条件变量

信号量

读写锁

# **5.进程控制与通信**

## **1.进程控制**

获得进程号

创建进程

执行进程

等待进程

结束进程

## **2.进程通信**

System V 信号量

System V 共享内存

System V 消息队列

# **4.Shell编程**

####    **（1）输入输出重定向**

####    **（2）特殊符号**

####    **（3）执行**

####    **（4）shell变量**

（5）输入输出

（6）条件测试

（7）字符串比较

（8）算数比较

（9）文件测试

（10）逻辑运算

（11）算数运算

（12）if语句

（13）case语句

（14）for语句

（15）while语句

（16）until语句

（17）break，continue

（18）shell函数

# **3.Linux程序设计**

1.GCC编译

​	(1)编译过程

​	(2)基本用法 

​		-o，-c，-g，-S，-I，-L，-l，-w，-Wall

​		*注意：*有多个头文件路径，多个自定义库路径时，要依次使用这个选项

---

###  **2.Makefile文件**

---

 ### **3.GDB调试**

---

 ### **4.静态库和动态库**

---

### **5.命令行参数**

---

### **6.环境变量**

---

### **7.时间管理**

---

### **8.错误处理**

---

### **9.标准I/O与文件I/O**

---



# **2.Linux文件与目录**

### **1.Linux目录结构**

------

### **2.文件系统**

​	（1）操作系统使用一个新的设备文件时，要先进行“格式化”——建立			文件系统。建立初始的数据结构。

​	 	inode——df -i，ls -i

​		引导块，超级块，索引节点表，数据区块

​	（2）文件类型

​		cat 符号链接——输出链接的目标文件的内容

​		符号链接内存放的是目标文件的路径

​	（3）文件访问权限

​		三种表示方法（字母，数字，符号常量）

​		setuid,setgid,sticky

​		inode中st_mode的每位代表的含义

​	（4） Linux下文件的扩展名

​	 （5）常见文件系统

​	 （6）Linux虚拟文件系统

​	 （7）相对路径与绝对路径

---

### **3.Linux版本**

​	uname，内核版，发行版

---

### **4.Linux分区**

​	挂载点

​	 IDE硬盘——“hdx1”

​	 SCSI硬盘——“sdx1”

​	 分区：Swap——相当于Windows中的虚拟内存

### **5.awk -F:'{print $1,"|",$3}' /etc/passwd——有问题**

​		`awk -F  ':'  '{print $1,"|",$3}' /etc/passwd`

---

### **6.ppt与pptx的区别**

---

### **7.Linux基本组成**

---

### **8.Linux内核组成**

---

### **9.Yum,apt-get,/etc/source.list**

---

### **10.系统调用，库函数**

---

### **11.vi编辑器**

​	（1）三种状态

​	（2）vi模式下的常用命令

​			/字符串，n，N，：数字，：set number，dd，yy，p

​			nG，：set nu，：set nonu，u，. ，：m，n w file

​	（3）`[range]  s/pattern/string/[cegi]`

​			1,7    1,$   1,.   .,.+10

​		(4):wq，：q！，q，：w，：w 文件名

---

### **12.Linux常用命令**

​	man，pwd，stat，ls，cd，cat，more，less，mkdir，touch，cp，	rm，rmdir，useradd，passwd，groupadd，groupdel

​      ` (1)sudo useradd tom -m -d ~/work/tom`

​	   `(2) sudo passwd tom`

​	  `(3) sudo groupadd student`

*问题：*

![问题](/home/qzj/Pictures/2019-11-30-1.png)

​	(4)切换用户：`su tom`

​	（5）使用userdel -r 时，不允许删除，关掉终端？



---

### **13.Linux基本文件操作命令**

​	mv，ln，grep，sort，uniq，conn，diff，wc，find，chmod，chown，tar，gzip

---

### **14.进程命令**

​	ps，kill

---

### **15.atime，mtime，ctime**

​	atime：最后一次访问时间

​	mtime：最后一次更改文件内容的时间，vi后wq

​	ctime：最后一次更改文件属性的时间，文件大小，权限等

​				vi后，输入内容，更改了文件大小，atime，ctime和mtime都被				更改。

​				touch 三个时间都被更改

---

### **16.文件基础操作**

（1）打开/创建文件

​	`int open(const char* pathname,int flags);`

​	`int open(const char* pathname,int flags,mode_t mode);`

​	`int creat(const char* pathname,mode_t mode);`

​	返回：最小文件描述符

​	flags：打开方式

​				常见打开方式：O_RDONLY,O_WRONLY,O_RDWR,O_CREAT,O_EXCL,O_APPEND

​	mode：创建文件时，新文件的访问权限

​	打开文件后，内存中的三个数据结构：

​							文件描述符表，文件表，内存inode表

​	（2）读文件

​		`ssize_t read(int fd，void* buf，size_t count)；`

​	（3）写文件

​		`ssize_t write(int fd，const void *buf，size_t count)；`

​	（4）文件定位

​	  `off_t lseek(int fd，off_t offset，int whence)；`

​		whence：SEEK_SET，SEEK_CUR，SEEK_END

（5）关闭文件

​	`int close(int fd);`

---

### **17.文件访问的同步 **

`void sync(void);`

`int fsync(int fd);`

`int fdatasync(int fd);`

---

### **18.获得文件属性**

（1）

​		`int stat(const char* file_name，struct stat* buf);`

​		`int fstat(int filedes，struct stat* buf)；`

​		`int lstat(const char* file_name，struct stat* buf)；`

（2）判断文件类型（2种）

（3）判断文件权限

（4）判断setuid,setgid,sticky权限

---

### **19.通过用户/组ID获得用户/组的信息**

`struct passwd* getpwuid(uid_t uid);`

`struct group* getgrgid(gid_t gid);`

---

### **20.符号链接与硬链接**

(1)区别

（2）相关系统调用

`int link(char* pathname1,char* pathname2);`

​	`int unlink(char* pathname);`

`int symlink(char* actualpath,char* sympath);`

`int readlink(char* pathname,char* buf,int bufsize);`

---

### **21.dup/dup2**

`int dup(int oldfd);`

`int dup2(int oldfd,int newfd);`

### **22.文件属性的修改**

(1)修改文件所有者及所属组

​	`int chown(const char* path,uid_t owner,gid_t group);`

​	`int fchown(int fd,uid_t owner,gid_t group);`

​	`int lchown(const char* path,uid_t owner,gid_t group);`

(2)改变文件访问权限

​	`int chmod(const char* path,mode_t mode);`

​	`int fchmod(int fd,mode_t mode);`

(3)改变文件时间

​	`int utime(const char* filetime,struct utimbuf* buf);`

(4)改变文件长度

​	`int truncate(const char* path,off_t length);`

​	`int ftruncate(int fd,off_t length);`

---

### **23.目录相关操作**

​	（1）打开目录

​			`DIR* opendir(const char* name);`

​	（2）读目录

​			`struct dirent* readdir(DIR* dir);`

​	（3）关闭目录

​			`int closedir(DIR* dir);`

​	（4）切换目录

​			`int chdir(const char* path);`

​			`int fchdir(int fd);`

​	（5）创建目录

​			`int mkdir(const char* pathname,mode_t mode);`

​	（6）删除目录

​			`int rmdir(const char* pathname);`

​	（7）目录定位指针

​		`off_t telldir(DIR* dir);`

​		`void seekdir(DIR* dir,off_t offset);`

​		`void rewinddir(DIR* dir);`

---

# **1.Linux 简介**

## Linux体系结构

## Linux内核组成

## Linux分区

## Linux版本

## 库函数和系统函数

---

