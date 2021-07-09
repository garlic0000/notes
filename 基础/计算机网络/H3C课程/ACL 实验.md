## ACL 实验

### 实验拓扑

![acl-1](/home/garlic/Desktop/笔记/图片/acl-1.PNG)

### 实验需求

1. 按照图示配置 IP 地址
2. 全网路由互通
3. 在 SERVER1 上配置开启 TELNET 和 FTP 服务
4. 配置 ACL 实现如下效果
   1. `192.168.1.0/24` 网段不允许访问 `192.168.2.0/24` 网段，要求使用基本 ACL 实现
   2. PC1 可以访问 SERVER1 的 TELNET 服务，但不能访问 FTP 服务
   3. PC2 可以访问 SERVER1 的 FTP 服务，但不能访问 TELNET 服务
   4. `192.168.2.0/24` 网段不允许访问 SERVER1，要求通过高级 ACL 实现

------

### 实验解法

1. **配置 IP 地址**

     ![acl-2](/home/garlic/Desktop/笔记/图片/acl-2.PNG)

     ![acl-3](/home/garlic/Desktop/笔记/图片/acl-3.PNG)

     ![acl-4](/home/garlic/Desktop/笔记/图片/acl-4.PNG)

     ![acl-5](/home/garlic/Desktop/笔记/图片/acl-5.PNG)

     ![acl-6](/home/garlic/Desktop/笔记/图片/acl-6.PNG)

     ![acl-7](/home/garlic/Desktop/笔记/图片/acl-7.PNG)

     ![acl-8](/home/garlic/Desktop/笔记/图片/acl-8.PNG)

2. **R1，R2，R3 上配置 RIP 使全网路由互通**

     ![acl-10](/home/garlic/Desktop/笔记/图片/acl-10.PNG)

     ![acl-11](/home/garlic/Desktop/笔记/图片/acl-11.PNG)

     ![acl-12](/home/garlic/Desktop/笔记/图片/acl-12.PNG)

     ![acl-13](/home/garlic/Desktop/笔记/图片/acl-13.PNG)

3. **在 SERVER1 上配置开启 TELNET 和 FTP 服务**

     ![acl-14](/home/garlic/Desktop/笔记/图片/acl-14.PNG)

4. **配置 ACL 部分**

   *分析：需求 i，要求 `192.168.1.0/24` 网段不允许访问 `192.168.2.0/24` 网段，只能使用基本 ACL 实现。基本 ACL 只过滤源 IP 地址，只能在 R2 的 g0/2 接口上配置出方向包过滤来实现。如果配置在两个网段沿途的其他位置，将会影响到 `192.168.1.0/24` 网段和其他网段的正常通讯
      　　需求 ii，PC1 可以访问 SERVER1 的 TELNET 服务，但不能访问 FTP 服务。既然要过滤指定的服务，就只能使用高级 ACL，高级 ACL 不会造成误过滤，所以可以配置在离源地址最近的接口的入方向，也就是 R1 的 g0/1 接口的入方向。另外，由于 H3C 的 ACL 用于包过滤默认动作是允许，所以并不需要专门配置允许 PC1 访问 SERVER1 的 TELNET，只需要配置拒绝访问 FTP 的规则即可
      　　需求 iii，PC2 可以访问 SERVER1 的 FTP 服务，但不能访问 TELNET 服务。同理，只能使用高级 ACL，配置在 R1 的 g0/1 接口的入方向。而且也只需要配置拒绝访问 TELNET 的规则即可
      　　由于需求 i 和需求 ii 配置在同一个路由器同一个接口的同方向，所以把规则写入到同一个 ACL 即可
      　　需求 iv：`192.168.2.0/24` 网段不允许访问 SERVER1，要求通过高级 ACL 实现。高级 ACL 不会造成误过滤，所以可以配置在离源地址最近的接口的入方向，也就是 R2 的 g0/2 接口的入方向。另外，没有明确说明不允许访问什么服务，就是所有都不允许访问，所以高级 ACL 中的协议需要指定为 IP 协议*
      　　
   *步骤 1：创建基本 ACL，使 `192.168.1.0/24` 网段不能访问 `192.168.2.0/24` 网段，并在 R2 的 g0/2 接口的出方向配置包过滤*

   ![acl-16](/home/garlic/Desktop/笔记/图片/acl-16.PNG)

   *步骤 2：创建高级 ACL，使 PC1 可以访问 SERVER1 的 TELNET 服务，但不能访问 FTP 服务；PC2 可以访问 SERVER1 的 FTP 服务，但不能访问 TELNET 服务，并在 R1 的 g0/1 接口的入方向配置包过滤*

   ![acl-17](/home/garlic/Desktop/笔记/图片/acl-17.PNG)

   *步骤 3：创建高级 ACL，使PC3 不能访问 SERVER1，并在 R2 的 g0/2 接口的入方向配置包过滤*

   ![acl-18](/home/garlic/Desktop/笔记/图片/acl-18.PNG)

5. **效果测试**

   *步骤 1：PC1 和 PC2 都无法 Ping 通 PC3*

   ![acl-19](/home/garlic/Desktop/笔记/图片/acl-19.PNG)

   *步骤 2：PC1 可以连接 SERVER1 的 TELNET，但不能连接 FTP*

   ![acl-20](/home/garlic/Desktop/笔记/图片/acl-20.PNG)

   实验出错

   ![acl-21](/home/garlic/Desktop/笔记/图片/acl-21.PNG)

   *步骤 3：PC2 可以连接 SERVER1 的 FTP，但不能连接 TELNET*

   ![acl-22](/home/garlic/Desktop/笔记/图片/acl-22.PNG)

   实验出错

   ![acl-23](/home/garlic/Desktop/笔记/图片/acl-23.PNG)

   *步骤 4：PC3 不能 Ping 通 SERVER1*

   ![acl-24](/home/garlic/Desktop/笔记/图片/acl-24.PNG)