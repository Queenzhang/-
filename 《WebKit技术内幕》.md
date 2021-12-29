###  《WebKit技术内幕》

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
+ Content接口:提供了一层对多进程进行渲染的抽象接口，而且还支持所有的HTML5功能、GPU硬件加速功能和沙箱机制
  + App：与应用程序或进程的创建和初始化相关，它被所有的进程使用，用来处理一些进程的公共操作，具体包括两种类型
    + 进程创建的初始化函数，也就是Content模块的初始化和关闭动作
    + 各种回调函数，用来告诉嵌入者启动完成，进程启动、退出，沙盒模型初始化开始和结束等
  + Browser
    + 对一些HTML5功能和其他一些高级功能实现的参与
    + ContentBrowserClient
  + Common：定义一些公共的接口
  + Plugin：通知嵌入者Plugin进程合适被创建
  + Renderer
    + 获取RenderThread的消息循环、注册V8 Extension、计算JavaScript表达式等
    + ContentRenderClient
  + Utility：让嵌入者参与Content接口中的线程创建和消息的过滤
+ WebKit和WebKIt2嵌入式接口
  + WebKit和WebKIt2不兼容
  

#### 资源加载和网络栈

+ 使用网络栈来下载网页和网页中的资源是渲染引擎工作过程的第一步，也是非常消耗时间的步骤

+ WebKit资源加载机制

  + 资源：网页本身就是一种资源，而且网页一般还需要依赖很多其他类型的资源，如图片、视频等

  + HTML支持的资源主要包括

    + HTML
    + JavaScript
    + CSS
    + 图片
    + SVG
    + CSS Shader（好像凉了。。。）
    + 视频、音频和字幕
    + 字体文件
    + XSL样式表

  + ![image-20211128185808103](/Users/queen/Library/Application Support/typora-user-images/image-20211128185808103.png)

  + 资源缓存：提高资源使用效率的有效方法。

    + 建立一个资源的缓存池，当WebKit需要请求资源的时候，先从资源池中查找是否存在相应的资源。如果有，WebKit则取出以便使用；如果没有，WebKit创建一个新的CacheResource子类的对象，并发送真正的请求给服务器，WebKit收到资源后将其设置到该资源类的对象中去，以便缓存后下次使用
    + 这里的缓存指的是内存缓存，而不是磁盘缓存

  + 资源加载器

    + 特定加载器：只加载某一种资源
    + CachedResourceLoader：缓存机制的资源加载器。所有特定加载器都共享它来查找并插入缓存资源
    + ResourceLoader：通用的资源加载器。在WebKit需要从网络或文件系统获取资源的时候使用该类只负责获得资源的数据，被所有特定资源加载器共享。与CachedResourceLoader没有继承关系

  + ![image-20211128185832502](/Users/queen/Library/Application Support/typora-user-images/image-20211128185832502.png)

    + 通常一些资源的加载是异步执行的，也就是资源的获取和加载不会阻碍当前WebKit的渲染过程，例如图片、CSS文件
    + 某些特别的资源比如JavaScript会阻碍主线程的渲染过程，WebKit会启动另一个线程去遍历后面的HTML网页，收集需要的资源URL，然后发送请求；同时，WebKit能够并发下载这些资源

  + 资源的生命周期

    + LRU（最近最少使用）算法

  + Chromium多进程资源加载

    ![image-20211128185918009](/Users/queen/Library/Application Support/typora-user-images/image-20211128185918009.png)

+ 网络栈

  + WebKit网络设施：交由各个移植来实现，主要是一些HTTP消息头、MIME消息、状态码等信息的描述和处理

  + Chromium网络栈

    + 基本组成：HTTP协议、DNS解析、SPDY、QUIC等

    + 从URLRequest类到Socket类的调用

      ![image-20211128190006648](/Users/queen/Library/Application Support/typora-user-images/image-20211128190006648.png)

    + 代理：![image-20211128190037061](/Users/queen/Library/Application Support/typora-user-images/image-20211128190037061.png)

    + 域名解析（DNS）：在建立TCP连接前需要解析域名[chrome://net-internals/#dns]

  + 磁盘本地缓存

    + Chromium的本地磁盘缓存特性
      1. 必须要有相应的机制来移除合适的缓存资源，以便加入新的资源
      2. 确保在浏览器崩溃时不破坏磁盘文件，至少能够保护原先在磁盘中的文件
      3. 能够高效和快速地访问磁盘中现有的数据结构，支持同步和异步两种访问方式
      4. 能够避免同时存储两个相同的资源
      5. 能够很方便地从磁盘中删除一个项，同时可以在操作一个项的时候不受其他请求的影响
      6. 磁盘不支持多线程访问，所以需要把所有磁盘缓存的操作放入单独的一个线程
      7. 升级版本时，如果磁盘缓存的内部存储结构发生改变，Chromium仍然能够支持老版本的结构

  + Cookie机制

    + 格式：关键字+值
    + 基于安全考虑，一个网页的Cookie只能被该网页（该域的网页）访问
    + 类型：
      + 会话型：只保存在内存中，当浏览器退出时即清除
      + 持续型：在有期内，每次访问该Cookie所属域的时候，都需要将该Cookie发送给服务器，这样服务器能够有效追踪用户的行为 

  + 安全机制：HTTP是一种使用明文来传输数据的应用层协议，构建在SSL之上的HTTPS提供了安全的网络传输机制。HSTS协议能让网络服务器声明他只支持HTTPS协议

  + 高性能网络栈

    + DNS预取：利用现有的DNS机制，提前解析网页中可能的网络连接
    + TCP预连接（Preconnect）：使用追踪技术来获取用户从什么网页跳转到另外一个网页，利用这些数据，一些启发式规则和其他一些暗示来预测用户下面会点击什么超链接，当有足够把握时，便先DNS预取，然后预先建立TCP连接
    + HTTP管线化：同时将多个HTTP请求一次性提交给服务器的技术。管线化机制需要通过永久连接完成，并且只有GET和HEAD等请求可以进行管线化

  + SPDY：核心思想是多路复用，仅使用一个连接来传输一个网页中的众多资源

    + 利用一个TCP连接来传输不限个数的资源请求的读写数据流
    + 根据资源请求的特性和优先级，SPDY可以调整这些资源请求的优先级
    + 只对这些请求使用压缩技术，可大大减少需要传送的字节数
    + 当用户浏览某个网页时，支持SPDY协议的服务器在发送网页内容时，可以尝试发送一些信息给浏览器，告诉后面可能需要哪些资源，浏览器可以提前知道并决定是否需要下载（甚至服务器可以主动发送资源）

    ![image-20211128190103317](/Users/queen/Library/Application Support/typora-user-images/image-20211128190103317.png)

  + QUIC：一种网络传输协议，主要目标是改进UDP数据协议的能力，解决传输层的传输效率，并提供了数据的加密

+ 高效的资源使用策略

  + DNS和TCP连接

    + 减少链接的重定向
    + 利用DNS预取机制
    + 搭建支持SPDY协议的服务器
    + 避免错误的链接请求

  + 资源的数量

    + 在HTML网页中内嵌小型的资源，即开发者可以将比较小的资源直接放在网页中（CSS、JavaScript、图片等）。可以通过base64将图片变成字符串，直接放入网页中
    + 合并一些资源，如将大量使用的小图片合并成一张大的图片以供使用

  + 资源的数据量

    + 使用浏览器本地磁盘缓存机制（对资源设置适当的失效期来减少浏览器对资源的重复获取）

    + 启用资源的压缩技术（使用zip技术对图片进行压缩，然后在HTTP消息头中说明该资源经过压缩，减少网络传输的数据量、减少无用的空格、启用异步资源加载等）

      PageSpeed

#### HTML解释器和DOM模型

+ DOM模型
  + DOM（Document Object Model）的全称是文档对象模型，它可以以一种独立于平台和语言的方式访问和修改一个文档的内容和结构。DOM定义的是一组与平台、语言无关的接口，该接口允许编程语言动态访问和更改结构化文档。使用DOM表示的文档被描述成一个树形结构，使用DOM的接口可以对DOM树结构进行操作。
  + DOM结构构成的基本要素是“节点”。（Document、Element、Entity、ProcessingIntruction、CDataSection、Comment等）
  + DOM树![截屏2021-11-28 下午7.35.26](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-28 下午7.35.26.png)
  
+ HTML解释器
  + HTML解释器将网络或者本地磁盘获取的HTML网页和资源从字节流解释成DOM树结构。![截屏2021-11-28 下午7.38.35](/Users/queen/Library/Application Support/typora-user-images/截屏2021-11-28 下午7.38.35.png)
  
  + ![截屏2021-11-28 下午7.41.50](/Users/queen/Desktop/截屏2021-11-28 下午7.41.50.png)
  
  + 词法分析：
  
    + 在分析前，解析器会先检查该网页内容使用的编码格式，以便后面使用合适的解码器。
  
    + HTMLTokenizer类
  
      ![截屏2021-12-03 下午10.08.23](/Users/queen/Library/Application Support/typora-user-images/截屏2021-12-03 下午10.08.23.png)
  
  + XSSAuditor验证词语：安全机制
  
  + 词语到节点：HTMLDocumentParser类调用HTMLTreeBuilder类的“construcuTree”函数来实现
  
  + 节点到DOM树：HTMLConstructionSite类中包含一个“HTMLElementStack”变量，它是一个保存元素节点的栈
  
  + 网页基础设施：Chrome类
  
    1. 功能
  
    + 跟用户界面和渲染显示相关的需要各个移植实现的接口集合类
    + 继承自HostWindow（宿主窗口）类，该类包含一系列接口，用来通知重绘或者更新整个窗口、滚动窗口等
    + 窗口相关操作，例如显示、隐藏窗口等
    + 显示和隐藏窗口中的工具栏、状态栏、滚动条等
    + 显示JavaScript相关的窗口，例如JavaScript的alert、confirm、prompt窗口等
  
    2.需求
  
    + 具备获取各个平台资源的能力
    + 把Webkit的状态和进度等信息派发给外部的调用者
  
  + 线程化的解释器：利用单独的线程来解释HTML文档。在webkit中，网络资源的字节流自IO线程传递给渲染线程之后，后面的解释、布局和渲染等工作基本上都是工作在该线程，也就是渲染线程完成的（当然这不是绝对的）。因为DOM树只能在渲染线程上创建和访问，这就是说构建DOM树的过程只能在渲染线程中进行，但是，从字符串到词语这个阶段可以交给单独的线程来做。
  
    ![截屏2021-12-05 下午7.40.15](/Users/queen/Library/Application Support/typora-user-images/截屏2021-12-05 下午7.40.15.png)
  
    ![截屏2021-12-05 下午7.40.15](/Users/queen/Library/Application Support/typora-user-images/截屏2021-12-05 下午7.42.12.png)
  
  + JavaScript的执行：发生在将字符串解释成词语之后、创建各种节点的时候。Javascript代码可能会修改文档结构，它的执行会阻碍后面节点的创建，同时也会阻碍后面的资源下载，这导致了资源不能并发下载的严重影响性能的问题。当DOM树构建完之后，Webkit触发“DOMContentLoaded”事件，注册在该事件上的Javascript函数会被调用。当所有资源都被加载完之后，Webkit触发“onload”事件
  
    + 建议：
      1. 将“script”元素加上“async”属性
      2. 将“script”元素放在“body”元素的最后
  
+ DOM的事件机制

  + 事件的工作过程：

    + 事件在工作过程中使用两个主体，event（事件）和EventTarget（事件目标）。每个事件都有属性来标记该事件的事件目标。当事件到达事件目标的时候，这个目标上注册的Event Listeners（监听者）都会被触发调用，这些监听者的调用顺序是不固定的，所以不能依赖监听者注册的顺序来决定代码逻辑。

    + 事件处理最重要的就是Event Capture（事件捕获）和Event bubbling（事件冒泡）。当渲染引擎接收到一个事件的时候，会检查哪个元素是直接的事件目标

      + 事件捕获是自顶向下，即事件先到document节点，然后一路到达目标节点。事件可以在这一传递过程中被捕获，只需要在注册监听者的时候设置相应的参数即可。默认情况下，其他节点不捕获这样的事件。如果网页注册了这样的监听者，那么监听者的回调函数会被调用，通过“stopPropagation”函数阻止

      + 事件冒泡是自下向上，它的默认行为是不冒泡，但是事件包含一个是否冒泡属性，也可以通过“stopPropagation”函数阻止

        ![截屏2021-12-06 下午9.15.56](/Users/queen/Library/Application Support/typora-user-images/截屏2021-12-06 下午9.15.56.png)

  + webkit事件处理机制：DOM事件分为多种，其中与用户相关的一种为UIEvent。UIEvent包括但不限于FocusEvent、MouseEvent、KeyboardEvent、Composition Event等。WebKit浏览器事件处理过程首先是做HitTest，查找事件发生处的元素，检测该元素有无监听者。如果注册了，那么浏览器会把事件派发给WebKit内核来处理。同时，浏览器也可能需要理解和处理这样的事件。这主要是因为，有些事件浏览器必须响应从而对网页做默认处理。（Web开发者可以在监听者的代码中调用事件的preventDefault函数来阻止浏览器触发默认处理行为）

+ 影子（Shadow）DOM：主要解决了一个文档中可能需要大量交互的多个DOM树建立和维护各自的功能边界的问题。

  + 影子DOM的规范草案能够使得一些DOM节点在特定范围内可见，而在网页的DOM树中却不可见，但在网页渲染的过程中包含了这些节点，这就使得封装变得容易很多。当使用JavaScript代码访问HTML文档的DOM树的时候，通常的接口是不能直接访问到影子DOM子树中的节点的，只能通过特殊的接口方式。HTML5中的视频、音频也是使用了这一思想
  + 事件目标其实就是包含影子DOM子树的节点对象。事件捕获逻辑没有变化，在影子DOM子树内也会继续传递。当影子DOM子树中的事件向上冒泡的时候，WebKIt会同时向整个文档的DOM上传递该事件，以避免一些奇怪的行为

#### CSS解释器和样式布局

+ CSS基本功能

  + Cascading Style Sheet，级联样式表，主要用来控制网页的显示风格。

  + 样式的来源：1.网页开发者编写的样式，被包含在网页或外部样式文件中；2.读者设置的样式信息；3.浏览器内在默认样式。优先级递减

  + 样式规则在：CSS规范的最近本的组成。包含两部分：规则头（由一个或多个选择器组成）、规则体（由一个或多个样式声明组成，每个样式声明由样式名和样式值构成，表示这个规则对哪些样式进行了规定和设置）。

    ![截屏2021-12-07 下午9.01.59](/Users/queen/Library/Application Support/typora-user-images/截屏2021-12-07 下午9.01.59.png)
  
  + 选择器：一组模式，用来匹配相应的HTML元素。
  
    + 标签选择器
    + 类型选择器
    + ID选择器
    + 属性选择器
    + 后代选择器
    + 子女选择器
    + 相邻同胞选择器
  
    + 伪类选择器
  
  + 优先级高的选择器所设置的属性值将会应用到该元素上
  
  + 框模型（Box model）：CSS标准中引入来表示HTML标签元素的布局结构。
  
    + 外边距（margin）
  
    + 边框（border）
  
    + 内边距（padding）
  
    + 内容（content）
  
      ![截屏2021-12-26 上午11.57.14](/Users/queen/Library/Application Support/typora-user-images/截屏2021-12-26 上午11.57.14.png)
  
  + 包含块模型：当Webkit计算元素的箱子的位置和大小时，Webkit需要计算该元素和另外一个矩形区域的相对位置，这个矩形区域称为该元素的包含块
  
    + 根元素的包含块称为初始包含块，通常大小为可视区域（Viewport）大小
    + 对于其他位置属性设置为static和relative的元素，它的包含块就是最近祖先的箱子模型中的内容区域
    + 位置属性为fixed，那么该元素的包含块脱离HTML文档，固定在可视区域的某个特定位置
    + 位置属性为absolute，那么该元素的包含块由最近的含义属性absolute、relative、fixed的祖先决定
  
  + CSS样式属性
  
    + 背景
    + 文本
    + 字体
    + 列表
    + 表格
    + 定位
  
  + CSSOM:CSS对象模型。它的思想是在DOM中的一些节点接口中，加入获取和操作CSS属性或者接口的Javascript接口，因而Javascript可以动态操作CSS样式
  
+ CSS解释器和规则匹配

  + 样式的Webkit表示类：
    + DocumentStyleCollection类包含了所有CSS样式表
    + Webkit使用CSSStyleSheet类来表示CSS样式表（不管内嵌还是外部文档）。它包含CSS的href、类型、内容等信息
    + CSS的内容就是样式信息StyleSheetContents，包含了样式规则（StyleRuleBase）列表
    + StyleSheetResolver类将解释后的规则组织起来，用于为DOM中的元素匹配相应的规则，从而应用规则中的属性值序列
    + ![WechatIMG120](/Users/queen/Desktop/WechatIMG120.png)
  + 解释过程：从CSS字符串经过CSS解释器处理后变成渲染引擎的内部规则表示的过程
    + Webkit解释CSS内容时，调用CSSParser对象来设置CSSGrammer对象等，解释过程中需要的回调函数由CSSParser来负责处理，最后Webkit将创建好的结果直接设置到StyleSheetContents对象中
    + 在解释网页中自定义的样式之前，Webkit渲染引擎会为每个网页设置一个默认的样式
    + 样式规则建立完成后，Webkit将规则结果保存在DocumentRuleSets对象类中
  + 样式规则匹配
    + 使用StyleResolver类来为DOM的元素节点匹配样式，将样式信息保存到RenderStyle中
    + RenderStyle对象被RenderObject类管理和使用
    + 规则的匹配由ElementRuleCollector类计算并获得
  + Javascript设置样式：CSSOM定义了JavaScript访问样式的能力和方式，这需要JavaScript引擎和渲染引擎协同完成

+ Webkit布局
  + 基础
    + 当Webkit创建RenderObject对象之后，每个对象是不知道自己的位置、大小等信息的，Webkit根据框模型来计算位置、大小等信息的过程称为布局计算
    + 布局计算分为
      1. 对整个RenderObject树进行计算
      2. 对RenderObject树中某个子树进行计算，常见于文本元素或overflow：auto块的计算（这种情况一般是其子树布局改变不影响周围元素的布局，不需要重新计算更大范围的布局）
  + 布局计算：一个递归的过程
    + ![WechatIMG121](/Users/queen/Desktop/WechatIMG121.png)
    + 样式发生变化就需要重新计算布局
      + 首次打开网页时（可视区发生变化时）
      + 网页动画触发布局计算
      + JavaScript代码通过CSSOM等直接修改样式信息
      + 用户的交互（如翻滚网页等）
    + 布局计算相对比较耗时，一旦布局发生变化，Webkit需要重绘，减少样式变动可以依赖一些HTML5的新功能来提高网页的渲染效率
  + 布局测试：用于测试网页的整个渲染结果，包括网页加载和渲染整个过程

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

使用HTML技术来编写网页或Web应用，了解其背后的工作原理是写出高效代码的有效捷径。Webkit只是浏览器内核的其中一种，对于它的学习不能包括其他主流浏览器，但也是很有借鉴意义