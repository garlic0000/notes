## PPP 实验

### 实验拓扑

![ppp-1](/home/garlic/Desktop/笔记/图片/ppp-1.PNG)

### 实验需求

1. R1 和 R2 使用 PPP 链路直连，R2 和 R3 把 2 条 PPP 链路捆绑为 PPP MP 直连
2. 按照图示配置 IP 地址
3. R2 对 R1 的 PPP 进行单向 chap 验证
4. R2 和 R3 的 PPP 进行双向 chap 验证

### 实验解法

1. **R2 和 R3 上配置 PPP MP**

   ![ppp-2](/home/garlic/Desktop/笔记/图片/ppp-2.PNG)

2. **按照图示配置 IP 地址**
   　　
   R1 和 R2 的直连链路 IP 地址配置
   
   ![ppp-3](/home/garlic/Desktop/笔记/图片/ppp-3.PNG)

   在 R2 和 R3 的 MP-GROUP 口上配置 IP 地址

   ![ppp-4](/home/garlic/Desktop/笔记/图片/ppp-4.PNG)
   
   
   
3. **R2 对 R1 的 PPP 进行单向 chap 验证**
      　　
   在 R2 上创建用于验证 R1 的用户

   ![ppp-5](/home/garlic/Desktop/笔记/图片/ppp-5.PNG)

   在 R2 连接 R1 的接口上配置需要进行 PPP 验证，验证方式为 chap

   ![ppp-6](/home/garlic/Desktop/笔记/图片/ppp-6.PNG)

   在 R1 连接 R2 的接口上配置用于验证的用户名和密码

   ![ppp-7](/home/garlic/Desktop/笔记/图片/ppp-7.PNG)

   关闭在开启 R1 和 R2 的 PPP 链路，检查验证是否能够通过

   ![ppp-8](/home/garlic/Desktop/笔记/图片/ppp-8.PNG)

4. **R2 和 R3 的 PPP 进行双向 chap 验证**
   在 R2 和 R3上创建用户验证 R3 的用户

   ![ppp-9](/home/garlic/Desktop/笔记/图片/ppp-9.PNG)

   ![ppp-10](/home/garlic/Desktop/笔记/图片/ppp-10.PNG)

   在 R2 和 R3 相连的接口上配置需要进行 PPP 验证，验证方式为 chap，并配置对端验证本端的用户名

   ![ppp-11](/home/garlic/Desktop/笔记/图片/ppp-11.PNG)

   ![ppp-12](/home/garlic/Desktop/笔记/图片/ppp-12.PNG)

   关闭在开启 R2 和 R3 的 PPP 链路，检查验证是否能够通过

   ![ppp-13](/home/garlic/Desktop/笔记/图片/ppp-13.PNG)

   ![ppp-14](/home/garlic/Desktop/笔记/图片/ppp-14.PNG)