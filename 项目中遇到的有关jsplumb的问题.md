### 项目中遇到的有关jsplumb的问题

#### 前言

本文提到的是一个基于vue框架的web绘制流程图的项目，在我接手之前已经有过一版并发布，而这次的需求只是在原先基础上添加放大缩小的功能，所以在重构和修修补补之中选择了后者，然后就遇到了各种坑，也才有了这篇笔记。

#### 正文

先总结一下遇到的问题：

1.项目结构混乱，整体框架虽然是vue但是却包含了大量jQuery和原生js的语法且缺少文档和注释

2.项目本身存在bug，需要修复

3.jsplumb分为免费版和付费版，这两者差别很大，导致官方文档参考价值大大降低

解决过程及方案：
1.对于问题一和问题二，没有别的方法只能死命磕别人写的源代码、尝试接受并理解别人的思路。

2.对于问题三的详细展开：

jsplumb官网 [https://jsplumbtoolkit.com/] 的例子和文档是基于Toolkit版本的，所以对于免费版主要是参考[https://docs.jsplumbtoolkit.com/community/]，文档中显示有一个setZoom()的方法可以实现缩放，但是我在项目中死活没有生效（希望有大神可以解惑）。最终只能自己造轮子，由于是全英文所以对我来说还是有点累，关于jsplumb的基本概念主要是参考了另外两篇博文jsPlumb笔记[https://blog.csdn.net/weixin_36401046/article/details/79756422]jsPlumb.jsAPI 心得 [https://www.jianshu.com/p/d9e9918fd928]。

实现的主要思路：通过transform：scale改变元素的大小，然后以最左边的元素作为参照点，通过改变元素left、top实现位移。改变样式以后重绘节点、端点、连线。

主要代码：

``` js
//dom:需要缩放的元素;type:放大 or 缩小;leftBasic:缩放的参照点的left;topBasic:缩放的参照点的top;links:连线
calcStyle(dom,type,leftBasic,topBasic,links){
    dom.each((idx,el)=>{
   	let left = $(el).css('left')
   	let top = $(el).css('top')
   	left = parseInt(left.substring(0,left.length-2))
   	top = parseInt(top.substring(0,top.length-2))
    let x = 0
   	let y = 0
   	let id = $(el).attr('id')
   	this.jsPlumb.removeAllEndpoints(id);
   	this.jsPlumb.unmakeSource(id)
   	this.jsPlumb.unmakeTarget(id)
   	if(left>leftBasic){
        if(type==='zoomOut'){
            x = (1-this.zoomNum) *(left - leftBasic)*(-1)/this.zoomNum
            y =(1-this.zoomNum)*(top-topBasic)*(-1)/this.zoomNum
        }else{
            x = (this.zoomNum-1) *(left - leftBasic)*this.zoomNum
            y =(this.zoomNum-1)*(top-topBasic)*this.zoomNum
        }
        $(el).css("left",left+x)
        $(el).css("top",top+y)
        $(el).css("transform","scale(" + this.zoomNum + ")");
    }else{
        $(el).css("transform","scale(" + this.zoomNum + ")");
    }
        this.jsPlumb.makeSource(el, {
            filter: ".point",
            anchor: "Continuous",
            connectionType: "basic"
          });

          this.jsPlumb.makeTarget(el, {
            dropOptions: { hoverClass: "dragHover" },
            anchor: "Continuous",
            allowLoopback: true
          });
      })

        for (var i = 0; i < links.length; i++) {
          this.jsPlumb.connect({
            source: links[i].SourceId,
            target: links[i].TargetId,
            type: "basic",
          });
        }

        this.jsPlumb.repaintEverything()
    }
```

此外还有几点注意和提示：

1.初始化节点的时候需要添加缩放的样式

2.我试过translate(*x*,*y*)的方法来修改位移，但是重新连线的时候鼠标位置和端点位置都会出现偏差，可能用revalidate()以后能解决但是没实践。

3.在拖放新元素然后缩放（没有连线的情况下），也会导致端点位置有偏差，后来看了下jsplumb有一个revalidate()的方法可以单独重绘某个节点解决了该问题。

4.当元素过大过多时，采用的是加入拖拽画布的功能，而不是出现滚动条，因为我的放大缩小是鼠标滚动事件，不过加入拖拽之后最好搭配minimap，否则绘画元素出框的情况会比较尴尬。（但是我没有实现minimap，以后有时间再研究）

#### 总结

对于jsplumb我现在也还是一知半解，实践是最好的老师，后续遇到有新的需求继续一边学习一边进步！
