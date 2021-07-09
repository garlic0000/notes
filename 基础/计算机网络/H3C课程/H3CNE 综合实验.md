## H3CNE 综合实验

### 实验拓扑

![h3c-1](/home/garlic/Desktop/笔记/图片/h3c-1.PNG)

### 实验需求

1. 按照图示配置 IP 地址
2. SW1 和 SW2 之间的直连链路配置链路聚合
3. 公司内部业务网段为 Vlan10 和 Vlan20；Vlan10 是市场部，Vlan20 是技术部，要求对 Vlan 进行命名以便识别；PC1 属于 Vlan10，PC2 属于 Vlan20，Vlan30 用于 SW1 和 SW2 建立 OSPF 邻居；Vlan111 为 SW1 和 R1 的互联 Vlan，Vlan222 为 SW2 和 R2 的互联 Vlan
4. 所有交换机相连的端口配置为 Trunk，允许相关流量通过
5. 交换机连接 PC 的端口配置为边缘端口
6. 在 SW1 上配置 DHCP 服务，为 Vlan10 和 Vlan20 的 PC 动态分配 IP 地址、网关和 DNS 地址；要求 Vlan10 的网关是 `192.168.1.252`，Vlan20 的网关是 `192.168.2.253`
7. 按图示分区域配置 OSPF 实现公司内部网络全网互通，ABR 的环回口宣告进骨干区域；业务网段不允许出现协议报文
8. R1 上配置默认路由指向互联网，并引入到 OSPF
9. R1 通过双线连接到互联网，配置 PPP-MP，并配置双向 chap 验证
10. 配置 EASY IP，只有业务网段 `192.168.1.0/24` 和 `192.168.2.0/24` 的数据流可以通过 R1 访问互联网
11. R1 开启 TELNET 远程管理，使用用户 `abc` 登录，密码 `abc`，只允许技术部远程管理 R1

### 实验解法

#### 1.配置IP

按照图示配置 IP 地址

R1

```
//创建MP-GROUP并进行配置
[R1]interface MP-group 1
[R1-MP-group1]ip address 202.100.1.2 30
[R1-MP-group1]interface s1/0
[R1-Serial1/0]ppp mp MP-group 1
[R1-Serial1/0]interface s2/0
[R1-Serial2/0]ppp mp MP-group 1

//在各个物理接口配置ip
[R1]interface g0/1
[R1-GigabitEthernet0/1]ip address 10.0.0.1 30
[R1-GigabitEthernet0/1]interface g0/0
[R1-GigabitEthernet0/0]ip address 10.0.0.5 30
[R1-GigabitEthernet0/0]interface g0/2
[R1-GigabitEthernet0/2]ip address 10.0.0.14 30

//配置环回地址
[R1]interface LoopBack 0
[R1-LoopBack0]ip address 10.1.1.1 32
```

![h3c-3](/home/garlic/Desktop/笔记/图片/h3c-3.PNG)

![h3c-34](/home/garlic/Desktop/笔记/图片/h3c-34.PNG)

INTERNET

```
//创建MP-GROUP并进行配置
[INTERNET]interface MP-group 1
[INTERNET-MP-group1]ip address 202.100.1.1 30
[INTERNET-MP-group1]interface s1/0
[INTERNET-Serial1/0]ppp mp MP-group 1
[INTERNET-Serial1/0]interface s2/0
[INTERNET-Serial2/0]ppp mp MP-group 1

//配置环回地址
[INTERNET]interface LoopBack 0
[INTERNET-LoopBack0]ip address 100.1.1.1 32
```

![h3c-4](/home/garlic/Desktop/笔记/图片/h3c-4.PNG)

R2

```
//在各个物理接口配置ip
[R2]interface g0/2
[R2-GigabitEthernet0/2]ip address 10.0.0.2 30
[R2-GigabitEthernet0/2]interface g0/0
[R2-GigabitEthernet0/0]ip address 10.0.0.9 30
[R2-GigabitEthernet0/0]interface g0/1
[R2-GigabitEthernet0/1]ip address 10.0.0.18 30


//配置环回地址
[R2]interface LoopBack 0
[R2-LoopBack0]ip address 10.1.1.2 32
```

![h3c-5](/home/garlic/Desktop/笔记/图片/h3c-5.PNG)

R3

```
//在各个物理接口配置ip
[R3]interface g0/0
[R3-GigabitEthernet0/0]ip address 10.0.0.13 30
[R3-GigabitEthernet0/0]interface g0/1
[R3-GigabitEthernet0/1]ip address 10.0.0.17 30
[R3-GigabitEthernet0/1]interface g0/2
[R3-GigabitEthernet0/2]ip address 192.168.3.254 24

//配置环回地址
[R3]interface LoopBack 0
[R3-LoopBack0]ip address 10.1.1.3 32
```

![h3c-6](/home/garlic/Desktop/笔记/图片/h3c-6.PNG)

PC1

![h3c-7](/home/garlic/Desktop/笔记/图片/h3c-7.PNG)

PC2

![h3c-8](/home/garlic/Desktop/笔记/图片/h3c-8.PNG)

PC3

![h3c-9](/home/garlic/Desktop/笔记/图片/h3c-9.PNG)

SW1

```
[SW1]vlan 10
[SW1-vlan10]vlan 20
[SW1-vlan20]vlan 30
[SW1-vlan30]vlan 111
[SW1-vlan111]

//开启 Vlanif 接口并配置ip
[SW1]interface Vlan-interface 10
[SW1-Vlan-interface10]ip address 192.168.1.252 24
[SW1-Vlan-interface10]interface Vlan-interface 20
[SW1-Vlan-interface20]ip address 192.168.2.252 24
[SW1-Vlan-interface20]interface Vlan-interface 30
[SW1-Vlan-interface30]ip address 10.1.2.1 30
[SW1-Vlan-interface30]interface Vlan-interface 111
[SW1-Vlan-interface111]ip address 10.0.0.6 30

//配置L0
[SW1]interface LoopBack 0
[SW1-LoopBack0]ip address 10.1.1.11 32
```

![h3c-10](/home/garlic/Desktop/笔记/图片/h3c-10.PNG)

SW2

```
[SW1]vlan 10
[SW1-vlan10]vlan 20
[SW1-vlan20]vlan 30
[SW1-vlan30]vlan 222
[SW1-vlan222]

//开启 Vlanif 接口并配置ip
[SW1]interface Vlan-interface 10
[SW1-Vlan-interface10]ip address 192.168.1.253 24
[SW1-Vlan-interface10]interface Vlan-interface 20
[SW1-Vlan-interface20]ip address 192.168.2.253 24
[SW1-Vlan-interface20]interface Vlan-interface 30
[SW1-Vlan-interface30]ip address 10.1.2.2 30
[SW1-Vlan-interface30]interface Vlan-interface 222
[SW1-Vlan-interface222]ip address 10.0.0.10 30

//配置L0
[SW2]interface LoopBack 0
[SW2-LoopBack0]ip address 10.1.1.12 32
```

![h3c-11](/home/garlic/Desktop/笔记/图片/h3c-11.PNG)

#### 2.配置链路聚合

在SW1 和 SW2 之间的直连链路配置链路聚合

SW1

```
//在SW1上创建Bridge-Aggregation 1号聚合接口
//并把两个接口加入到聚合接口
[SW1]interface Bridge-Aggregation 1
[SW1-Bridge-Aggregation1]interface g1/0/1
[SW1-GigabitEthernet1/0/1]port link-aggregation group 1
[SW1-GigabitEthernet1/0/1]interface g1/0/2
[SW1-GigabitEthernet1/0/2]port link-aggregation group 1

//查看链路聚合状态
[SW1]display link-aggregation verbose
```

![h3c-12](/home/garlic/Desktop/笔记/图片/h3c-12.PNG)

SW2

```
//在SW2上创建Bridge-Aggregation 1号聚合接口
//并把两个接口加入到聚合接口
[SW2]interface Bridge-Aggregation 1
[SW2-Bridge-Aggregation1]interface g1/0/1
[SW2-GigabitEthernet1/0/1]port link-aggregation group 1
[SW2-GigabitEthernet1/0/1]interface g1/0/2
[SW2-GigabitEthernet1/0/2]port link-aggregation group 1

//查看链路聚合状态
[SW1]display link-aggregation verbose
```

![h3c-13](/home/garlic/Desktop/笔记/图片/h3c-13.PNG)

#### 3.vlan和trunk配置

*公司内部业务网段为 Vlan10 和 Vlan20；Vlan10 是市场部，Vlan20 是技术部，要求对 Vlan 进行命名以便识别；PC1 属于 Vlan10，PC2 属于 Vlan20，Vlan30 用于 SW1 和 SW2 建立 OSPF 邻居；Vlan111 为 SW1 和 R1 的互联 Vlan，Vlan222 为 SW2 和 R2 的互联 Vlan*

*所有交换机相连的端口配置为 Trunk，允许相关流量通过*

SW1

```
//在SW1上分别创建vlan10、vlan20、vlan30和vlan111并命名
//同时指定物理接口
[SW1]vlan 10
[SW1-vlan10]name shichangbu
[SW1-vlan10]vlan 20
[SW1-vlan20]name jishubu
[SW1-vlan20]vlan 30
[SW1-vlan30]name to_SW2
[SW1-vlan30]vlan 111
[SW1-vlan111]name to_R1
[SW1-vlan111]port g1/0/4


//配置trunk
[SW1]interface Bridge-Aggregation 1
[SW1-Bridge-Aggregation1]port link-type trunk
[SW1-Bridge-Aggregation1]port trunk permit vlan 10 20 30

[SW1]interface g1/0/3
[SW1-GigabitEthernet1/0/3]port link-type trunk
[SW1-GigabitEthernet1/0/3]port trunk permit vlan 10 20
```

![h3c-15](/home/garlic/Desktop/笔记/图片/h3c-15.PNG)

SW2

```
//在SW2上分别创建vlan10、vlan20、vlan30和vlan222并命名
//同时指定物理接口
[SW2]vlan 10
[SW2-vlan10]name shichangbu
[SW2-vlan10]vlan 20
[SW2-vlan20]name jishubu
[SW2-vlan20]vlan 30
[SW2-vlan30]name to_SW1
[SW2-vlan30]vlan 222
[SW2-vlan222]name to_R2
[SW2-vlan222]port g1/0/4


//配置trunk
[SW2]interface Bridge-Aggregation 1
[SW2-Bridge-Aggregation1]port link-type trunk
[SW2-Bridge-Aggregation1]port trunk permit vlan 10 20 30

[SW2]interface g1/0/3
[SW2-GigabitEthernet1/0/3]port link-type trunk
[SW2-GigabitEthernet1/0/3]port trunk permit vlan 10 20

```

![h3c-16](/home/garlic/Desktop/笔记/图片/h3c-16.PNG)

SW3

```
//在SW3上分别创建vlan10、vlan20并命名
//同时指定物理接口
[SW3]vlan 10
[SW3-vlan10]name shichangbu
[SW3-vlan10]port g1/0/3
[SW3-vlan10]vlan 20
[SW3-vlan20]name jishubu
[SW3-vlan20]port g1/0/4


//配置trunk
[SW3]interface g1/0/1
[SW3-GigabitEthernet1/0/1]port link-type trunk
[SW3-GigabitEthernet1/0/1]port trunk permit vlan 10 20
[SW3-GigabitEthernet1/0/1]interface g1/0/2
[SW3-GigabitEthernet1/0/2]port link-type trunk
[SW3-GigabitEthernet1/0/2]port trunk permit vlan 10 20
```

![h3c-17](/home/garlic/Desktop/笔记/图片/h3c-17.PNG)

#### 4.配置边缘端口

交换机连接 PC 的端口配置为边缘端口

```
[SW3]interface g1/0/3
[SW3-GigabitEthernet1/0/3]stp edged-port 
[SW3-GigabitEthernet1/0/3]interface g1/0/4
[SW3-GigabitEthernet1/0/4]stp edged-port 
```

![h3c-18](/home/garlic/Desktop/笔记/图片/h3c-18.PNG)

####  5.配置dhcp服务

*在 SW1 上配置 DHCP 服务，为 Vlan10 和 Vlan20 的 PC 动态分配 IP 地址、网关和 DNS 地址；要求 Vlan10 的网关是 `192.168.1.252`，Vlan20 的网关是 `192.168.2.253`*

```
[SW1]dhcp enable
[SW1]dhcp server ip-pool vlan10
[SW1-dhcp-pool-1]network 192.168.1.0 mask 255.255.255.0
[SW1-dhcp-pool-1]gateway-list 192.168.1.252
[SW1-dhcp-pool-1]dns-list 114.114.114.114

[SW1]dhcp server ip-pool vlan20
[SW1-dhcp-pool-2]network 192.168.2.0 mask 255.255.255.0
[SW1-dhcp-pool-2]gateway-list 192.168.2.253
[SW2-dhcp-pool-1]dns-list 114.114.114.114
```

![h3c-19](/home/garlic/Desktop/笔记/图片/h3c-19.PNG)

![h3c-33](/home/garlic/Desktop/笔记/图片/h3c-33.PNG)

#### 6.ospf配置

*按图示分区域配置 OSPF 实现公司内部网络全网互通，ABR 的环回口宣告进骨干区域；业务网段不允许出现协议报文*

SW1

```
//查看路由信息
[SW1]display ip interface brief

//进行配置
[SW1]ospf router-id 10.1.1.11
[SW1-ospf-1]silent-interface Vlan-interface 10
[SW1-ospf-1]silent-interface Vlan-interface 20
[SW1-ospf-1]area 1
[SW1-ospf-1-area-0.0.0.1]network 192.168.1.252 0.0.0.0
[SW1-ospf-1-area-0.0.0.1]network 192.168.2.252 0.0.0.0
[SW1-ospf-1-area-0.0.0.1]network 10.1.2.1 0.0.0.0
[SW1-ospf-1-area-0.0.0.1]network 10.1.1.11 0.0.0.0
[SW1-ospf-1-area-0.0.0.1]network 10.0.0.6 0.0.0.0
[SW1-ospf-1-area-0.0.0.1]quit
[SW1-ospf-1]quit
```

![h3c-20](/home/garlic/Desktop/笔记/图片/h3c-20.PNG)

SW2

```
[SW2]ospf router-id 10.1.1.12
[SW2-ospf-1]silent-interface Vlan-interface 10
[SW2-ospf-1]silent-interface Vlan-interface 20
[SW2-ospf-1]area 1
[SW2-ospf-1-area-0.0.0.1]network 192.168.1.253 0.0.0.0
[SW2-ospf-1-area-0.0.0.1]network 192.168.2.253 0.0.0.0
[SW2-ospf-1-area-0.0.0.1]network 10.1.2.2 0.0.0.0
[SW2-ospf-1-area-0.0.0.1]network 10.0.0.10 0.0.0.0
[SW2-ospf-1-area-0.0.0.1]network 10.1.1.12 0.0.0.0
[SW2-ospf-1-area-0.0.0.1]quit
```

![h3c-21](/home/garlic/Desktop/笔记/图片/h3c-21.PNG)

R1

```
[R1]ospf router-id 10.1.1.1
[R1-ospf-1]area 0
[R1-ospf-1-area-0.0.0.0]network 10.0.0.1 0.0.0.0
[R1-ospf-1-area-0.0.0.0]network 10.0.0.14 0.0.0.0
[R1-ospf-1-area-0.0.0.0]network 10.1.1.1 0.0.0.0
[R1-ospf-1-area-0.0.0.0]area 1
[R1-ospf-1-area-0.0.0.1]network 10.0.0.5 0.0.0.0
[R1-ospf-1-area-0.0.0.1]quit
```

![h3c-22](/home/garlic/Desktop/笔记/图片/h3c-22.PNG)

R2

```
[R2]ospf router-id 10.1.1.2
[R2-ospf-1]area 0
[R2-ospf-1-area-0.0.0.0]network 10.0.0.18 0.0.0.0
[R2-ospf-1-area-0.0.0.0]network 10.0.0.2 0.0.0.0
[R2-ospf-1-area-0.0.0.0]network 10.1.1.2 0.0.0.0
[R2-ospf-1-area-0.0.0.0]area 1
[R2-ospf-1-area-0.0.0.1]network 10.0.0.9 0.0.0.0
[R2-ospf-1]quit
```

![h3c-23](/home/garlic/Desktop/笔记/图片/h3c-23.PNG)

R3

```
[R3]ospf router-id 10.1.1.3
[R3-ospf-1]area 0
[R3-ospf-1-area-0.0.0.0]network 10.0.0.13 0.0.0.0
[R3-ospf-1-area-0.0.0.0]network 10.0.0.17 0.0.0.0
[R3-ospf-1-area-0.0.0.0]network 192.168.3.254 0.0.0.0
[R3-ospf-1-area-0.0.0.0]network 10.1.1.3 0.0.0.0
[R3-ospf-1-area-0.0.0.0]quit
[R3-ospf-1]quit
```

![h3c-24](/home/garlic/Desktop/笔记/图片/h3c-24.PNG)

#### 7.默认路由

*R1 上配置默认路由指向互联网，并引入到 OSPF*

```
//配置默认路由
[R1]ip route-static 0.0.0.0 0 202.100.1.1

//引入到 OSPF
[R1]ospf
[R1-ospf-1]default-route-advertise
```

![h3c-25](/home/garlic/Desktop/笔记/图片/h3c-25.PNG)

#### 8.配置PPP-MP

*R1 通过双线连接到互联网，配置 PPP-MP，并配置双向 chap 验证*

```
//PPP-MP在配置ip地址时已经配过

//chap验证
[R1]local-user xiaoming class network 
[R1-luser-network-xiaoming]password simple 666666
[R1-luser-network-xiaoming]service-type ppp

[INTERNET]local-user xiaoming class network 
[INTERNET-luser-network-xiaoming]password simple 666666
[INTERNET-luser-network-xiaoming]service-type ppp

[R1]interface s1/0
[R1-Serial1/0]ppp authentication-mode chap
[R1-Serial1/0]ppp chap user xiaoming
[R1-Serial1/0]interface s2/0
[R1-Serial2/0]ppp authentication-mode chap
[R1-Serial2/0]ppp chap user xiaoming

[INTERNET]interface s1/0
[INTERNET-Serial1/0]ppp authentication-mode chap
[INTERNET-Serial1/0]ppp chap user xiaoming
[INTERNET-Serial1/0]interface s2/0
[INTERNET-Serial2/0]ppp authentication-mode chap
[INTERNET-Serial2/0]ppp chap user xiaoming

//shutdown MP接口，再undo shutdown，观察MP接口是否up
```

![h3c-26](/home/garlic/Desktop/笔记/图片/h3c-26.PNG)

![h3c-27](/home/garlic/Desktop/笔记/图片/h3c-27.PNG)

![h3c-28](/home/garlic/Desktop/笔记/图片/h3c-28.PNG)

![h3c-29](/home/garlic/Desktop/笔记/图片/h3c-29.PNG)

#### 9.配置EASY IP

*配置 EASY IP，只有业务网段 `192.168.1.0/24` 和 `192.168.2.0/24` 的数据流可以通过 R1 访问互联网*

```
//配置easy ip
[R1]acl basic 2000
[R1-acl-ipv4-basic-2000]rule permit source 192.168.1.0 0.0.0.255
[R1-acl-ipv4-basic-2000]rule permit source 192.168.2.0 0.0.0.255
[R1-acl-ipv4-basic-2000]interface MP-group 1
[R1-MP-group1]nat outbound 2000

//PC1,PC2访问互联网
<h3c>ping 100.1.1.1
```

![h3c-32](/home/garlic/Desktop/笔记/图片/h3c-32.PNG)

![h3c-30](/home/garlic/Desktop/笔记/图片/h3c-30.PNG)

#### 10.配置TELNET

*R1 开启 TELNET 远程管理，使用用户 `abc` 登录，密码 `abc`，只允许技术部远程管理 R1*

```
//开启并配置telnet服务
[R1]telnet server enable
[R1]local-user abc class manage 
[R1-luser-manage-abc]password simple 123
[R1-luser-manage-abc]service-type telnet 
[R1-luser-manage-abc]authorization-attribute user-role level-15

[R1]user-interface vty 0 4
[R1-line-vty0-4]authentication-mode scheme 
[R1-line-vty0-4]user-role level-15

//只允许技术部(vlan20)远程管理R1
[R1]access-list basic 2001
[R1-acl-ipv4-basic-2001]rule permit source 192.168.2.0 0.0.0.255
[R1-acl-ipv4-basic-2001]quit
[R1]telnet server acl 2001
```

![h3c-31](/home/garlic/Desktop/笔记/图片/h3c-31.PNG)