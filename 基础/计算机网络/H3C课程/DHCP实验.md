## DHCP实验

### 实验拓扑

![20210112-14](/home/garlic/Desktop/笔记/图片/20210112-14.PNG)

### 实验需求

1. 按照图示为R1配置IP地址
2. 配置R1为DHCP服务器，提供服务的地址池为`192.168.1.0/24`网段，网关为`192.168.1.254`，DNS服务器地址为`202.103.24.68`，`202.103.0.117`
3. `192.168.1.10-192.168.1.20`为专用地址段，要求不能用于自动分配
4. PC3和PC4都能获取到`192.168.1.0/24`网段的IP地址

------

### 实验解法

1. **R1配置IP地址**

   ![20210112-15](/home/garlic/Desktop/笔记/图片/20210112-15.PNG)

2. **配置R1的DHCP服务**

   *步骤1：在R1上开启DHCP服务*

   ![20210112-16](/home/garlic/Desktop/笔记/图片/20210112-16.PNG)

   *步骤2：创建`1`号地址池，宣告网段`192.168.1.0/24`，网关为`192.168.1.254`，DNS为`202.103.24.68`和`202.103.0.117`*

   ![20210112-17](/home/garlic/Desktop/笔记/图片/20210112-17.PNG)

3. 配置IP地址排除

   　　*分析：被配置为排除的IP地址段，DHCP服务器将不会进行分配。配置排除的命令需要退出到系统视图配置*

   *步骤1：配置IP地址排除段，为`192.168.1.10-192.168.1.20`*

   ![20210112-18](/home/garlic/Desktop/笔记/图片/20210112-18.PNG)

4. 配置PC3和PC4的IP地址为自动获取，然后可以自动获得`192.168.1.0/24`网段的IP地址

   ![20210112-19](/home/garlic/Desktop/笔记/图片/20210112-19.PNG)

   ![20210112-20](/home/garlic/Desktop/笔记/图片/20210112-20.PNG)