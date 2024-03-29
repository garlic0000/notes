### 基本语法



- 基本数据类型

  不同编程语言的基本数据类型不同。基本数据类型是的申请内存空间变得方便、规范化。

- 变量

  不同编程语言的声明变量方式有很大不同。有的如 Java 、C++ 需要明确指定变量数据类型，这种叫强类型定义语言。有的语言（主要是脚本语言），如 Javascript、Shell 等，不需要明确指定数据类型，这种叫若类型定义语言。

  还需要注意的一点是变量的作用域范围和生命周期。不同语言变量的作用域范围和生命周期不一定一样，这个需要在代码中细细体会，有时会为此埋雷。

- 逻辑控制语句

  编程语言都会有逻辑控制语句，哪怕是汇编语言。

  掌握条件语句、循环语句、中断循环语句（break、continue）、选择语句。一般区别仅仅在于关键字、语法格式略有不同。

- 运算符

  掌握基本运算符，如算术运算符、关系运算符、逻辑运算符、赋值运算符等。

  有些语言还提供位运算符、特殊运算符，视情节掌握。

- 注释（没啥好说的）

- 函数

  编程语言基本都有函数。注意语法格式：是否支持出参；支持哪些数据作为入参，有些语言允许将函数作为参数传入另一个参数（即回调）；返回值；如何退出函数（如 Java、C++的 return，）。

### 数组、枚举、集合

枚举只有部分编程语言有，如 Java、C++、C#。

但是数组和集合（有些语言叫容器）一般编程语言都有，只是有的编程语言提供的集合比较丰富。使用方法基本类似。

### 常用类

比较常用的类（当然有些语言中不叫类，叫对象或者其他什么，这个不重要，领会精神）请了解其 API 用法，如：字符串、日期、数学计算等等。

### 语言特性

语言特性这个特字反映的就是各个编程语言自身的"独特个性"，这涉及的点比较多，简单列举一些。

**编程模式**

比较流行的编程模式大概有：

面向对象编程，主要是封装、继承、多态；函数式编程，主要是应用 Lambda；过程式编程，可以理解为实现需求功能的特定步骤。

每种编程模式都有一定的道理，我从不认为只有面向对象编程才是王道。

Java 是面向对象语言，从 Java8 开始也支持函数编程（引入 Lambda 表达式）；C++ 可以算是半面向对象，半面向过程式语言。

**语言自身特性**

每个语言自身都有一些重要特性需要了解。例如，学习 C、C++，你必须了解内存的申请和释放，了解指针、引用。而学习 Java，你需要了解 JVM，垃圾回收机制。学习 Javascript，你需要了解 DOM 操作等。

### 代码组织、模块加载、库管理

一个程序一般都有很多个源代码文件。这就会引入这些问题：如何将代码文件组织起来？如何根据业务需要，选择将部分模块启动时进行加载，部分模块使用懒加载（或者热加载）？

最基本的引用文件就不提了，如C、C++的#include，Java 的 import 等。

针对代码组织、模块加载、库管理这些问题，不同语言会有不同的解决方案。

如 Java 可以用 maven、gradle 管理项目依赖、组织代码结构；Javascript （包括 Nodejs、jquery、react 等等库）可以用 npm、yarn 管理依赖，用 webpack 等工具管理模块加载。

### 容错处理

程序总难免会有 bug。

所以为了代码健壮性也好，为了方便定位问题也好，代码中需要有容错处理。常见的手段有：

- 异常
- 断言
- 日志
- 调试
- 单元测试

### 输入输出和文件处理

这块知识比较繁杂。建议提纲挈领的学习一下，理解基本概念，比如输入输出流、管道等等。至于 API，用到的时候再查一下即可。

### 回调机制

每种语言实现回调的方式有所不同，如 .Net 的 delegate （大量被用于 WinForm 程序）；Javascript 中函数天然支持回调：Javascript 函数允许传入另一个函数作为入参，然后在方法中调用它。其它语言的回调方式不一一列举。

### 序列化和反序列化

首先需要了解的是，序列化和反序列化的作用是为了在不同平台之间传输对象。

其次，要知道序列化存在多种方式，不同编程语言可能有多种方案。根据应用的序列化方式，选择性了解即可。

### 进阶特性

以下学习内容属于进阶性内容。可以根据开发需要去学习、掌握。需要注意的是，学习这些特性的态度应该是不学则已，学则死磕。因为半懂半不懂，特别容易引入问题。

*对于半桶水的同学，我想说：放过自己，也放过别人，活着不好吗？*

**并发编程：**好处多多，十分重要，但是并发代码容易出错，且出错难以定位。要学习还是要花很大力气的，需要了解大量知识，如：进程、线程、同步、异步、读写锁等等。

**反射：**让你可以动态编程（慎用）。

**泛型：**集合（或者叫容器）的基石。精通泛型，能大大提高你的代码效率。

**元数据**：描述数据的数据。Java 中叫做注解。

### 库和框架

