## H3C配置管理实验

### 实验拓扑

![1](/home/garlic/Desktop/笔记/图片/21.PNG)

### 实验需求

1. 按照图示连接到真机，并配置IP地址（真机IP地址配置到VirtualBox Host-Only Ethernet Adapter网卡）
2. R1保存当前配置
3. 在R1上开启FTP服务
4. 使用真机访问FTP服务，把R1的配置文件拷贝到本地
5. 在R1上清空配置，重启R1，确认已配置为空配状态
6. 再次在R1开启FTP服务，并把真机拷贝的配置文件还原到路由器
7. 更改R1的启动配置文件名
8. 再次重启R1，确认配置已还原

### 实验解法

1.**配置IP地址**

![2](/home/garlic/Desktop/笔记/图片/22.PNG)

![5](/home/garlic/Desktop/笔记/图片/25.PNG)

![3](/home/garlic/Desktop/笔记/图片/23.PNG)

![4](/home/garlic/Desktop/笔记/图片/24.PNG)

2.**R1保存当前配置，并确认，命令如下**

![6](/home/garlic/Desktop/笔记/图片/26.PNG)

1. **R1上开启FTP服务，创建用户`xiaoming`，密码`666666`**

   *步骤1：开启FTP服务*

   ![7](/home/garlic/Desktop/笔记/图片/27.PNG)

   *步骤2：创建用于FTP身份验证的用户，配置密码，并设置用户权限级别和服务类型*

   ![8](/home/garlic/Desktop/笔记/图片/28.PNG)

2. **使用真机访问FTP服务，备份R1的配置文件**

   *步骤1：使用资源管理器访问FTP服务，如图所示*

   ![9](/home/garlic/Desktop/笔记/图片/29.PNG)

   *步骤2：输入用户名和密码，如图所示*

   ![10](/home/garlic/Desktop/笔记/图片/30.PNG)

   *步骤3：复制R1的配置文件，如图所示*

   ![11](/home/garlic/Desktop/笔记/图片/31.PNG)

3. **在R1上清空配置，命令如下**

   ![12](/home/garlic/Desktop/笔记/图片/32.PNG)

4. **重启R1，命令如下**

   ![13](/home/garlic/Desktop/笔记/图片/33.PNG)

   ![14](/home/garlic/Desktop/笔记/图片/34.PNG)

5. **查看R1配置，发现R1的配置已经变成空配状态**

   ![15](/home/garlic/Desktop/笔记/图片/35.PNG)

6. **再次把R1的g0/0口配置IP地址，并开启FTP**

   ![16](/home/garlic/Desktop/笔记/图片/36.PNG)

7. **把真机上的配置文件还原到路由器**

   ![17](/home/garlic/Desktop/笔记/图片/37.PNG)

   ![18](/home/garlic/Desktop/笔记/图片/38.PNG)

8. **更改R1的启动配置文件名，命令如下**

   ![39](/home/garlic/Desktop/笔记/图片/39.PNG)

9. **重启R1，确认配置已经还原到清空前的状态**

   ![40](/home/garlic/Desktop/笔记/图片/40.PNG)

   



