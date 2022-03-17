Web Worker让JS有了[多线程](https://so.csdn.net/so/search?q=多线程&spm=1001.2101.3001.7020)的能力，可以将复杂耗时的操作都交付给Worker线程处理。WebSocket让web端与服务端维持一个有效的长连接，实现服务端主动推送数据。将二者一结合，业务系统信息流转通知功能完全就可以剥离出来。

Worker在当前架构中实现一个桥梁的左右，上连接[socket](https://so.csdn.net/so/search?q=socket&spm=1001.2101.3001.7020)端中的数据，下负责分发socket中的数据。此处我们先了解下Worker本身的功能实现。

1. 主线程与Worker线程通过方法`postMessage`相互传递信息
2. 主线程与Worker线程通过事件`onmessage`接收相互传递的消息
3. Worker中引入第三方js使用方法`importScripts([url,])`
4. 主线程调用`worker.terminate()`结束线程
5. Worker线程通过调用`this.close()`结束自身线程

WebSocket和Http一样都是基于Tcp协议。不同是WebSocket实现了服务端与客户端的全双工通讯。在Websocket未出现之前，要是实现一个信息推送的功能，通过http来实现唯一方案就是轮训，轮训分长短，各有弊端。现在WebSocket一出现，一切都好办了。