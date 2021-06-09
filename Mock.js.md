## Mock.js

1. 特点

   + 前后端分离
   + 开发无侵入
     * 不需要修改既有代码，就可以**拦截Ajax请求**，返回模拟的响应数据
   + 数据类型丰富
     * 支持生成**随机**的文本、数字、布尔值、日期、邮箱、链接、图片、颜色等
   + 增加单元测试的真实性
     + 随机生成数据
   + 用法简单
   + 方便扩展
     + **支持自定义函数和正则**

2. 安装

   ```js
   npm install mockjs
   ```

3. 使用

   ```js
   var Mock = require('mockjs')
   var data = Mock.mock({
       // 属性 list 的值是一个数组，其中含有 1 到 10 个元素
       'list|1-10': [{
           // 属性 id 是一个自增数，起始值为 1，每次增 1
           'id|+1': 1
       }]
   })
   // 输出结果
   console.log(JSON.stringify(data, null, 4))
   ```

4. 语法规范

   * 数据模板定义

     * 属性名、规则、属性值

       ```
       'name|rule': value
       ```

       **********

       - *属性名* 和 *生成规则* 之间用竖线 `|` 分隔。

       - *生成规则* 是可选的。

       - 生成规则

          

         有 7 种格式：

         1. `'name|min-max': value`
         2. `'name|count': value`
         3. `'name|min-max.dmin-dmax': value`
         4. `'name|min-max.dcount': value`
         5. `'name|count.dmin-dmax': value`
         6. `'name|count.dcount': value`
         7. `'name|+step': value`

       - ***生成规则\* 的 含义 需要依赖 \*属性值的类型\* 才能确定。**

       - *属性值* 中可以含有 `@占位符`。

       - *属性值* 还指定了最终值的初始值和类型。

   * 数据占位符定义

     * 格式：

       ```
       @占位符
       @占位符(参数 [, 参数])
       ```

       *****

       1. 用 `@` 来标识其后的字符串是 *占位符*。
       2. *占位符* 引用的是 `Mock.Random` 中的方法。
       3. 通过 `Mock.Random.extend()` 来扩展自定义占位符。
       4. *占位符* 也可以引用 *数据模板* 中的属性。
       5. *占位符* 会优先引用 *数据模板* 中的属性。
       6. *占位符* 支持 *相对路径* 和 *绝对路径*。     

   * 示例

     * [mock.js官方示例]（http://mockjs.com/examples.html#Random\.region\(\)）

5. 应用

