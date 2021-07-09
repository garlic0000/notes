## NAT 实验

### 实验拓扑

![nat-1](/home/garlic/Desktop/笔记/图片/nat-1.PNG)

## 实验需求

1. 按照图示配置 IP 地址
2. 私网 A 通过 R1 接入到互联网，私网 B 通过 R3 接入到互联网
3. 私网 A 内部存在 Vlan10 和 Vlan20，通过 R1 上单臂路由访问外部网络
4. 私网 A 通过 NAPT 使 Vlan10 和 Vlan20 都能够使用 R1 的公网地址访问互联网
5. 私网 B 通过在 R3 上配置 EASY IP 访问互联网
6. 私网 A 配置 NAT SERVER 把 FTPA 的 FTP 服务发布到公网，使 PCB 可以访问

------

### 实验解法

1. **配置 IP 地址**

     SWA

     ![nat-2](/home/garlic/Desktop/笔记/图片/nat-2.PNG)

     R1
     
     ![nat-3](/home/garlic/Desktop/笔记/图片/nat-3.PNG)
     
     R2
     
![nat-4](/home/garlic/Desktop/笔记/图片/nat-4.PNG)
     
R3   ![nat-5](/home/garlic/Desktop/笔记/图片/nat-5.PNG)
     
2. **R1 和 R3 上配置默认路由指向公网**

     ![nat-6](/home/garlic/Desktop/笔记/图片/nat-6.PNG)

     

3. **私网 A 内部单臂路由配置**

     在 R1 上创建子接口 ，开启 dot1q 识别，绑定到 Vlan，并配置 IP 地址

     ![nat-7](/home/garlic/Desktop/笔记/图片/nat-7.PNG)

     

4. **私网 A 通过 NAPT 使 Vlan10 和 Vlan20 都能够使用 R1 的公网地址访问互联网**

   R1 上创建基本 ACL，允许 `192.168.1.0/24` 和 `192.168.2.0/24` 网段

   ![nat-8](/home/garlic/Desktop/笔记/图片/nat-8.PNG)

   R1 上创建 NAT 地址池，设置公网地址

   ![nat-9](/home/garlic/Desktop/笔记/图片/nat-9.PNG)

   在 R1 的公网接口上配置 NAPT

   ![nat-10](/home/garlic/Desktop/笔记/图片/nat-10.PNG)

   在 PCA 上 Ping R3 的公网地址，测试是否可以访问互联网

   ```
   <PCA>ping 100.2.2.3
   Ping 100.2.2.3 (192.168.2.10): 56 data bytes, press CTRL_C to break
   56 bytes from 100.2.2.3: icmp_seq=0 ttl=254 time=22.000 ms
   56 bytes from 100.2.2.3: icmp_seq=1 ttl=254 time=51.000 ms
   56 bytes from 100.2.2.3: icmp_seq=2 ttl=254 time=21.000 ms
   56 bytes from 100.2.2.3: icmp_seq=3 ttl=254 time=43.000 ms
   56 bytes from 100.2.2.3: icmp_seq=4 ttl=254 time=34.000 ms
   ```

5. **私网 B 通过在 R3 上配置 EASY IP 访问互联网**

   R3 上创建基本 ACL，允许 `192.168.1.0/24` 网段

   ![nat-11](/home/garlic/Desktop/笔记/图片/nat-11.PNG)

   在 R3 的公网接口上配置 EASY IP

   ![nat-12](/home/garlic/Desktop/笔记/图片/nat-12.PNG)

   在 PCB 上 Ping R1 的公网地址，测试是否可以访问互联网

   ```
   <PCB>ping 100.1.1.1
   Ping 100.1.1.1 (192.168.1.10): 56 data bytes, press CTRL_C to break
   56 bytes from 100.1.1.1: icmp_seq=0 ttl=254 time=32.000 ms
   56 bytes from 100.1.1.1: icmp_seq=1 ttl=254 time=29.000 ms
   56 bytes from 100.1.1.1: icmp_seq=2 ttl=254 time=41.000 ms
   56 bytes from 100.1.1.1: icmp_seq=3 ttl=254 time=33.000 ms
   56 bytes from 100.1.1.1: icmp_seq=4 ttl=254 time=34.000 ms
   ```

6. **私网 A 配置 NAT SERVER 把 FTPA 的 FTP 服务发布到公网，使 PCB 可以访问**

   在R2上开启FTP服务，创建用户`xiaoming`，密码`666666`

   ![nat-13](/home/garlic/Desktop/笔记/图片/nat-13.PNG)


    在 R1 的公网接口上配置 NAT SERVER，映射端口 20 和 21

   ![nat-14](/home/garlic/Desktop/笔记/图片/nat-14.PNG)

     在 PCB 上测试是否能够通过 R1 的公网地址访问 FTPA 的 FTP 服务

   ```
   <PCB>ftp 100.1.1.1
   Press CTRL+C to abort.
   Connected to 100.1.1.1 (100.1.1.1).
   220 FTP service ready.
   User (100.1.1.1:(none)): 
   ```

   