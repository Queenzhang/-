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

+ RenderObject树：Webkit使用RenderObject树进行布局计算并保存计算结果
  + Webkit需要将可视节点的内容绘制到最终的网页结果中，因此需要为它们建立相应的RenderObject树
    + DOM树的document节点
    + DOM树种的可视节点，如html、body、div等
    + 匿名的RenderObject节点，该节点不对应于DOM树中的任何节点，而是Webkit处理上的需要
  + 对于影子节点，Webkit也需要创建并渲染RenderObject
  + ![1251641303724_.pic](/Users/queen/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/70c82dfb9120d9582c942df73e168a61/Message/MessageTemp/9e20f478899dc29eb19741386f9343c8/Image/1251641303724_.pic.jpg)
  + RenderObject类包含了很多虚函数
    + 遍历和修改RenderObject树的函数，如parent()、firstChild()、addChild()
    + 计算布局和获取布局相关信息的函数，如layout()、style()
    + 判断RenderObject对象属于哪种类型的子类
    + 跟RenderObject对象所在的RenderLayer对象相关的操作
    + 坐标和绘图相关的操作，如paint()、repaint()
  + 创建RenderObject的过程
    1. Webkit检查DOM节点是否需要创建RenderObject
    2. 如果需要，Webkit建立或获取一个创建RenderObject对象的NodeRenderingContext对象，它会分析RenderObject对象的父节点、兄弟节点等，设置这些信息后完成插入树的操作
+ 网页层次和RenderLayer树
  + 网页是可以分层次的，一是为了方便网页开发者开发网页并设置网页的层次；二是为了Webkit处理上的遍历，即简化渲染的逻辑
  + Webkit会为网页的层次创建相应的RenderLayer对象，RenderLayer树是基于RenderObject树建立的。RenderLayer节点和RenderObject节点不一一对应，而是一对多
  + RenderObject节点需要建立新的RenderLayer节点的规则
    + DOM树的Document节点对应的RenderView节点
    + DOM树中的Document的子女节点，即HTML节点对应的RenderBook节点
    + 显式指定CSS位置的RenderObject节点
    + 有透明效果的RenderObject节点
    + 节点有溢出（overflow）、alpha或者反射等效果的RenderObject节点
    + 使用Canvas2D和3D技术的RenderObject节点
    + Video节点对应的RenderObject节点
  + RenderLayer类没有子类，它表示的是网页的一个层次，没有“子层次的说法”
  + 构建RenderLayer树：根据规则判断是否需要建立一个新的RenderLayer对象，并设置RenderLayer对象的父亲和兄弟关系即可
+ 渲染方式
  + 绘图上下文：绘图操作被定义了一个抽象层，即绘图上下文。可分为2D绘图上下文和3D绘图上下文
  + 渲染方式：软件渲染、硬件加速渲染、混合渲染
    + 软件渲染（CPU）：节省内存，但是只能处理2D方面的操作。简单的网页没有复杂绘图或者多媒体方面的需求比较适合
    + 硬件加速渲染（GPU）：适合需要使用3D绘图的操作。但会消耗更多内存资源。
    + 混合操作：结合前两者的优点
+ Webkit软件渲染技术
  + 软件渲染过程：Webkit遍历RenderLayer树来绘制各个层，对于每个RenderObject对象，需要三个阶段绘制，第一阶段是绘制该层中所有块的背景和边框，第二阶段是绘制浮动内容，第三阶段是前景（内容部分、轮廓等）。
  + Chromium的多进程软件渲染技术：通过引入多进程模型，Chromium将渲染结果从Renderer进程传递到Browser进程。

#### 硬件加速机制

+ 硬件加速基础

  + GPU的硬件能力来帮助渲染网页：一旦有更新请求，如果没有分层，引擎可能需要重新绘制所有的区域。当网页分层之后，部分区域的更新可能只在网页的一层或几层，而不需要将整个网页都重新绘制。通过重绘网页的一个或几个层，并将它们和其他之前完成的层合成起来，既能使用GPU的能力，又能减少重绘的开销
  + 硬件加速机制在RenderLayer树建立后需要：
    + Webkit决定将哪些RenderLayer对象组合在一起，形成一个有后端存储的新层，这一层不久后会用于之后的合成（合成层）。每个新层都有一个或多个后端存储（可能是GPU的内存）。对于一个RenderLayer对象，如果它没有后端存储的新层，就使用它的父亲所使用的合成层
    + 将每个合成层包含的这些RenderLayer内容绘制在合成层的后端存储中，可以是软件绘制也可以是硬件绘制
    + 由合成器将多个合成层合成起来，形成网页的最终可视化结果，实际就是一张图
  + 把C代码宏“ACCELERATED_COMPOSITING”打开后，硬件加速机制才会被开启，有关硬件加速的基础设施才会被编译进去
  + RenderLayerBacking对象：每个合成层都有一个RenderLayerBacking，它负责管理RenderLayer所需要的所有后端存储，存储空间使用GraphicsLayer类表示。每个GraphicsLayer都使用一个GraphicsLayerClient对象，该对象能够收到GraphicsLayer的一些状态更新信息，并包含一个绘制该GraphicsLayer对象的方法
  + 合成层特征：
    + RenderLayer具有CSS 3D属性或CSS透视效果
    + RenderLayer包含的RenderObject节点表示的是使用硬件加速的视频解码技术的HTML5“video”元素
    + RenderLayer包含的RenderObject节点表示的是使用硬件加速的Canvas 2D元素或WebGL技术
    + RenderLayer使用了CSS透明效果的动画或CSS变换的动画、
    + RenderLayer使用了硬件加速的CSS Filters技术
    + RenderLayer使用了剪裁（Clip）或反射（Reflection）属性，并且它的后代中包括一个合成层
    + RenderLayer有一个Z坐标比自己小的兄弟节点，且该节点是一个合成层
  + 合成层的好处：
    + 合并一些RenderLayer层，减少内存的使用量
    + 合并之后，尽量减少合并带来的重绘性能和处理上的困难
    + 对于那些使用单独层能够显著提升性能的RenderLayer对象，可以继续使用这些好处，如canvas元素
  + ![1271641902107_.pic_hd](/Users/queen/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/70c82dfb9120d9582c942df73e168a61/Message/MessageTemp/9e20f478899dc29eb19741386f9343c8/Image/1271641902107_.pic_hd.jpg)
  + 硬件渲染过程：
    + 确定并计算合成层
    + 遍历和绘制每一个合成层
    + 渲染引擎将所有绘制完的合成层合成起来
  + 3D图形上下文：提供一组抽象接口，提供类似OpenGLES的功能，其主要目的是使用OpenGL绘制3D图形的能力

+ Chromium的硬件加速机制

  + GraphicsLayer的支持![1281641902115_.pic_hd](/Users/queen/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/70c82dfb9120d9582c942df73e168a61/Message/MessageTemp/9e20f478899dc29eb19741386f9343c8/Image/1281641902115_.pic_hd.jpg)

  + 框架：在Chromium中，所有的GPU硬件加速都是由一个进程负责完成的。GPU进程处理一些命令后，会向Renderer进程报告自己当前的状态，Renderer进程通过检查状态信息和自己的期望结果来确定是否满足自己的条件。GPU进程最终绘制的结果不再像软件渲染那样通过共享内存传递给Browser进程，而是直接将页面的内容绘制在浏览器的标签窗口内![1301641902132_.pic_hd](/Users/queen/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/70c82dfb9120d9582c942df73e168a61/Message/MessageTemp/9e20f478899dc29eb19741386f9343c8/Image/1301641902132_.pic_hd.jpg)

  + 命令缓冲区：主要用于GPU进程和GPU的调用者进程传递GL操作命令。现有的实现是基于共享内存的方式来完成的，因而命令是基于GLES编码成特定的格式存储在共享内存中。共享内存方式采用了环形缓冲区的方式来管理，这表示内存可以循环使用，旧的命令会被新的命令所覆盖。

    + 一条命令分为命令头和命令体。命令头是命令的原数据信息，包含命令的长度和命令的标识；命令体包含命令所需要的的其他信息，如命令的立即操作数
    + 命令本身是保存在共享内存中的，另外共享内存的大小是固定的，对于传输较大数据的命令，如TexImage2D，Chromium采用Bucket机制。它的原理是：通过共享内存机制来分块传输，而后把分块的数据保存在本地的桶内，从而避免申请大块的共享内存
  + Chromium合成器：将多个合成层合成并输出一个最终的结果，所以它的输入是多个待合成的合成层，每个层都有一些属性，输出是一个后端存储
  
    + 架构上，合成器采用表示和实现分离的原则![1311641902140_.pic_hd](/Users/queen/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/70c82dfb9120d9582c942df73e168a61/Message/MessageTemp/9e20f478899dc29eb19741386f9343c8/Image/1311641902140_.pic_hd.jpg)
    + 合成器的主要组成分为：事件处理、合成层的表示和实现、合成层组成两种类型的树、合成调度器、合成器的输出结果、各种后端存储等资源、支持动画和3D变形功能所需的基础设施
    + 合成过程：
      1. 创建输出结果的目标对象“Surface”，即合成结果的存储空间
      2. 开始一个新的帧，包括计算滚动和缩放大小、动画计算、重新计算网页的布局、绘制每个合成层等
      3. 将Layer树中包含的这些变动同步到LayerImpl树中
      4. 合成LayerImpl树中的各个层并交换前后帧缓冲区，完成一帧的绘制和显示动作
    + 减少重绘：使用合适的网页分层技术以减少需要重新计算的布局和绘图；使用CSS 3D变形和动画技术
  
+ 其他硬件加速模块

  + 2D图形的硬件加速机制：使用GPU来绘制2D图形方法；应用场景：1.网页基本元素的绘制；2.HTML5的canvas元素
  + WebGL
  + CSS 3D变形
  + 其他：视频解码和播放等

#### JavaScript引擎

 + 设计之初的目标：解决一些脚本语言的问题，没有重点考虑性能。出现是为了控制网页客户端的逻辑，例如用户交互、异步通信。

  + 特点：

    + 本质上是一种解释型语言，函数是第一等公民，也就是函数能够当做参数或返回值来传递。
    + 动态类型：没法在编译的时候知道变量类型，只有在运行时才能确定，导致JavaScript语言的规范面临性能方面的巨大压力。与C++相比，编译确定位置、偏移信息共享、偏移信息查找都有差异
    + JIT（Just-In-Time）技术：作用是解决解释型语言的性能问题，主要思想是当解释器将源代码解释成内部表示的时候，JavaScript的执行环境不仅是解释这些内部表示，而是将其中一些字节码转成本地代码（汇编代码），这样可以被CPU直接执行，而不是解释执行

  + 闭包：一个拥有许多变量和绑定了这些变量的环境的表达式，因而这些变量也是该表达式的一部分。JavaScript使用作用域链来实现闭包。只希望内部调用，可以用一个匿名函数，不会污染全局空间，其内部函数也只在匿名函数内有效，不会影响其他代码

  + JavaScript引擎：能够将JavaScript代码处理并执行的运行环境。

    ![1341642302509_.pic_hd](/Users/queen/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/70c82dfb9120d9582c942df73e168a61/Message/MessageTemp/9e20f478899dc29eb19741386f9343c8/Image/1341642302509_.pic_hd.jpg)

    ![1351642302513_.pic_hd](/Users/queen/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/70c82dfb9120d9582c942df73e168a61/Message/MessageTemp/9e20f478899dc29eb19741386f9343c8/Image/1351642302513_.pic_hd.jpg)
    
    对于JavaScript语言，现在将抽象语法树转成中间表示（也就是字节码），然后通过JIT技术转成本地代码。当然也有些直接从抽象语法树生成本地代码的的JIT技术，例如V8。
    
    ![截屏2022-01-16 上午11.48.57](/Users/queen/Library/Application Support/typora-user-images/截屏2022-01-16 上午11.48.57.png)
    
    + JavaScript引擎包含：
      + 编译器
      + 解释器
      + JIT工具
      + 垃圾回收器和分析工具
    + JavaScript引擎和渲染引擎：从模块上看，它们是独立的模块，JavaScript引擎负责执行JavaScript代码，渲染引擎负责渲染网页。但是实际上两种引擎通过桥接接口来访问DOM结构
    
  + V8引擎：目的就是提高性能。

    + API（应用程序编程接口）：
        + 各种各样的基础类
        + Value
        + V8数据的句柄类
        + Isolate
        + Context
        + Extension
        + Handle
        + Script
        + HandleScope
        + FunctionTemplate
        + ObjectTemplate
    + 工作原理：
        + 数据表示：在V8中，数据的表示分为两个部分：数据的实际内容（变长）和数据的句柄（定长）
        + 工作过程：编译和运行。还有一个重要特点：延迟（deferred），这使得很多JavaScript代码的编译直到运行的时候被调用才会发生，可以减少时间开销
            + 编译：
                1. 将源代码转变成抽象语法树
                2. 通过JIT编译器的全代码生成器从抽象语法树直接生成本地代码（减少抽象树到字节码的转换时间，在网页加载时提高优化的可能，缺点是在某些JavasCript使用场景使用解释器会更合适；没有中间表示会减少优化的机会）
            + 运行：
                1. 通过数据分析器来采集一些信息，以帮助决策哪些本地代码需要优化，以生成效率更高的本地代码
                2. 当发现优化后的代码性能其实没有提高甚至有所降低时，能够退回到原来的代码
        + 优化回滚：这是一个很费时的操作，所以能够不回滚肯定不要回滚
        + 隐藏类和内嵌缓存：
            + 隐藏类：使用类和偏移位置思想，将本来需要通过字符串匹配来查找属性值的算法改进为使用类似C++编译器的偏移位置的机制来实现
            + 内嵌缓存：可以避免方法和属性被存取的时候出现的因哈希表查找而带来的问题。基本思想是将使用之前查找的结果缓存起来，当下次查找的时候，首先比较当前对象是否也是之前查找的隐藏类，减少查找表的时间
        + 内存管理：
            + 内存的划分
                1. Zone类：管理一系列的小块内存
                2. 堆：分为年轻分代、老年分代、大对象
            + 对Javascript代码的垃圾回收机制
        + 快照：将内置的对象和函数加载之后的内存保存并序列化。也能够将一些开发者认为需要的JS文件序列化，以减少以后处理的时间，但是这些代码没有办法被CrankShaft等优化编译器优化，存在性能上的问题
    + 绑定和扩展
        + Extension机制：通过V8提供的基类Extension来达到扩展JavaScript能力的目的
        + 绑定：使用IDL文件或者接口文件来生成绑定文件，然后将这些文件同V8引擎的代码一起编译

  + JavaScriptCore引擎：Webkit的默认引擎

    + 数据表示：同样使用句柄来表示数据
    + 模块：
        + JavaScriptCore引擎不是从抽象语法树生成本地代码，而是生成平台无关的字节码
        + 在字节码之后，JavaScriptCore包含了字节码解释器
        + JavaScriptCore在获悉热点函数后，需要对他们进行优化，就会使用简单JIT编译器，将对应函数的字节码翻译成本地代码
        + JavaScriptCore引入DFG JIT编译器，在字节码基础上生成基于SSA的中间表示
        + JavaScriptCore引入LLVM：将多个不同的前端语言转化成不同的后端本地代码
    + 内存管理：JSGlobalData（类似Zone）和分代垃圾回收机制
    + 绑定：类似V8

  + 高效的JavaScript代码

    + 编程方式：
        + 类型:对于函数只是使用某个类型的对象或者较少类型，以此减少缓存失误的几率从而提高性能；同时对于数组，尽量使用存放相同类型的数据，可以通过偏移位置来访问它们（asm.js）
        + 数据表示：因为使用了一部分位来表示数据，整数表示的范围缩小，所以对于较大的整数需要用堆来保存。能使用整数的，尽量不要使用浮点类型
        + 内存：即时回收不需要使用的内存
        + 优化回滚：不要书写触发出现优化回滚的代码；在执行多次之后，不要出现修改对象类型的语句
        + 新机制：使用JavaScript引擎或渲染引擎提供的新机制和新接口
    + 未来趋势：提高性能
        + JavaScript语言和规范的发展：并行JavaScript（WebWorker）
        + JavaScript引擎技术的发展和创新
        + 高效的代码，使用新技术和回避一些会对引擎带来重大性能伤害的用法

#### 插件和JavaScript扩展

虽然目前浏览器功能强大，但仍有能力不足的时候。尤其早期，Web开发者希望通过一些机制来扩展浏览器能力，便有了插件机制（有名的Flash），现在流行的是混合编程模式。插件机制扩展了浏览器的能力，丰富了网页的应用场景。同时，随着HTML5的发展，很多HTML5功能需要扩展JavaScript的编程接口，以便开发者可以使用JavaScript代码来调用。

插件其实是一种统称，表示一些动态库，这些动态库根据定义的一些标准接口可以跟浏览器进行交互。

+ NPAPI插件：网景插件应用程序编程接口，用于让浏览器执行外部程序，以支持网页中各种格式的文件，如视频、音频和PDF文件等。在NPAPI插件系统中，通常做法是当网页需要显示该插件或者需要更新的时候，它会发送一个失效的通知，让插件来绘制它们
+ Chromium PPAPI插件：PPAPI的提出是因为NPAPI的可移植性和性能存在比较大的问题，特别是针对跨进程的插件。它引入了一个保留模式，其含义是浏览器始终保留一个后端存储空间，用来表示上一次绘制完的区域
+ Native Client：一种沙箱技术，能够提供给平台无关的不受信本地代码一个安全的运行环境，可以针对那些计算密集型的需求，例如游戏引擎、可视化计算、大数据分析、3D图形渲染等，这些场合只需要访问有限的一些本地接口，不需要通过网络服务来计算，以免占用额外的带宽资源。本身也是一个PPAPI插件。
+ JavaScript引擎的扩展机制：
  + V8-Javascript绑定
  + V8-Extension机制
  + JavaScriptCore-JavaScript绑定

+ Chromium扩展机制

#### 多媒体

+ HTML5的多媒体支持：在此之前，网页对视频和音频播放的支持基本上都是依靠Flash插件。而在HTML5之后，音频和视频直接成为HTML一系列规范中的第一等公民

  + 网页可以直接支持多媒体的播放
  + JavaScript接口的支持：控制音视频的播放、停止、记录等
  + 支持其他技术进行操作：CSS技术来修改样式，结合Canvas或WebGL等

  在HTML5中，对于多媒体的支持大概包括：

  + ”video“
  + “audio”
  + 将多个声音合成处理的WebAudio技术
  + 将照相机、麦克风功能与视频、音频和通信结合起来使用的WebRTC（网络实时通信）

  一个完整的多媒体解决方案总体有四大部分：

  + Webkit基础部分，包括对规范的支持，这其中有DOM树、RenderObject树和RenderLayer树等
  + Chromium的桥接部分，也就是将Webkit的接口桥接到Chromium项目中，包括接口、渲染等
  + 依赖其他多媒体库，包括ffmpeg、libjingle等
  + Chromium对多媒体资源获取和使用多媒体库来帮助解码等管线化过程的具体实现

+ 视频

  + 资源获取：使用缓存机制或者其他机制来预先获取视频资源
  + 基础设施：![image-20220317132626537](/Users/queen/Library/Application Support/typora-user-images/image-20220317132626537.png)
  + 桌面系统：Chromium使用了一套多媒体播放框架，而不是直接使用系统或第三方库的完整解决方案
  + Android系统：直接使用系统自带的多媒体功能
  + 字幕：W3C已经开始支持字幕的“track”元素，而字幕文件采用的格式是WebVTT格式
  + 视频扩展：包括Media Source接口，音视频资源保护等

+ 音频

  + 音频元素：HTML 5 Audio元素
  + 基础设施：当webkit和Chromium需要输出解码后的音频数据时，通过从右侧自上向下、左侧自下向上的过程，然后使用共享内存的方式将解码后的数据输出到实际的物理设备中
  + Web Audio：提供了高层次的JavaScript接口，用来处理和合成声音
  + MIDI和Web MIDI：MIDI是一个通信标准，是电子乐器之间以及电子乐器与电脑之间的统一交流协议。Web MIDI技术定义了一系列接口来接收和发送MIDI指令，但是该技术本身并不提供语义上的控制，只是负责传输这些指令，所以渲染引擎其实并不知道这些指令的实际含义，这个与Web Audio不同
  + Web Speech：语音识别技术（Speech-to-Text）和合成语音技术（Text-to-Speech）。Web Speech是讲语音识别和合成语音技术提供给JavaScript接口，这样Web前端开发者可以在网页中使用它们

+ WebRTC：Web实时通信技术是一种提供实时视频通信的规范

  + 音视频输入和输出设备
  + 网络连接的建立
  + 数据捕获、编码和发送
  + 数据接收、解码和显示

#### 安全机制

+ 网页安全模型：当用户访问网页的时候，浏览器需要确保该网页中数据的安全性，如Cookie、用户名、密码等信息不会被其他的恶意网页所获取。
  + 域（origin）：网页所在的域名、传输协议和端口等信息，是表明网页身份的重要标识。默认情况下，不同网页间的数据是被浏览器隔离的，不能互相访问（Same origin Policy）。跨域攻击是网页安全最主要的问题之一
  + XSS（Cross Site Scripting）：执行跨域的JavaScript脚本代码。可以在HTTP消息头中定义一个名为“X-XSS-Protection”的字段，此时，浏览器会打开防止XSS攻击的过滤器
  + CSP（Content Security Policy）：一种防止XSS攻击的技术，它使用HTTP消息头来指定网站能够标注哪些域中的哪些类型的资源被允许加载在该域的网页中，包括javaScript、CSS、HTML Frames、字体、图片和嵌入对象（插件、Java Applet等）
  + CORS（Cross Origin Resource Sharing）：跨域资源共享，也是借助于HTTP消息头并通过定义一些字段来实现不同域之间交互数据
    + CSP定义的是网页自身能够访问的某些域和资源，而CORS定义的是一个网页如何才能访问被同源策略禁止的跨域资源，规定了两者交互的协议和方式
  + 消息传递机制（Cross Document Messaging）：通过window.postMessage接口让JavaScript在不同域的文档中传递消息称为可能。
  + 安全传输协议（HTTPS）：HTTPS是在HTTP协议之上使用SSL技术来对传输的数据进行加密，从而保证了数据的安全性。
    + SSL工作的主要流程是先进行服务器认证，然后是用户认证
    + TLS是在SSL3.0基础上发展起来的，它使用了新的加密算法，所以同HTTPS不兼容。它用于两个通信应用程序之间，提供保密性和数据完整性
+ 沙箱模型
  + 原理：对于网络上的网页，浏览器认为它们是不安全的，因为网页总是存在各种可能性。沙箱模型就是一种机制，将网页的运行限制在一个特定的环境中，使它只能访问有限的功能，那么即使网页工作的渲染引擎被攻击，它也不能获取渲染引擎工作的主机系统中的任何权限。
  + 实现机制：沙箱模型严重依赖操作系统提供的技术，而不同操作系统提供的安全技术不一样，因此需要分别针对不同平台来实现。

#### 移动WebKit

+ 触控和手势事件：

  + HTML5 Touch Events：推荐的规范。该标准主要是定义如何将原始的触控事件以特定的方式传递给JavaScript引擎，然后再传递给注册的事件响应函数。在标准定义中，Touch Event分为四种类型：touchstart、touchmove、touchend和touchcancel
  + Gesture Events：Safari浏览器支持。由浏览器来识别原始事件并将手势事件传递给Javascript代码。时间类型分为gesturestart、gesturechange、gestureend

+ meta标签可以帮助提供非常好的移动用户体验,如使网页的宽度适合屏幕、控制网页缩放等

  ```html
  <meta name="viewport" content="width=device-width,initial-sacle=0.9,minimum-sacle=0.5,maxium-scale=1.0,user-scaleable = no"> 
  ```

+ Media Queries技术：响应式设计的基本思想是根据不同分辨率或者不同大小的屏幕，设计不同的布局。通过CSS规范中的Media Queries技术，区分屏幕或使用场景

  ```css
  @media(min-width:1280px) and (min-height:720px) and (orientation:landscape) {
    body{……}
  }
  ```

+ 其他机制：

  + 新渲染机制：提升渲染性能来增加响应速度，甚至不惜牺牲一些跟规范定义的行为不一致的地方。
    + Tiled Backing Store：使用后端的缓存技术来预先绘制网页和减少网页的重绘动作（使用空间换时间的思路）
    + 线程化渲染：将渲染过程分为若干个独立的步骤，然后使用不同的线程来完成其中的某个或几个步骤（一个重要的发展方向）
    + 快速移动翻页：webkit要在快速滚动中绘制一个静止的元素非常困难，只能通过慢速重绘，去避免一种Rendering Artifacts（前面一帧的某些数据出现在后面的绘制中）
  + Application Cache（应用缓存）：这一机制能够支持离线浏览，同时还能加速资源的访问并加快启动速度。其基本思想是使用缓存机制并缓存那些需要保存在本地的资源，开发者可以指定哪些是需要缓存的资源。
  
  ```html
  <html manifest="app.appcache">
  ```
  
  ```js
  var appCache = window.applicationCache
  appCache.addEventListener("updateready",function(event){
    if(appCache.status == appCache.UPDATEREADY){
      appCache.swapCache()
    }else{
      ...
    }
  })
  appCache.update()
  ```
  
  
  
  + Frame Flatterning（网页的多框结构）:该技术的含义是将框中的内容全部显示在网页中，通俗来讲就是将框中的内容平铺在网页中，而不用设置滚动条

#### 调试机制

​	支持调试HTML、CSS和JavaScript代码是浏览器或者渲染引擎需要提供的一项非常重要的功能。其中包括两种调试类型：功能——帮助HTML开发者使用单步调试等技术来查找代码中的问题；性能——采集JavaScript代码、网络等性能瓶颈。

+ Web Inspector
  + 元素审查（Elements）：帮助开发者查看每一个DOM元素，同样可以查看它的样式信息
  + 资源（Resources）：帮助开发者查看各种资源信息，包括内存存储、Cookie、离线缓存等
  + 网路（Network）：帮助开发者了解和诊断网络功能和性能
  + Javascript代码（Sources）：调试JavaScript代码，能够设置断点、单步调试语句等
  + 时间序列（Timeline）：能够按照时间次序来收集网页消耗的内存、绘制的帧数和生成各种事件，帮助开发者分析网页性能
  + 性能收集器（Profiles）：能够收集JavaScript代码使用CPU的情况、JavaScript堆栈、CSS选择器等信息，帮助开发者分析网页的运行行为
  + 诊断器（Audits）：帮助开发者分析网页可能存在的问题或者可以改善的地方
  + 控制台（Console）：可以输入JavaScript语句，由JavaScript引擎计算出结果。插件“PageSpeed”能够帮助全方位分析各种可能的优化点
+ 协议：调试机制的前端和后端通过使用一定格式的数据来进行通信，这些数据使用JSON格式来表示。 
+ 远程调试：Chromium支持远程调试
+ Chromium Tracing机制：如果需要分析Chromium自身问题，就可以借助这一工具

#### Web前端的未来

+ 趋势
  + 技术上
    1. web能力的逐渐加强
    2. web中将引入并行计算的能力
    3. 性能将提升
    4. 从web网页向web应用发展
  + 大方向上
    1. 平台化策略：web运行平台可以管理和运行web应用，即开发出同本地应用能力一样的应用程序，这方面浏览器不一定支持（虽然很多web运行平台是从浏览器基础上开发的，但不一样）
    2. 移动化：能够跨操作系统，在移动领域是HTML5不停向前发展的一个推力
    3. 向不同应用领域渗透：对于一些热门领域如游戏，因为对功能和性能要求高，所以浏览器和Web平台对游戏的支持是非常重要的发展方向
    4. web和HTML5技术：向不同的嵌入式领域发展，因为跨平台和低成本性，很适合应用在电视、车载系统、家用电器等领域
+ 嵌入式应用模式：很多web运行平台是基于嵌入式模式的接口开发出来的
  + 嵌入式模式：在渲染引擎之上提供一层本地（C++或Java）接口，这些接口提供了渲染网页的能力，渲染的结果被绘制到一个控件或者子窗口中，本地应用通过本地接口来获得渲染网页的能力。
  + 两个典型的基于Webkit渲染引擎的嵌入式接口：CEF和Android WebView
+ web应用和web运行环境
  + web应用分为：Packaged Application（应用包含了自身所需要的所有资源，不需要网络就能运行）和Hosted Application（除了Packaged Application）
  + web运行环境：
    + 运行HTML5的能力
    + 对（离线）存储的要求
    + 将web资源文件打包的支持
    + 应用程序的运行模式：也就是生命周期方面的支持
    + 能够启动并运行web应用

#### 总结

使用HTML技术来编写网页或Web应用，了解其背后的工作原理是写出高效代码的有效捷径。Webkit只是浏览器内核的其中一种，对于它的学习不能包括其他主流浏览器，但也是很有借鉴意义。

很多书都在说如何的写出高效的代码，比如《高性能JavaSript》等，其实本质都是基于语言本身的特性和浏览器实现的机制，这本书扩展了我的视野和知识边界。

另外由于书出版的日期较久，很多内容都有了更新，不过重要的还是学习思想。