#### WebRTC笔记

+ **简介**

  网页即时通信（Web Real-Time Communication）是一个支持网页浏览器进行实时语音对话或视频对话的API。目的主要是让Web开发者能够基于浏览器（Chrome\FireFox\...）轻易快捷开发出丰富的实时多媒体应用，而无需下载安装任何插件；Web开发者也无需关注多媒体的数字信号处理过程，只需编写简单的Javascript程序即可实现。

  WebRTC提供了视频会议的核心技术，包括音视频的采集、编解码、网络传输、显示等功能，并且还支持跨平台：windows，linux，mac，android。

  不能简单地将 WebRTC 与 RTC 划等号。

+ **应用场景**

  视频成了娱乐、学习、商务会议、社交、电商的载体，人们逐渐不再有耐心阅读文字性的信息。视频不仅是信息的展现方式，从单向的“录制 上传 下载 找播放器打开 播放”，变成了“现场录制 边录边播 实时收看”，再变成视频与即时通讯工具、会议工具融合的双向“录制与播放”。实时视频的目标，是把正在某个地方A发生的人和事，以几乎零延迟、不失真的方式“同步”到另外一个地方 B，让 B 的人瞬间看到、听到，并且反之亦然。

  Cloud Gaming，就是你不需要本地的光盘了，游戏在云端运行，然后通过流媒体的方式传输到你的屏幕上，就像你在电视上点播电影一样，但你用游戏手柄可以与“电影”互动。

  元宇宙，是一个“仿真”或者说“全真”的互联网，它的特点之一，是利用极其强大的实时网络，把物理世界里事物的无限细节信息化并瞬间传播给接收者，使其通过一些特殊设备去复原这些信息并最大程度感受到在原发地事物的原本样子。

+ **项目开发**

  在项目中简单实现了一下实时显示录像视频，只应用到了接受流。主要使用了**webrtc-adapter.js**。

  ```vue
  import adapter from 'webrtc-adapter'
  Vue.prototype.adapter = adapter
  ```

  ```js
  async function handleNegotiationNeededEvent(event) {
          var localePc = event.target;
          const offer = await localePc.createOffer();
          await localePc.setLocalDescription(offer);
          _this.getRemoteSdp(localePc, equiUuid);
        }
  
        const privatePc = new RTCPeerConnection(config);
        privatePc.onnegotiationneeded = handleNegotiationNeededEvent;
        const privatestream = new MediaStream();
        privatePc.ontrack = function(event) {
          privatestream.addTrack(event.track);
          privateVideoElem.srcObject = privatestream;
        };
        privatePc.addTransceiver("video", {
          direction: "sendrecv"
        });
        privatePc.addTransceiver("video", {
          direction: "sendrecv"
        });
  
  getRemoteSdp(localePc, uuid) {
        const formData = new FormData();
        formData.append("suuid", uuid);
        formData.append("data", window.btoa(localePc.localDescription.sdp));
        getWebRtc(uuid, formData)
          .then(res => {
            localePc.setRemoteDescription(
              new RTCSessionDescription({
                type: "answer",
                sdp: window.atob(res)
              })
            );
          })
          .catch(e => {
            console.warn(e);
          });
      }
  ```

+ **补充**

  WebRTC 成为下一代互联网的实时应用基石，估计有点悬，因为确实有潜在的更优解在那里。**但是，对于应用开发者，未来几年内，WebRTC可能就是我们的最优解。**

+ **参考**

  1.https://baijiahao.baidu.com/s?id=1714740880954778889&wfr=spider&for=pc

  2.https://baike.baidu.com/item/WebRTC/5522744?fr=aladdin