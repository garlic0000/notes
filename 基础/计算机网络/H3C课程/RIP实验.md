## RIP实验

### 实验拓扑

![rip-1](/home/garlic/Desktop/笔记/图片/rip-1.PNG)

### 实验需求

1. 按照图示配置 IP 地址
2. 配置 RIP 实现全网路由互通
3. 要求全网路由器不能出现明细路由（直连网段除外），不影响网络正常访问
4. 业务网段不允许出现协议报文
5. R1 和 R2 之间需要开启接口身份验证来保证协议安全性，密钥为 `runtime`

------

### 实验解法

1. **配置 IP 地址**

     ![rip-2](/home/garlic/Desktop/笔记/图片/rip-2.PNG)

     ![rip-3](/home/garlic/Desktop/笔记/图片/rip-3.PNG)

     ![rip-4](/home/garlic/Desktop/笔记/图片/rip-4.PNG)

     ![rip-5](/home/garlic/Desktop/笔记/图片/rip-5.PNG)

     ![rip-6](/home/garlic/Desktop/笔记/图片/rip-6.PNG)

     ![rip-7](/home/garlic/Desktop/笔记/图片/rip-7.PNG)

     ![rip-8](/home/garlic/Desktop/笔记/图片/rip-8.PNG)

2. **配置 RIP 实现全网路由互通**

   *分析：实现全网互通，意味着每台路由器都要宣告本地的所有直连网段。RIP 只能做主类宣告，以 R1 为例，连接的两个业务网段属于同一个 B 类主类网段划分出的子网，所以只用宣告一次；而且为了不造成路由环路，需要开启 RIP v2 版本，以支持 VLSM；R3 同理*
      　　
   *步骤 1：在 R1，R2，R3 上分别配置 RIP v2，关闭自动聚合，并宣告所有直连网段*

   ![rip-9](/home/garlic/Desktop/笔记/图片/rip-9.PNG)

   ![rip-10](/home/garlic/Desktop/笔记/图片/rip-10.PNG)

   ![rip-11](/home/garlic/Desktop/笔记/图片/rip-11.PNG)

   *步骤 2:在路由器上查看路由表，发现已经学习到了全网明细路由*

   ![rip-12](/home/garlic/Desktop/笔记/图片/rip-12.PNG)

   ![rip-13](/home/garlic/Desktop/笔记/图片/rip-13.PNG)

   ![rip-14](/home/garlic/Desktop/笔记/图片/rip-14.PNG)

3. **要求全网路由器不能出现明细路由（直连网段除外），不影响网络正常访问**

   *分析：上一步中的 RIP 已经配置完成，但路由器学习到的都是各网段的明细路由。在网络结构庞大的拓扑中，明细路由太多会导致路由器查表效率降低，所以需要配置路由聚合来减少路由数量
      　RIP 的聚合方式分为自动聚合和手动聚合。自动聚合是聚合为主类网段，在本拓扑中会造成路由环路，所以只能使用手动聚合
      　R1 连接的 2 个业务网段的路由可以聚合为一条 `172.16.0.0/23`，R3连接的 2 个业务网段的路由可以聚合为一条 `172.16.2.0/23`，在各自的路由传递的出接口上配置手动聚合*
      　
   *步骤 1：在 R1 的 g0/0 接口配置手动路由聚合*

   ![rip-15](/home/garlic/Desktop/笔记/图片/rip-15.PNG)

   *步骤 2：在 R3 的 g0/0 接口配置手动路由聚合*

   ![rip-16](/home/garlic/Desktop/笔记/图片/rip-16.PNG)

   *步骤 3：在 R2 上查看路由表，发现学习到的是 R1 和 R3 发布的聚合路由*

   　　*注意：基于 RIP 的工作原理，旧的明细路由需要一定时间延迟才会从路由表中彻底删除*

   ![rip-17](/home/garlic/Desktop/笔记/图片/rip-17.PNG)

4. **业务网段不允许出现协议报文**

   *分析：基于 `network` 命令的两层含义，R1 和 R3 对直连的业务网段进行宣告后，会往该网段发送 RIP 的协议报文。这些协议报文是完全没有意义的，还会消耗网络带宽，所以需要配置静默接口*
      　　
   *步骤 1：把 R1 连接业务网段的 g0/1 和 g0/2 接口配置为静默接口*

   ![rip-18](/home/garlic/Desktop/笔记/图片/rip-18.PNG)

   *步骤 2：把 R3 连接业务网段的 g0/1 和 g0/2 接口配置为静默接口*

   ![rip-19](/home/garlic/Desktop/笔记/图片/rip-19.PNG)

5. **R1 和 R2 之间需要开启接口身份验证来保证协议安全性，密钥为 `runtime`**

   *步骤 1：在 R1 的 g0/0 接口配置接口验证，密钥 `runtime`*

   ![rip-20](/home/garlic/Desktop/笔记/图片/rip-20.PNG)

   *步骤 2：在 R2 的 g0/0 接口配置接口验证，密钥必须和 R1 一致*

   ![rip-21](/home/garlic/Desktop/笔记/图片/rip-21.PNG)

   　　*说明：通过重置 RIP 进程观察是否能够学习到路由来判断接口验证是否通过*