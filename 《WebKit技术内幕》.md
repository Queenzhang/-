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

+ HTML网页的结构特征：
  + 树状结构
    + html是网页的根元素
    + 根元素下面包含很多节点
  + 层次结构
    + 网页中的元素可能分布在不同的层次中
    + ![截屏2021-11-05 下午9.06.24](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-05 下午9.06.24.png)
    + 需要复杂变换和处理的元素，需要新层
  + 框结构
    + 网页中嵌入新的框结构
    + iframe、frame、frameset
+ 网页构成
  + HTML文本
  + JavaScript代码
  + CSS代码
  + 各种资源文件
+ URL标记网络上的每个资源（URI的一直实现）
+ 加载：从“URL”到构建DOM树
+ 渲染：从DOM树到生成可视化图像
  + 网页通常比屏幕可视面积大
  + 当前可视区域称为视图（viewport)
+ ![截屏2021-11-05 下午9.34.22](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-05 下午9.34.22.png)
  + 过程：
    1. 当用户输入网页URL的时候，WebKit调用其资源加载器加载该URL对应的网页
    2. 加载器依赖网络模块建立连接，发送请求并接收答复
    3. WebKit接收到各种网页或者资源的数据，其中某些资源可能是同步或异步获取的
    4. 网页被交给HTML解释器转变成一系列的词语
    5. 解释器根据词语构建节点，形成DOM树
    6. 如果节点是JavaScript代码的话，调用JavaScript引擎解释并执行
    7. JavaScript代码可能会修改DOM树的结构
    8. 如果节点需要依赖其他资源，例如图片、CSS、视频等，调用资源加载器来加载它们，但是它们是异步的，不会阻碍当前DOM树的继续创建；如果是JavaScript资源URL（没有标记异步方式），则需要停止当前DOM树的创建，直到JavaScript的资源加载并被JavaScript引擎执行后才继续DOM树的创建
  + DOM树构建完之后，DOMContent事件触发
  + DOM树建完并且网页所依赖的资源都加载完之后，onload事件触发
+ ![截屏2021-11-05 下午9.38.37](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-05 下午9.38.37.png)
  + 过程：
    1. CSS文件被CSS解释器解释称内部表示结构
    2. CSS解释器工作完之后，在DOM树上附加解释后的样式信息，这就是RenderObject树
    3. RenderObject节点在创建的同时，WebKit会根据网页的层次结构创建RenderLayer树，同时构建一个虚拟的绘图上下文。
+ ![截屏2021-11-05 下午9.39.07](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-05 下午9.39.07.png)
  + 过程：
    1. 绘图上下文是一个与平台无关的抽象类，它将每个绘图操作桥接到不同的具体实现类，也就是绘图具体实现类
    2. 绘图实现类也可能有简单的实现，也可能有复杂的实现。
    3. 绘图实现类将2D图形库或者3D图形库绘制的结果保存下来，交给浏览器来同浏览器界面一起显示
+ 

#### WebKit架构和模块

+ ![截屏2021-11-06 下午11.02.54](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-06 下午11.02.54.png)
  + WebCore：加载和渲染网页的基础部分，目前被各个浏览器所使用的WebKit共享部分
  + JavaScriptCore引擎：WebKit默认的JavaScript引擎
  + WebKit Ports：WebKit中非共享部分
+ WebKit项目重要的目录：LayoutTests、PerformanceTests、Source、Tools
+ ![截屏2021-11-08 下午7.43.52](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-08 下午7.43.52.png)
  + Content模块和Content API将下面的渲染机制、安全机制和插件机制等隐藏起来，提供一个接口层
+ 多进程模型
  + 避免因单个页面的不响应或者崩溃而影响整个浏览器的稳定性，特别是对用户界面的影响
  + 当第三方插件崩溃时不会影响页面或者浏览器的稳定性
  + 方便了安全模型的实施，即沙箱模型是基于多进程架构的
+ ![截屏2021-11-08 下午7.52.13](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-08 下午7.52.13.png)
  + Browser进程：浏览器的主进程，负责浏览器界面的显示、各个页面的管理，是所有其他类型进程的祖先，负责它们的创建和销毁等工作，它有且仅有一个
  + Renderer进程：网页的渲染进程
  + NPAPI插件进程：该进程是为NPAPI类型的插件而创建的。其创建的基本原则是每种类型的插件只会被创建一次，而且仅当使用时才被创建
  + GPU进程：最多只有一个，当且仅当GPU硬件加速打开的时候才会被创建，主要用于对3D图形加速调用的实现
  + Pepper插件进程：同NPAPI插件进程，是为Pepper插件而创建的进程
  + 其他类型的进程
+ 进程模型的特征
  + Browser进程和页面的渲染是分开的，这保证了页面的渲染导致的崩溃不会导致浏览器主界面的崩溃
  + 每个页面是独立的进程，这保证了页面之间互相不影响
  + 插件进程是独立的，插件本身的问题不会影响浏览器主界面和网页
  + GPU硬件加速进程是独立的
+ 多线程模型
  + 每个进程内部，都有很多的线程![截屏2021-11-10 下午7.05.41](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-10 下午7.05.41.png)
    + 对于Browser进程，多线程主要目的是为了保持用户界面的高响应度，保证UI线程不会被任何其他费时的操作阻碍从而影响了对用户操作的响应
    + 在Renderer进程中，Chromium不让其他操作阻止渲染线程的快速执行

  + 网页加载和渲染过程基本工作方式：
    1. Browser进程收到用户的请求，首先由UI线程处理，而且将相应的任务转给IO线程，它随即将该任务传递给Renderer进程
    2. Renderer进程的IO线程经过简单解释后交给渲染线程。渲染线程接受请求，加载网页并渲染网页，这其中可能需要Browser进程获取资源和需要GPU进程来帮助渲染。最后Renderer进程将结果由IO线程传递给Browser进程
    3. 最后，Browser进程接收到结果并将结果绘制出来

+ Content接口
  + App
  + Browser
  + Common
  + Plugin
  + Renderer
  + Utility


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