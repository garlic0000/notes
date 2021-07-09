## Vlan和Trunk实验

### 实验拓扑

![捕获0](/home/garlic/Desktop/笔记/图片/捕获0.PNG)



### 实验需求

1. 按图示为PC配置IP地址
2. SW1和SW2上分别创建vlan10和vlan20，要求PC3和PC5属于vlan10，PC4和PC6属于vlan20
3. SW1和SW2相连的接口配置为trunk类型，允许vlan10和vlan20通过
4. 测试效果，同一vlan的PC可以互通，不同vlan的PC无法互通

------

### 实验解法

1. **PC配置IP地址命令**

   ![捕获1](/home/garlic/Desktop/笔记/图片/捕获1.PNG)

   ![捕获2](/home/garlic/Desktop/笔记/图片/捕获2.PNG)

   ![捕获3](/home/garlic/Desktop/笔记/图片/捕获3.PNG)

   ![捕获4](/home/garlic/Desktop/笔记/图片/捕获4.PNG)

2. **SW1和SW2上分别创建vlan10和vlan20**

   *步骤1：在SW1上创建vlan10和vlan20*

   ```
   [SW1]vlan 10
   [SW1-vlan10]vlan 20
   [SW1-vlan20]
   ```

   ![捕获5](/home/garlic/Desktop/笔记/图片/捕获5.PNG)

   步骤2：在SW2上创建vlan10和vlan20*

   ```
   [SW2]vlan 10
   [SW2-vlan10]vlan 20
   [SW2-vlan20]
   
   ```

   ![捕获6](/home/garlic/Desktop/笔记/图片/捕获6.PNG)

3. **SW1和SW2都把g1/0/1接口加入vlan10，g1/0/2接口加入vlan20**

   *步骤1：在SW1上把g1/0/1接口加入到vlan10，把g1/0/2接口加入到vlan20*

   ```
   [SW1]vlan 10
   [SW1-vlan10]port g1/0/1
   [SW1-vlan10]vlan 20
   [SW1-vlan20]port g1/0/2
   
   ```

   ![捕获7](/home/garlic/Desktop/笔记/图片/捕获7.PNG)

   *步骤2：在SW2上把g1/0/1接口加入到vlan10，把g1/0/2接口加入到vlan20*

   ```
   [SW2]vlan 10
   [SW2-vlan10]port g1/0/1
   [SW2-vlan10]vlan 20
   [SW2-vlan20]port g1/0/2
   ```

   ![捕获8](/home/garlic/Desktop/笔记/图片/捕获8.PNG)

4. **SW1和SW2的g1/0/3接口都配置为trunk，允许vlan10和vlan20通过**

   *步骤1：在SW1上把g1/0/3接口配置为Trunk类型，并允许vlan10和vlan20通过*

   ```
   [SW1]interface g1/0/3
   [SW1-GigabitEthernet1/0/3]port link-type trunk 
   [SW1-GigabitEthernet1/0/3]port trunk permit vlan 10 20
   ```

   ![捕获9](/home/garlic/Desktop/笔记/图片/捕获9.PNG)

   *步骤2：在SW2上把g1/0/3接口配置为Trunk类型，并允许vlan10和vlan20通过*

   ```
   [SW2]interface g1/0/3
   [SW2-GigabitEthernet1/0/3]port link-type trunk 
   [SW2-GigabitEthernet1/0/3]port trunk permit vlan 10 20
   ```

   ![捕获10](/home/garlic/Desktop/笔记/图片/捕获10.PNG)

5. **测试结果，如下所示，PC3可以PING通PC5，但无法PING通PC4和PC6**

   *步骤1：在PC3上PingPC4，发现不能Ping通*

   ```
   <H3C>ping 192.168.1.2
   Ping 192.168.1.2 (192.168.1.2): 56 data bytes, press CTRL_C to break
   Request time out
   Request time out
   Request time out
   Request time out
   Request time out
   ```

   ![捕获11](/home/garlic/Desktop/笔记/图片/捕获11.PNG)

   *步骤2：在PC3上PingPC5，发现可以Ping通*

   ![捕获12](/home/garlic/Desktop/笔记/图片/捕获12.PNG)
   
   ```
   <H3C>ping 192.168.1.3
   Ping 笔记/图片7.0.0.1 (笔记/图片7.0.0.1): 56 data bytes, press CTRL_C to break
   56 bytes from 笔记/图片7.0.0.1: icmp_seq=0 ttl=255 time=0.000 ms
   56 bytes from 笔记/图片7.0.0.1: icmp_seq=1 ttl=255 time=0.000 ms
   56 bytes from 笔记/图片7.0.0.1: icmp_seq=2 ttl=255 time=0.000 ms
   56 bytes from 笔记/图片7.0.0.1: icmp_seq=3 ttl=255 time=0.000 ms
56 bytes from 笔记/图片7.0.0.1: icmp_seq=4 ttl=255 time=0.000 ms
   ```

   *步骤3：在PC3上PingPC6，发现不能Ping通*
   
   ```
   <H3C>ping 192.168.1.4
   Ping 192.168.1.4 (192.168.1.4): 56 data bytes, press CTRL_C to break
   Request time out
   Request time out
   Request time out
   Request time out
   Request time out

   ```
   
   ![捕获13](/home/garlic/Desktop/笔记/图片/捕获13.PNG)

