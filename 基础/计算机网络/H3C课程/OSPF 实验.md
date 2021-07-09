## OSPF 实验

### 实验拓扑

![ospf-1](/home/garlic/Desktop/笔记/图片/ospf-1.PNG)

### 实验需求

1. 按照图示配置 IP 地址
2. 按照图示分区域配置 OSPF ，实现全网互通
3. 为了路由结构稳定，要求路由器使用环回口作为 Router-id，ABR 的环回口宣告进骨干区域

------

### 实验解法

1. **配置 IP 地址**

     ![ospf-2](/home/garlic/Desktop/笔记/图片/ospf-2.PNG)

     ![ospf-3](/home/garlic/Desktop/笔记/图片/ospf-3.PNG)

     ![ospf-4](/home/garlic/Desktop/笔记/图片/ospf-4.PNG)

     ![ospf-5](/home/garlic/Desktop/笔记/图片/ospf-5.PNG)

     ![ospf-6](/home/garlic/Desktop/笔记/图片/ospf-6.PNG)

2. **按照图示分区域配置 OSPF ，实现全网互通**

   *分析：实现全网互通，意味着每台路由器都要宣告本地的所有直连网段，包括环回口所在的网段。要求 ABR 的环回口宣告进骨干区域，即区域 0，
      　　同时，每台路由器手动配置各自环回口的 IP 地址作为 Router-id*

   *步骤 1：在路由器上分别配置 OSPF，按区域宣告所有直连网段和环回口*

   ![ospf-7](/home/garlic/Desktop/笔记/图片/ospf-7.PNG)

   ![ospf-8](/home/garlic/Desktop/笔记/图片/ospf-8.PNG)

   ![ospf-9](/home/garlic/Desktop/笔记/图片/ospf-9.PNG)

   ![ospf-10](/home/garlic/Desktop/笔记/图片/ospf-10.PNG)

   ![ospf-11](/home/garlic/Desktop/笔记/图片/ospf-11.PNG)

3. **检查是否全网互通**

   *分析：检查 OSPF 是否全网互通，一个是检查邻居关系表，看邻居关系是否正常；另一个是检查路由表，看是否学习到全网路由
      　　这里只展示 R1 的检查结果*
      　　
   *步骤 1：检查 R1 的邻居关系表*

   ![ospf-12](/home/garlic/Desktop/笔记/图片/ospf-12.PNG)

   　　*说明：可以看到，R1 分别和 R2 和 R4 建立了邻接关系，状态为 FULL，邻居关系正常*
   　　
   *步骤 2：检查 R1 的路由表*

   ![ospf-13](/home/garlic/Desktop/笔记/图片/ospf-13.PNG)

   　　*说明：可以看到，R1 已经学习到了全网所有网段的路由信息*