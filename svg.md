### **SVG**笔记

#### 基本概念

##### 1. 图形系统

计算机中描述图形信息的两大图形系统：栅格图形和矢量图形。栅格图形中图形被表示为图片元素或者像素的长方形数组。矢量图形中图形被描述为一系列几何形状，通过矢量图形阅读器在指定的坐标集上绘制形状。

##### 2. SVG(Scalable Vector Graphics)

SVG是一种XML应用，用来表示矢量图形。所有的图形有关信息被存储为纯文本，具有XML的开放性、可移植性和可交互性。

SVG文档结构是标准的XML文档，根元素svg定义图形的大小，根元素中包含各种的形状元素。SVG允许使用单独的属性指定元素的样式。

SVG使用g元素对图形进行分组，使用use元素实现元素的复用。

##### 3.SVG 的优势

- SVG 可被非常多的工具读取和修改（比如记事本）
- SVG 与 JPEG 和 GIF 图像比起来，尺寸更小，且可压缩性更强。
- SVG 是可伸缩的
- SVG 图像可在任何的分辨率下被高质量地打印
- SVG 可在图像质量不下降的情况下被放大
- SVG 图像中的文本是可选的，同时也是可搜索的（很适合制作地图）
- SVG 可以与 Java 技术一起运行
- SVG 是开放的标准
- SVG 文件是纯粹的 XML

#### HTML 页面中的 SVG

##### 1. 将SVG作为图像

将svg作为图像包含在HTML标记的img元素内，但是这样有一定的局限性：**SVG转为栅格图像时与主页面分离，并且无法在两者之间通信(SVG渲染过程与主页面独立)。主页面上的样式对SVG无效，运行在主页面上的脚本无法感知或者修改SVG文档结构。**

在CSS中包含SVG，最常用的是background-image属性，应该避免SVG元素文件太大。

##### 2. 将SVG作为应用程序

使用object元素将SVG嵌入HTML文档中，object元素的type属性表示要嵌入的文档类型，对用SVG应该是type="image/svg+xml"。object元素必须有起始标签和结束标签，这两个标签之间的内容为对象数据本身不能被渲染时显示。

当在 HTML 页面中嵌入 SVG 时使用 <embed> 标签是 Adobe SVG Viewer 推荐的方法！然而，如果需要创建合法的 XHTML，就不能使用 <embed>。任何 HTML 规范中都没有 <embed> 标签。

使用<iframe>标签

**HTML5支持内联svg（推荐）**

```html
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" height="190">
  <polygon points="100,10 40,180 190,60 10,60 160,180"
  style="fill:lime;stroke:purple;stroke-width:5;fill-rule:evenodd;" />
</svg>
```

#### 坐标系统

##### 1. 视口

视口是指文档打算使用的画布区域。在svg元素上使用width和height属性确定视口的大小，属性值可以仅仅是为数字也可以为带单位的数字(单位可以为em、ex、px、pt、pc、cm、mm和in)也可以为百分比。

##### 2. 默认用户坐标

SVG阅读器会设置一个坐标系统，即原点(0,0)位于视口的左上角，x向右递增，y向下递增。这个坐标系统是一个纯粹的几何系统，点没有大小，网格线被认为是无限细。

在SVG中指定单位并不会影响其他元素中给定单位的坐标，也就是说SVG文档中各个元素的单位可以不统一。

##### 3. 指定用户坐标

摒弃阅读器设置的默认用户坐标，可以自己为视口设置一个用户坐标。通过在svg元素上设置viewBox属性。

viewBox属性由4个数值组成，分别代表要叠加在视口上的最小x、最小y，宽度、高度。

既然可以对svg自定义用户坐标，那么肯定要解决SVG视口长宽比例和viewBox定义的长宽比例不同的问题以及如何对齐问题。这个时候就需要preserveAspectRatio属性了。

如果viewBox的长宽比例与视口的长宽比例不同，那么SVG可以有以下三种选择：

a. 按较小的尺寸等比例缩放图形，使图形完全填充视口

b. 按较大的尺寸等比例缩放图形，并裁减掉超出视口的部分

c. 拉伸和压缩绘图以使其恰好填充视口

默认值为"xMidYMid meet"

·***alignment***指定轴和位置，x和y方向都有min,mid,max三种方式，分别表示x和y方向的对齐方式，对齐方式由x和y组合指定，共9中方式，也就是alignment共有如下9个取值：

| y\x      | xMin     | xMid     | xMax     |
| -------- | -------- | -------- | -------- |
| **yMin** | xMinYMin | xMidYMin | xMaxYMin |
| **yMid** | xMinYMid | xMidYMid | xMaxYMid |
| **yMax** | xMinYMax | xMidYMax | xMaxYMax |

·***meet***说明符在图形超出视口时候会对图形适当缩小调整适配可用的空间

·***slice***说明符直接裁剪超出视口的部分

除了上述操作之外，还可以指定**preserveAspectRatio="none"**，用于在viewBox和视口宽高比不同时缩放图像，此时图像不会被等比例缩放，会被拉伸、挤压、变形。

##### 4. 嵌套坐标系统

可以将另一个svg元素插入到文档中来建立一个新的视口和坐标系统，也就是说svg中可以嵌套另一个svg，每个svg都有自己独立的视口和坐标系统。

#### 坐标系统变换

##### 1. translate变换

translate变换用来对用户坐标进行平移，通过制定transform属性值来设置:transform = "translate(x,y)"。

translate工作原理:首先获取整个网络，然后将其移动到画布的新位置而不是移动所在的元素，也就是说**移动的是整个坐标系统而不是元素本身**。看似比移动元素复杂，其实在使用其他一系列变换时，这种移动整个坐标系的方法从数学和概念上讲，更方便。

##### 2. scale变换

缩放坐标系统。transform = "scale(value)"或者transform="scale(x-value,y-value)"。

仅仅使用scale(n)变换时，网格系统的原点位置并没有变化，只是每个用户坐标都变成了原来的n倍，也就是网格变大了，因此线也会变粗(用户单位并没有变)。

*技巧：如果从其他系统传输数据到SVG，则可能必须处理使用笛卡尔坐标表示的矢量图形，在笛卡尔坐标系统中，原点位于左下角，y向上递增，x向右递增。而SVG坐标原点位于左上角，此时使用scale(1,-1)就可以完成两者之间的转换。*

**缩放变换永远不会改变图形对象的网格坐标或者笔画宽度，仅仅改变对应画布上的坐标系统网格的大小。**

##### 3. rotate变换

根据指定的角度旋转坐标系统，默认的坐标系统中，角度的测量顺时针增加，0度为3点钟方向。

注意，除非另行指定，否则旋转以原点为中心。 此时可以通过平移+旋转的方式来指定旋转中心： translate(centerX,centerY) rotate(angle) translate(-centerX,-centerY)

但是有个更简单的方式：rotate(angle,centerX,centerY)

##### 4.围绕中心点缩放

上面提到，缩放默认是以原点为基准的，这显然不能满足需求，那么可以通过如下方式指定缩放中心：

translate(-centerX*(factor-1),-centerY*(factor-1)) scale(factor)

##### 5.skewX和skewY变换

这两个变换用来倾斜某个轴，一般形式为skewX(angle),skewY(angle)。这样的结果就是使得x轴和y轴不再垂直。

##### 6.矩阵变换

计算机图形学中坐标变换都通过矩阵来实现，除上述变换方法之外，还可以直接为变换指定变换矩阵，变换矩阵为matrix(a,b,c,d,e,f)，此时指定的变换矩阵为:

```text
a  c  e
b  d  f
0  0  1
```

#### 文档结构

##### 1. 结构和表现

SVG允许文档表现和文档结构分离，SVG支持四种方式指定表现信息：内联样式、内部样式表、外部样式表以及表现属性

| 表现方式   | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| 内联样式   | 元素内部使用style属性                                        |
| 内部样式表 | 内部样式定义在defs元素内部                                   |
| 外部样式表 | 与html类似，将样式定义在css文件中，使用选择器来设置相应的元素样式 |
| 表现属性   | SVG允许以属性的形式指定表现样式，但是**表现属性的优先级最低**，如果以其他三种形式指定了相同的样式属性，则将覆盖通过表现属性指定的样式 |

```text
<svg width="200px" height="200px" xmlns="http://www.w3.org/2000/svg>
    <defs>
        <style type="text/css"><![CDATA[
            circle{
                fill:#ccc
            }
        ]]></style>
    </defs>
    <circle cx="10" cy="10" r="5"/>
</svg>
```

#####  2. 分组和引用

**g元素**用来将其子元素作为一个组合，可以使文档结构更清晰。除此之外，在g标签中指定的所有样式会应用于组合内的所有子元素，可以不用在所有子元素上指定属性。

**use元素**用来复用图形中重复出现的元素，需要为use标签的xlink:href指定URI来引用指定的图形元素。同时还要指定x和y属性以表示组合应该移动到哪个位置。use元素并不限制只能使用同一个文件内的对象，xlink:href属性可以指定任何有效的文件或URI。

**defs元素**用来定义复用的元素，但是定义在defs内的元素并不会被显示，而是作为模板供其他地方使用。

**symbol元素**与g元素不同，symbol永远不会被显示，也可以用来指定被后续使用的元素，symbol元素可以指定viewBox和preserveAspectRatio属性。在引用时通过为use元素指定width和height属性就可以让symbol元素适配视口大小。

**image**可以用来包含一个完整的SVG或栅格文件。如果包含一个SVG文件，则视口会基于引用的文件的x,y,width,height属性来建立。如果包含栅格文件则会被缩放以适配该属性指定的矩形。SVG规范要求SVG阅读器支持JPEG和PNG两种栅格文件。

####  基本形状

SVG 有一些预定义的形状元素，可被开发者使用和操作：

##### 1.矩形

**<rect> 标签，使用x,y,width,height表示一个矩形**

- x 属性定义矩形的左侧位置（例如，x="0" 定义矩形到浏览器窗口左侧的距离是 0px）
- y 属性定义矩形的顶端位置（例如，y="0" 定义矩形到浏览器窗口顶端的距离是 0px）
- rect 元素的 width 和 height 属性可定义矩形的高度和宽度

| 特性         | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| fill         | 填充颜色                                                     |
| fill-opacity | 填充不透明度                                                 |
| stroke       | 边框颜色                                                     |
| stroke-width | 边框宽度，边框是骑在矩形边界上的，一半在矩形外，一半在矩形内 |
| rx/ry        | 圆角矩形，最大值为矩形宽/高的一半，如果只指定了一个，则认为两个都为相同的值 |

##### 2.圆形

**<circle> 标签可用来创建一个圆。**

+ cx 和 cy 属性定义圆点的 x 和 y 坐标。如果省略 cx 和 cy，圆的中心会被设置为 (0, 0)。
+ r 属性定义圆的半径。

##### 3.椭圆

**<ellipse> 标签可用来创建椭圆。椭圆与圆很相似。不同之处在于椭圆有不同的 x 和 y 半径，而圆的 x 和 y 半径是相同的。**

- cx 属性定义圆点的 x 坐标
- cy 属性定义圆点的 y 坐标
- rx 属性定义水平半径
- ry 属性定义垂直半径

| 特性         | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| fill         | 填充颜色                                                     |
| fill-opacity | 填充不透明度                                                 |
| stroke       | 边框颜色                                                     |
| stroke-width | 边框宽度，边框是骑在圆的边界上的，一半在圆/椭圆外，一半在圆/椭圆内 |

##### 4.线

**<line> 标签用来创建线条。**

- x1 属性在 x 轴定义线条的开始
- y1 属性在 y 轴定义线条的开始
- x2 属性在 x 轴定义线条的结束
- y2 属性在 y 轴定义线条的结束

| 特性             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| stroke-width     | 笔画宽度，坐标网格线位于笔画的正中间，可以使用css的shape-rendering值来控制反锯齿特性 |
| stroke           | 笔画颜色                                                     |
| stroke-opacity   | 线条的不透明度                                               |
| stroke-dasharray | 虚线，由一系列数字组成，数字个数为偶数(负责会自动重复一遍使其为偶数),表示线长-间隙-线长-间隙... |

##### 5.折线

**<polyline> 标签用来创建仅包含直线的形状。**

+ 使用points属性指定一系列点，不自动封闭图形

##### 6.多边形

**<polygon> 标签用来创建含有不少于三个边的图形。**

+ 由points属性指定的一系列坐标点界定，会自动封闭

| 特性         | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| fill         | 填充颜色                                                     |
| fill-opacity | 填充不透明度                                                 |
| stroke       | 边框颜色                                                     |
| stroke-width | 边框宽度                                                     |
| fill-rule    | 填充规则，如果多边形的边有交叉时，需要指定，可以取nozero(默认)和evenodd两个值。 |

fill-rule值为nonzero时的原理:判断一个点是在多边形内部还是外部时，从这个点画一条到无穷远的射线，然后数这个线和多边形的边有多少次交叉。如果交叉的边线是从右往左画，则总数加1，如果是从左往右则总数减1.如果最后总数为0则认为改点在图形外部，否则在内部。

fill-rule值为evenodd时只数射线与多边形边的交叉次数，如果为奇数则认为在多边形内部，否则认为在多边形外部。

##### 7.路径

**<path> 标签用来定义路径。**可以通过制定一系列相互连接的线、弧、曲线来绘制任意形状的轮廓，这些轮廓也可以填充或者绘制轮廓线，也可以用来定义裁剪区域或蒙版。

| 命令 | 参数                                      | 说明                                                         |
| ---- | ----------------------------------------- | ------------------------------------------------------------ |
| M m  | x y                                       | 移动画笔到制定坐标（**moveto**）                             |
| L l  | x y                                       | 绘制一条到给定坐标的线（**lineto**）                         |
| H h  | x                                         | 绘制一条到给定x坐标的横线（**horizontal lineto**）           |
| V v  | y                                         | 绘制一条到给定y坐标的垂线（**vertical lineto**）             |
| A a  | rx ry x-axis-rotation large-arc sweep x y | 圆弧曲线命令有7个参数，依次表示x方向半径、y方向半径、旋转角度、大圆标识、顺逆时针标识、目标点x、目标点y。大圆标识和顺逆时针以0和1表示。0表示小圆、逆时针（**elliptical Arc**） |
| Q q  | x1 y1 x y                                 | 绘制一条从当前点到x,y控制点为x1,y1的二次贝塞尔曲线（**quadratic Belzier curve**） |
| T t  | x y                                       | 绘制一条从当前点到x,y的光滑二次贝塞尔曲线，控制点为前一个Q命令的控制点的中心对称点，如果没有前一条则已当前点为控制点。（**smooth quadratic Belzier curveto**） |
| C c  | x1 y1 x2 y2 x y                           | 绘制一条从当前点到x,y控制点为x1,y1 x2,y2的三次贝塞尔曲线（**curveto**） |
| S s  | x2 y2 x y                                 | 绘制一条从当前点到x,y的光滑三次贝塞尔曲线。第一个控制点为前一个C命令的第二个控制点的中心对称点，如果没有前一条曲线，则第一个控制点为当前的点。（**smooth curveto**） |
| Z z  |                                           | (**closepath**)                                              |

**注释：**以上所有命令均允许小写字母。大写表示绝对定位，小写表示相对定位。

##### 8.marker元素

**marker元素用来在path上添加一个标记，比如箭头之类的**。

+ 首先需要定义好marker元素，然后在path中引用，一个marker标记是一个独立的图形，有自己的私有坐标。

```html
<!---html-->
<defs>
    <marker id="marker" markerWidth="10" markerHeight="10" refX="0" refY="4" orient="auto">
        <path d="M 0 0 4 4 0 8" style="fill:none;stroke:black;"/>
    </marker>
</defs>

<path d="M 10 20 100 20 A 20 30 0 0 1 120 50 L 120 110"
    style="marker-start:url(#marker);marker-mid:url(#marker);marker-end:url(#marker);fill:none;stroke:black;"/>
```

```css
/***css***/
path{
    marker:url(#marker_id);
}
```

| marker属性                  | 说明                                                         |
| --------------------------- | ------------------------------------------------------------ |
| markerWidth                 | marker标记的宽度                                             |
| markerHeight                | marker标记的高度                                             |
| refX refY                   | 指定marker中的哪个坐标与路径的开始坐标对齐                   |
| orient                      | 自动旋转匹配路径的方向，需要设置为auto                       |
| markerUnits                 | 这个属性决定标记的坐标系统是否需要根据path的笔画宽度调整，如果设置为strokeWidth，则标记会自动调整大小。如果设置为useSpaceOnUse，则不会自动调整标记的大小。 |
| viewBox preserveAspectRatio | 设置标记的显示效果，比如可以将标记的(0,0)设置在标记网格中心  |

**注释：**如果id为marker_id的标记中也有path元素，则会出现自身无限引用自身的情况，因此需要说明marker中的path元素不需要添加标记

#### 图案和渐变

##### 1.图案

使用图案填充图形，首先要定义一个水平或垂直方向的重复的图案对象，然后用它填充另一个对象或者作为笔画使用。这个图形对象被称为"tile"(瓷砖)。

图案对象使用pattern元素定义，pattern元素内部包裹了图案的path元素。定义好之后下一个需要解决的问题是如何排列图案，那就需要使用patternUnits属性.

+ patternUnits = objectBoundingBox

  如果希望图案的大小基于要填充对象的大小计算，则需要设置patternUnits属性为objectBoundingBox(0到1之间的小数或百分比)，并需要指定图案左上角的x和y坐标。

+ patternUnits = userSpaceOnUse

  按用户单位制定图案的width和height

+ patternContentUnits属性默认为userSpaceOnUse,当设置patternContentUnits属性为objectBoundingBox时就可以使用百分比来设置图案的大小。

##### 2.渐变

**SVG 渐变必须在 <defs> 标签中进行定义。**渐变是一种从一种颜色到另一种颜色的平滑过渡。另外，可以把多个颜色的过渡应用到同一个元素上。

+ 线性渐变：<linearGradient> 标签，必须嵌套在 <defs> 的内部

  线性渐变是一系列颜色沿着一条直线过渡，在特定的位置指定想要的颜色，被称为渐变点。渐变点是渐变结构的一部分，颜色是表现的一部分。

  **stop元素的属性：**

  | 属性         | 说明                         |
  | ------------ | ---------------------------- |
  | offset       | 必需，取值范围0%-100%        |
  | stop-color   | 必需，对应offset位置点的颜色 |
  | stop-opacity | 对应offset位置点的不透明度   |

  **linearGradient元素属性：**

  | 属性         | 说明                                                         |
  | ------------ | ------------------------------------------------------------ |
  | x1,y1        | 渐变的起点位置，使用百分比表示，默认的渐变方向是从左到右     |
  | x2,y2        | 渐变的终点位置，使用百分比表示                               |
  | spreadMethod | 如果设置的offset不能覆盖整个对象，该怎么填充。pad:起点或终点颜色会扩展到对象边缘。repeat:渐变重复起点到终点的过程。reflect:渐变按终点-起点-终点的排列重复。 |

  - 当 y1 和 y2 相等，而 x1 和 x2 不同时，可创建水平渐变
  - 当 x1 和 x2 相等，而 y1 和 y2 不同时，可创建垂直渐变
  - 当 x1 和 x2 不同，且 y1 和 y2 不同时，可创建角形渐变

  ``` text
  <defs>
  	<linearGradient id="linear">
  		<stop offset="0%" style="stop-color:#ffcc00;"></stop>
  		<stop offset="100%" style="stop-color:#0099cc;"></stop>
  	</linearGradient>
  </defs>
  	<rect x="20" y="20" width="200" height="100" style="fill:url(#linear);stroke:black;"></rect>
  ```

+ 放射渐变：<radialGradient> 标签，必须嵌套在 <defs> 的内部

  径向渐变的每个渐变点是一个圆形路径，从中心点向外扩散。设置方式与线性渐变大致相同。如果填充对象边界框不是正方形的，则过渡路径会变成椭圆来匹配边界框的长宽比。

  radialGradient元素属性：

  | 属性         | 说明                                                         |
  | ------------ | ------------------------------------------------------------ |
  | cx,cy,r      | 定义渐变的范围，测量半径的单位是对象的宽高均值，而不是对角线，默认都为50% |
  | fx,fy        | 0%点所处的圆路径的圆心，默认和cx,cy一样                      |
  | spreadMethod | pad,repeat,reflect三个值，用来解决绘制范围没有到达图形边缘的情况。 |

#### 文本

##### 1. 相关术语

| 术语                | 说明                                                         |
| ------------------- | ------------------------------------------------------------ |
| 字符                | XML中，字符是指带有一个数字值得一个或多个字节，数字值与Unidode标准对应 |
| 符号                | 字符的视觉呈现。每个字符可以有多种视觉呈现                   |
| 字体                | 代表某个字符集合的一组符号                                   |
| 基线                | 字体中所有符号以基线对齐                                     |
| 上坡度              | 基线到字体中最高字符的顶部距离                               |
| 下坡度              | 基线到最深字符底部的距离                                     |
| 大写字母高度、x高度 | 大写字母高度是指基线上大写字母的高度，x高度是基线到小写字母x顶部的高度 |

##### 2. text元素的基本属性

text元素以指定的x和y值作为元素内容第一个字符的基线位置，默认样式黑色填充、没有轮廓。

| 属性            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| font-family     | 以空格分割的一系列字体名称或通用字体名称                     |
| font-size       | 如果有多行文本，则font-size为平行的两条基线的距离            |
| font-weight     | 两个值：bold(粗体)和nromal(默认)                             |
| font-style      | 常用的两个值:italic(斜体)和normal                            |
| text-decoration | 可能的值:none,underline(下划线),overline(上划线),line-through(删除线) |
| word-spacing    | 单词之间的距离                                               |
| letter-spacing  | 字母之间的间距                                               |
| text-anchor     | 对齐方式：start,middle,end                                   |
| textLength      | 设置文本的长度                                               |
| lengthAdjust    | 在指定了textLength时，可以通过lengthAdjust属性设置字符的调整方式，值为 spacing(默认)时,只调整字符的间距。当值为spacingAndGlyphs时，同时调整字符间距和字符本身的大小 |

##### 3. tspan元素

text元素无法对文本进行换行操作，如果需要分行显示文本，则需要使用tspan元素。tspan元素与html的span元素类似，可以嵌套在文本内容中，并可以单独改变其内部文本内容的样式。

tspan元素除大小，颜色等表现样式之外，还可以设置以下属性：

| 属性           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| dx,dy          | x和y方向的偏移                                               |
| x,y            | 对tspan进行绝对定位                                          |
| rotate         | 旋转字符，可以同时设置多个值，这些值会依次作用在tspan包裹的字母上 |
| baseline-shift | 与dy属性设置上下标相比，这个属性更方便，当为super时，会上标。sub时为下标。仅仅在所在的tspan内有效 |

##### 4. 纵向文本

文本一般从左到右排列，如果需要上下排列，则需要使用**writing-mode属性**。

设置writing-mode属性值为tb(top to bottom)，可以将文本上下排列。

##### 5. 文本路径

如果要使得文本沿着某条路径排列，则需要使用**textPath元素。**需要将文本放在textPath元素内部，然后使用textPath元素的xlink:href属性引用一个定义好的path元素。

```text
<defs>
	<path id="path" d="M30 40 C 50 10 ,70 10,120 40 S150 0,200 40" style="fill:none;stroke:black"></path>
</defs>
<g transform="translate(10,50)">
	<path id="path" d="M30 40 C 50 10 ,70 10,120 40 S150 0,200 40" style="fill:none;stroke:black"></path>
	<text>
		<textPath xlink:href="#path">
			hello world
		</textPath>
	</text>
</g>
<g transform="translate(10,100)">
	<path id="path" d="M30 40 C 50 10 ,70 10,120 40 S150 0,200 40" style="fill:none;stroke:black"></path>
	<text>
		<textPath xlink:href="#path" startOffset="50%" text-anchor="middle">
			hello world
		</textPath>
	</text>
</g>
```

**startOffset属性**用来指定文本的起点，当设置为50%，并且设置text-anchor为middle时，文本会被定为在path的中间。

#### 滤镜

**SVG 滤镜用来向形状和文本添加特殊的效果。**

在 SVG 中，可用的滤镜有：

- feBlend
- feColorMatrix
- feComponentTransfer
- feComposite
- feConvolveMatrix
- feDiffuseLighting
- feDisplacementMap
- feFlood
- feGaussianBlur
- feImage
- feMerge
- feMorphology
- feOffset
- feSpecularLighting
- feTile
- feTurbulence
- feDistantLight
- fePointLight
- feSpotLight

##### 1. 滤镜工作原理

SVG阅读器处理一个图形对象时，会将对象呈现在位图输出设备上，它可以将对象的描述信息转化为一组对应的像素。在使用滤镜时，SVG阅读器不会直接将图形渲染为最终结果，而是先将像素保存到临时位图中，然后将滤镜指定的操作应用到该临时位图，其结果作为最终图形。

在SVG中，使用**filter元素**指定一组操作(也叫基元),在渲染图形对象时，将该操作应用在最终图形上。

filter标记之间就是我们想要的滤镜基元，每个基元有一个或多个输入，但是只有一个输出，输入可以是原始图形(SourceGraphic)、图形的阿尔法通道(不透明度，SourceAlpha)或者是前一个滤镜基元的输出。

##### 2. 创建投影效果

filter元素有一些属性用来描述该滤镜的裁剪区域。通过x,y,width,height属性定义一个滤镜范围，这些属性默认情况是按照对象的边界框计算的，即filterUnits属性的默认值为objectBoundingBox,如果要按照用户单位制定边界，则需要设置该属性值为userSpaceOnUse。

还可以用primitiveUnits属性为基元操作指定单位，默认值为userSpaceOnUse,如果设置为objectBoundingBox则会按照图形尺寸的百分比来表示单位。

- <filter> 标签的 id 属性可为滤镜定义一个唯一的名称（同一滤镜可被文档中的多个元素使用）
- filter:url 属性用来把元素链接到滤镜。当链接滤镜 id 时，必须使用 # 字符
- 滤镜效果是通过 <feGaussianBlur> 标签进行定义的。fe 后缀可用于所有的滤镜
- <feGaussianBlur> 标签的 stdDeviation 属性可定义模糊的程度
- in="SourceGraphic" 这个部分定义了由整个图像创建效果

```text
<defs>
	<filter id="gaussian" x="0" y="0">
		<feGaussianBlur in="SourceGraphic" stdDeviation="2"></feGaussianBlur>
	</filter>
</defs>
<g transform="translate(10,10)">
	<rect x="10" y="10" width="100" height="100" fill="#ccc" filter="url(#gaussian)"></rect>
</g>
<g>
	<rect x="10" y="10" width="100" height="100" fill="black"></rect>
</g>
```

#### 剪裁和蒙版

##### 1. 裁剪路径

在创建SVG文档时，可以通过指定感兴趣的区域的宽度和高度建立视口，这个视口就会变成默认的裁剪区域，裁剪区域外的任何部分都不会被显示。裁剪区域可以通过**clipPath元素**建立自己的裁剪区域。

```text
<defs>
	<clipPath id="rectClip">
		<rect x="100" y="100" width="100" height="90" fill="none" stroke="black"></rect>
		<circle cx="300" cy="150" r="60" fill="none"></circle>
		<path d="M100 50L150,50L100,20L40,60Z" fill="none"></path>
	</clipPath>
</defs>
<image x="0" y="0" width="480" height="270" xlink:href="./10.0.jpg" style="clip-path:url(#rectClip);"></image>
<image x="0" y="0" width="480" height="270" xlink:href="./10.0.jpg" opacity="0.2"></image>
```

裁剪路径也可以指定坐标系，在上面的示例中使用的是用户坐标系，也就是裁剪路径中的坐标值都是基于原点的。也可以根据对象的边界来指定，需要设置clipPathUnits属性为objectBoundingBox(默认值为userSpaceOnUse)。

##### 2. 蒙版

SVG的蒙版会变换对象的透明度，如果蒙版是不透明的，则被蒙版覆盖的对象的像素就是不透明的，如果蒙版是半透明的，则对象就是半透明的。

使用**mask元素**创建蒙版，使用x,y,width,height指定蒙版的尺寸，这些尺寸默认按照objectBoungdingBox计算，如果想根据用户空间坐标计算，则需要设置mask元素的maskUnits值为userSpaceOnUse。

mask之间是想要用作蒙版的任意基本形状、文本图像或路径。这些元素默认坐标使用用户坐标空间表达，如果想要这些元素使用对象的边界框，则设置maskContentUnits属性为objectBoungdingBox即可。

注意与maskUnits属性的区别，maskUnits针对mask元素，maskContentUnits属性针对mask元素内的元素。

SVG需要确定蒙版的透明度，每个像素由4个值描述：R,G,B,透明度，使用如下公式计算：

(0.2125*r + 0.7154*g + 0.0721*b)* opacity

系数不同，是因为完全饱和情况下，红绿蓝的亮度不同。

```text
<defs>
	<mask id="mask" x="0" y="0" width="1" height="1" maskContentUnits="objectBoundingBox">
		<circle cx=".500" cy=".50" r=".30" fill="red"></circle>
	</mask>
</defs>
<rect x="0" y="0" width="100" height="100" style="mask:url(#mask)"></rect>
<rect x="0" y="0" width="100" height="100" fill="none" stroke="black"></rect>
```

#### SVG动画

##### 1. 动画基础

SVG动画特性基于"同步多媒体集成语言"(SMIL)规范。在这个动画系统中，可以指定想要进行的动画的属性(颜色、动作或者变形等)的起始值和初始值，以及动画开始的时间和持续时间。

##### 2. 动画时间与同步动画

##### 3. 多边形和path动画

##### 4. 对坐标变换进行过渡

##### 5. 沿着path运动

##### 6. CSS处理SVG动画

#### HTML 5 Canvas vs. SVG

**Canvas 和 SVG 都允许您在浏览器中创建图形，但是它们在根本上是不同的。**

Canvas通过 JavaScript 来绘制 2D 图形。Canvas 是逐像素进行渲染的。

在 canvas 中，一旦图形被绘制完成，它就不会继续得到浏览器的关注。如果其位置发生变化，那么整个场景也需要重新绘制，包括任何或许已被图形覆盖的对象。

- 依赖分辨率
- 不支持事件处理器
- 弱的文本渲染能力
- 能够以 .png 或 .jpg 格式保存结果图像
- 最适合图像密集型的游戏，其中的许多对象会被频繁重绘

SVG 是一种使用 XML 描述 2D 图形的语言。

SVG 基于 XML，这意味着 SVG DOM 中的每个元素都是可用的。您可以为某个元素附加 JavaScript 事件处理器。

在 SVG 中，每个被绘制的图形均被视为对象。如果 SVG 对象的属性发生变化，那么浏览器能够自动重现图形。

- 不依赖分辨率
- 支持事件处理器
- 最适合带有大型渲染区域的应用程序（比如谷歌地图）
- 复杂度高会减慢渲染速度（任何过度使用 DOM 的应用都不快）
- 不适合游戏应用



https://www.w3school.com.cn/svg/index.asp

https://www.d3js.org.cn/svg/get_start/
