## lib-flexible （Flexible.js）

1. 用法

   * js

     * 安装

       npm i -S amfe-flexible

     * 引入

       ```html
       <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no">
       <script src="./node_modules/amfe-flexible/index.js"></script>
       ```

   * vue

     * 安装lib-flexible并搭配px2rem-loader

       npm install lib-flexible --save-dev
       npm install px2rem-loader --save-dev

     * 引入

       在`main.js`中引入lib-flexible 

       ```js
       // px2rem 自适应
       import 'lib-flexible'
       ```

     * 配置（vue.config.js/vue-cli 3.x）

       ```js
       module.exports = {
           css: {
               loaderOptions: {
                   css: {},
                   postcss: {
                       plugins: [
                           require('postcss-px2rem')({
                               // 以设计稿750为例， 750 / 10 = 75
                               remUnit: 75
                           }),
                       ]
                   }
               }
           },
       };
       ```

   * react

     * 安装

       npm i lib-flexible --save

       npm i postcss-px2rem --save

     * 引入

       在`index.js`中引入lib-flexible 

       ```js
       import 'lib-flexible';
       ```

     * 配置webpack.config.js

       ```js
       {
           loader: require.resolve('postcss-loader'),
           options: {
           /* 省略代码... */
               ident: 'postcss',
               plugins: () => [
               	require('postcss-flexbugs-fixes'),
               	require('postcss-preset-env')({
               		autoprefixer: {
               			flexbox: 'no-2009',
               		},
               	stage: 3,
               }),
           	px2rem({remUnit: 75}), // 添加的内容
           /* 省略代码... */
           ],
           sourceMap: isEnvProduction && shouldUseSourceMap,
           },
       },
       ```

2. 原理

   在页面中引入flexible.js后，flexible会在<html>标签上增加一个data-dpr属性和font-size样式。js首先会获取设备型号，然后根据不同设备添加不同的data-dpr值，比如说1、2或者3，从源码中我们可以看到。

   ```jsx
   if (!dpr && !scale) {
       var isAndroid = win.navigator.appVersion.match(/android/gi);
       var isIPhone = win.navigator.appVersion.match(/iphone/gi);
       var devicePixelRatio = win.devicePixelRatio;
       if (isIPhone) {
           // iOS下，对于2和3的屏，用2倍的方案，其余的用1倍方案
           if (devicePixelRatio >= 3 && (!dpr || dpr >= 3)) {
               dpr = 3;
           } else if (devicePixelRatio >= 2 && (!dpr || dpr >= 2)) {
               dpr = 2;
           } else {
               dpr = 1;
           }
       } else {
           // 其他设备下，仍旧使用1倍的方案
           dpr = 1;
       }
       scale = 1 / dpr;
   }
   ```

   页面中的元素用rem单位来设置，rem就是相对于根元素<html>的font-size来计算的，flexible.js能根据<html>的font-size计算出元素的盒模型大小。这样就意味着我们只需要在根元素确定一个px字号，因此来算出各元素的宽高，从而实现屏幕的适配效果。

   把视觉稿中的px转换成rem。以视觉稿为640px的宽来举例子，把640px分为100份，每一份称为一个单位a，那么每个a就是6.4px，而1rem单位被认定为10a，此时，1rem=1(a)X10X6.4(px)即64px。

3. 优缺点

   * 优点

     * 开源
     * 可以在各类项目中引入和引用
     * 终端设备适配的解决方案，即实现在不同终端设备中的页面适配

   * 缺点

     * 由于单位换算成rem，不适合文本（字体仍然建议使用px，表单）

       ```css
       [data-dpr="2"] div {
           font-size: 24px;
       }
       ```

     * 不能适应所有尺寸的设备，也不能解决高度上的自适应

4. 其他移动端适配方案

