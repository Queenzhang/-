### 《WebKit技术内幕》

#### 浏览器和浏览器内核

+ 浏览器：互联网最重要的终端接口之一
  + 特性
    + 网络
    + 资源管理
    + 网页浏览
    + 多页面管理
    + 插件和扩展
    + 账户和同步
    + 安全机制
    + 开发者工具
  + HTML：超文本标记语言，用于网页的创建和其他信息在浏览器中的显示
  + HTML5标准的十大类别
    + 离线（offline）
    + 存储（storage）
    + 连接（connectivity）
    + 文件访问（file access）
    + 语义（semantics）
    + 音频和视频（audio/video）
    + 3D和图形（3D/graphics）
    + 展示（presentation）
    + 性能（performance）
    + 其他（nuts and bolts）
  + https://html5test.com/
  + 每个浏览器都有自己的一套标准，兼容性成为HTML网页的一项重大挑战
  + 用户代理：作用是表明浏览器的身份，因而互联网的内容供应商能够知道发送请求的浏览器身份，浏览器能够支持什么样的功能
  + 用户代理信息是浏览器向网站服务器发送HTTP请求消息头的时候加入的
+ 浏览器内核
  + 内核：主要作用是将页面转变成可视化（加上可听化）的图像结果。通常也被称为渲染引擎
  + ![截屏2021-11-04 下午9.01.45](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-04 下午9.01.45.png)
  + 主流渲染引擎
    + Trident（IE）
    + Gecko（火狐）
    + Webkit（Chrome）
  + ![截屏2021-11-04 下午9.06.57](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-04 下午9.06.57.png)
    + HTML解释器：主要作用是将HTML文本解释成DOM（文档对象模型）树
    + CSS解释器：作用是为DOM中的各个元素对象计算出样式信息，从而为计算最后网页的布局提供基础设施
    + 布局：在DOM创建之后，Webkit需要将其中的元素对象用样式信息结合起来，计算它们的大小位置等布局信息，形成一个能够表示这所有信息的内部表示模型
    + JavaScript引擎：使用JavaScript代码可以修改网页的内容，也能修改CSS的信息。JavaScript引擎能够解释JavaScript代码并通过DOM接口和CSSDOM接口来修改网页内容和样式信息，从而改变渲染的结果
    + 绘图：使用图形库将布局计算后的各个网页的节点绘制成图像结果
  + ![截屏2021-11-04 下午9.16.18](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-04 下午9.16.18.png)
+ WebKit内核
  + ![截屏2021-11-04 下午9.24.34](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-04 下午9.24.34.png)
  + ![截屏2021-11-04 下午9.27.17](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-04 下午9.27.17.png)

#### HTML网页和结构

#### WebKit架构和模块

#### 资源加载和网络栈

#### HTML解释器和DOM模型

#### CSS解释器和样式布局

#### 渲染基础

#### 硬件加速机制

#### JavaScript引擎

#### 插件和JavaScript扩展

#### 多媒体

#### 安全机制

#### 移动WebKit

#### 调试机制

#### Web前端的未来

#### 总结

使用HTML技术来编写网页或Web应用，了解其背后的工作原理是写出高效代码的有效捷径。