### 《JavaScript设计模式》

原文地址：[[Learning JavaScript Design Patterns](https://www.patterns.dev/posts/classic-design-patterns/)]

#### 前言

编写可维护代码很重要！好的设计模式可以帮助我们注意到代码中重复出现的主题并对其进行优化（更好地编写可维护代码）。

#### 什么是模式？

设计模式是一种可重用的解决方案。在编写应用时，可以在不同的情况下使用不同的设计模式来解决问题。

**特性：**

* 经过验证

* 易于重用

* 具有解释性：用集合或者简单的词汇来描述复杂的解决方案

模式并不能解决所有的设计问题，但能提供很多**优势：**

1.    有助于发现可能导致开发过程中出现重大问题的小问题

2.    设计模式是通用的，不同的编程语言都可以应用来改进代码结构

3.    方便开发人员交流

4.    基于设计模式的解决方案比临时解决方案更稳定强大

#### 测试、原型模式、三法则

**测试**：完整的模式是经过严格审查和测试的

**原型模式**:尚未通过测试的模式，可能来自个人、社区

一个好的模式需要：

* 解决一个特定的问题

* 问题的解决方案不是显而易见的（好的设计模式通常间接地为问题提供解决方案）[?]

* 所描述的概念必须是已经被证明过的（设计模式需要证明它们的功能与描述的一致）

* 必须描述一种关系（设计模式需要描述深层次的系统结构和机制与代码的关系）

**三法则：**

1.    模型如何被认为是成功的？（how/适合解决某种问题）

2.    为什么模型被认为是成功的？（why/对于目标是起作用的）

3.    具有普遍的/广泛的适用性

#### 设计模式的结构

一个设计模式应该包括（设计自己的模式时）：

1.    名称和描述

2.    上下文大纲

3.    问题陈述

4.    解决方案

5.    设计：包括与用户的交互行为

6.    执行（操作）指南

7.    可视化表示

8.    示例/举例

9.    其他支持：包括其他模式

10.    与其他模式的关系描述（借鉴/类似）

11.    实际应用

12.    讨论

#### 编写设计模式（pass）

#### 现代JavaScript语法和特征

* **解耦应用程序的重要性**：模块化可以使程序更容易维护

* **import、export**：模块化鼓励代码重用
  
  *.mjs is an extension used for JavaScript modules that helps us distinguish between module files and classic scripts (.js).*

* **远程加载模块**

* **动态导入**：静态导入需要先下载、执行模块图后再运行代码，这可能会导致初始页面加载时间过长；按需加载可以提高初始加载时的性能
  
  ```js
  form.addEventListener("submit", e => {
    e.preventDefault();
    import("/modules/cakeFactory.js")
      .then((module) => {
        // Do something with the module.
        module.oven.makeCupcake("sprinkles");
        module.oven.makeMuffin("large");
      });
  });
  
  let module = await import("/modules/cakeFactory.js");
  ```

* **服务器模块**：node 15.3.0开始支持js-modules(npm)

* **Classes With <u>Constructors, Getters & Setters</u>**:
  
  ```javascript
  class Cake{
  
      // We can define the body of a class" constructor
      // function by using the keyword "constructor" 
      // with a list of class variables.
      constructor( name, toppings, price, cakeSize ){
          this.name = name;
          this.cakeSize = cakeSize;
          this.toppings = toppings;
          this.price = price;
      }
  
      // As a part of ES2015+ efforts to decrease the unnecessary
      // use of "function" for everything, you'll notice that it's
      // dropped for cases such as the following. Here an identifier
      // followed by an argument list and a body defines a new method
  
      addTopping( topping ){
          this.toppings.push( topping );
      }
  
      // Getters can be defined by declaring get before
      // an identifier/method name and a curly body.
      get allToppings(){
          return this.toppings;
      }
  
      get qualifiesForDiscount(){
          return this.price > 5;
      }
  
      // Similar to getters, setters can be defined by using
      // the "set" keyword before an identifier
      set cakeSize( size ){
          if ( size < 0){
              throw "Cake must be a valid size - either small, medium or large";
          }
         this._cakeSize = size;//写成“cakeSize”会报错“ Maximum call stack size exceeded”
      }
  }
  
  // Usage
  let cake = new Cake( "chocolate", ["chocolate chips"], 5, "large" );
  
  // 继承
  class BirthdayCake extends Cake {
    surprise() {
      console.log(`Happy Birthday!`);
    }
  }
  
  let birthdayCake = new BirthdayCake( "chocolate", ["chocolate chips"], 5, "large" );
  birthdayCake.surprise();
  ```
  
  ```javascript
  class Cookies {
    constructor(flavor) {
      this.flavor = flavor;
    }
  
    showTitle() {
      console.log(`The flavor of this cookie is ${this.flavor}.`);
    }
  }
  
  class FavoriteCookie extends Cookies {
    showTitle() { 
      // super 调用父类的构造函数
      super.showTitle();
      console.log(`${this.flavor} is amazing.`);
    }
  }
  
  let myCookie = new FavoriteCookie('chocolate');
  myCookie.showTitle();
  ```
  
  ```javascript
  class CookieWithPrivateField {
  // 创建私有类字段
    #privateField;
  }
  
  class CookieWithPrivateMethod {
    #privateMethod() {
      return 'delicious cookies';
    }
  }
  ```

#### Anti-Patterns

1.    描述对导致不良情况发生的特定问题的<u>不良解决方案</u>

2.    描述<u>如何摆脱上述情况</u>以及如何从那里找到一个好的解决方案

每个设计都始于努力去解决问题和其解决方案之间的适应性。在程序投入生产并准备进入维护模式之后，创建anti-patterns可以避免发生常见的错误，重构代码时可以使解决方案的整体质量立即得到提高。

总而言之，反模式是一个值得记录的糟糕设计。 JavaScript 中的反模式示例如下：

- 通过在全局上下文中定义大量变量来污染全局命名空间

- 将字符串而不是函数传递给 setTimeout 或 setInterval，因为这会在内部触发 eval() 的使用

- 修改 Object 类原型

- 在内联表单中使用 JavaScript

- 严重滥用document.write，像 document.createElement 这样的原生 DOM 替代品更合适

#### 设计模式的类别

* **创建型设计模式**：专注于处理对象创建机制（通过控制创建过程来减少创建对象时导致的项目复杂性）。包括：构造函数、工厂、抽象、原型、单例和生成器。

* **结构型设计模式**：关注对象的组合以及确定不同对象之间关系的简单方法（系统的一部分发生变化时，整个结构不受影响；将系统中不适合的部分重铸为符合需求的部分）。包括：装饰器、外观（Facade）、享元（Flyweight）、适配器和代理。

* **行为型设计模式**：聚焦于改进或简化不同对象之间的通行。包括：迭代器、中介者、观察者和访问者。

#### 设计模式分类

GoF提及的23种设计模式：

| ****Creational**** | Based on the concept of creating an object.                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| ***Class***        |                                                                                                |
| *Factory Method*   | This makes an instance of several derived classes based on interfaced data or events.          |
| ***Object***       |                                                                                                |
| *Abstract Factory* | Creates an instance of several families of classes without detailing concrete classes.         |
| *Builder*          | Separates object construction from its representation, always creates the same type of object. |
| *Prototype*        | A fully initialized instance used for copying or cloning.                                      |
| *Singleton*        | A class with only a single instance with global access points.                                 |

| ****Structural**** | Based on the idea of building blocks of objects.                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------- |
| ***Class***        |                                                                                                               |
| *Adapter*          | Match interfaces of different classes therefore classes can work together despite incompatible interfaces.    |
| ***Object***       |                                                                                                               |
| *Adapter*          | Match interfaces of different classes therefore classes can work together despite incompatible interfaces.    |
| *Bridge*           | Separates an object's interface from its implementation so the two can vary independently.                    |
| *Composite*        | A structure of simple and composite objects which makes the total object more than just the sum of its parts. |
| *Decorator*        | Dynamically add alternate processing to objects.                                                              |
| *Facade*           | A single class that hides the complexity of an entire subsystem.                                              |
| *Flyweight*        | A fine-grained instance used for efficient sharing of information that is contained elsewhere.                |
| *Proxy*            | A place holder object representing the true object.                                                           |

| ****Behavioral****        | Based on the way objects play and work together.                                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Class***               |                                                                                                                                               |
| *Interpreter*             | A way to include language elements in an application to match the grammar of the intended language.                                           |
| *Template Method*         | Creates the shell of an algorithm in a method, then defer the exact steps to a subclass.                                                      |
| ***Object***              |                                                                                                                                               |
| *Chain of Responsibility* | A way of passing a request between a chain of objects to find the object that can handle the request.                                         |
| *Command*                 | Encapsulate a command request as an object to enable, logging and/or queuing of requests, and provides error-handling for unhandled requests. |
| *Iterator*                | Sequentially access the elements of a collection without knowing the inner workings of the collection.                                        |
| *Mediator*                | Defines simplified communication between classes to prevent a group of classes from referring explicitly to each other.                       |
| *Memento*                 | Capture an object's internal state to be able to restore it later.                                                                            |
| *Observer*                | A way of notifying change to a number of classes to ensure consistency between the classes.                                                   |
| *State*                   | Alter an object's behavior when its state changes.                                                                                            |
| *Strategy*                | Encapsulates an algorithm inside a class separating the selection from the implementation.                                                    |
| *Visitor*                 | Adds a new operation to a class without changing the class.                                                                                   |

#### JavaScript设计模式

* **构造函数模式**：对象构造函数用于创建特定类型的对象 - 既<u>准备对象以供使用</u>，也接受参数，构造函数可以在第一次创建对象时使用这些参数设置成员属性和方法的值。（Vue）
  
  ```javascript
  // 创建对象的方式
  const newObject = {};
  
  // or
  const newObject = Object.create(Object.prototype);
  
  // or
  const newObject = new Object();
  ```
  
  ```javascript
  // 给对象赋值
  // 1. Dot syntax
  
  // Set properties
  newObject.someKey = 'Hello World';
  
  // Get properties
  const value = newObject.someKey;
  
  // 2. Square bracket syntax
  
  // Set properties
  newObject['Some Key'] = 'Hello World';
  
  // Get properties
  const value = newObject['Some Key'];
  
  // For more information see: http://kangax.github.io/compat-table/es5/
  
  // 3. Object.defineProperty
  
  // Set properties
  Object.defineProperty(newObject, 'someKey', {
      value: "for more control of the property's behavior",
      writable: true,
      enumerable: true,
      configurable: true,
  });
  
  // If the above feels a little difficult to read, a shorthand could
  // be written as follows:
  const defineProp = (obj, key, value) => {
      const config = {
          value: value,
          writable: true,
          enumerable: true,
          configurable: true,
      };
      Object.defineProperty(obj, key, config);
  };
  
  // To use, we then create a new empty "person" object
  const person = Object.create(Object.prototype);
  
  // Populate the object with properties
  defineProp(person, 'car', 'Delorean');
  defineProp(person, 'dateOfBirth', '1981');
  defineProp(person, 'hasBeard', false);
  
  console.log(person);
  // Outputs: Object {car: "Delorean", dateOfBirth: "1981", hasBeard: false}
  
  // 4. Object.defineProperties
  
  // Set properties
  Object.defineProperties(newObject, {
      someKey: {
          value: 'Hello World',
          writable: true,
      },
  
      anotherKey: {
          value: 'Foo bar',
          writable: false,
      },
  });
  
  // Getting properties for 3. and 4. can be done using any of the
  // options in 1. and 2.
  ```
  
  ```javascript
  // 创建的对象可以被继承
  // Create a race car driver that inherits from the person object
  const driver = Object.create(person);
  
  // Set some properties for the driver
  defineProp(driver, 'topSpeed', '100mph');
  
  // Get an inherited property (1981)
  console.log(driver.dateOfBirth);
  
  // Get the property we set (100mph)
  console.log(driver.topSpeed);
  ```
  
  ```javascript
  // class方式
  class Car {
      constructor(model, year, miles) {
          this.model = model;
          this.year = year;
          this.miles = miles;
      }
  
      toString() {
          return `${this.model} has done ${this.miles} miles`;
      }
  }
  
  // Usage:
  
  // We can create new instances of the car
  let civic = new Car('Honda Civic', 2009, 20000);
  let mondeo = new Car('Ford Mondeo', 2010, 5000);
  
  // and then open our browser console to view the
  // output of the toString() method being called on
  // these objects
  console.log(civic.toString());
  console.log(mondeo.toString());
  ```
  
  ```javascript
  // 或者使用原型方法
  // Note here that we are using Object.prototype.newMethod rather than
  // Object.prototype so as to avoid redefining the prototype object
  // We still could use Object.prototype for adding new methods, because internally we use the same structure
  Car.prototype.toString = function() {
      return `${this.model} has done ${this.miles} miles`;
  };
  ```

* **模块模式**：模块是任何健壮的应用程序架构的一个组成部分，通常有助于保持项目的代码单元清晰地分离和组织。
  
  模块模式最初被定义为一种为传统软件工程中的类<u>提供私有和公共</u>封装的方法。现在，开发人员只需使用 JavaScript 模块来组织对象、函数、类或变量，就可以轻松地将它们导出或导入到其他文件中。<u> 这有助于防止不同模块中包含的类或函数名称之间的冲突。</u>
  
  * privacy：为我们提供了一个干净的解决方案，用于<u>屏蔽执行繁重工作的逻辑，同时仅公开我们希望应用程序的其他部分使用的接口</u>。 该模式使用一个立即调用的函数表达式，并返回一个对象。
    
    * 在JavaScript中，变量在不能被声明为公共或私有的，因此我们使用函数作用域来模拟这个概念。 在模块模式中，闭包、声明的变量或方法只能在模块本身内部使用。 然而，在返回对象中定义的变量或方法对每个人都是可用的。
    
    * 在返回的对象中实现变量隐私的解决方法是使用 Wea​​kMap() 。 WeakMap() 只将对象作为键，不能迭代。 因此，访问模块内对象的唯一方法是通过它的引用。 在模块外，只能通过模块内定义的公共方法访问它。 因此，它确保了对象的隐私。
    
    ```javascript
    // ES2015+ keywords/methods used: import, export, let, const, reduce()
    
    // privates
    
    const basket = [];
    
    const doSomethingPrivate = () => {
      //...
    };
    
    const doSomethingElsePrivate = () => {
      //...
    };
    
    // Create an object exposed to the public
    const basketModule = {
      // Add items to our basket
      addItem(values) {
        basket.push(values);
      },
    
      // Get the count of items in the basket
      getItemCount() {
        return basket.length;
      },
    
      // Public alias to a private function
      doSomething() {
        doSomethingPrivate();
      },
    
      // Get the total value of items in the basket
      // The reduce() method applies a function against an accumulator and each element in the array (from left to right) to reduce it to a single value.
      getTotal() {
        return basket.reduce((currentSum, item) => item.price + currentSum, 0);
      },
    };
    
    export default basketModule;
    ```
    
    ```javascript
    import basketModule from './basketModule';
    
    // basketModule returns an object with a public API we can use
    
    basketModule.addItem({
      item: 'bread',
      price: 0.5,
    });
    
    basketModule.addItem({
      item: 'butter',
      price: 0.3,
    });
    
    // Outputs: 2
    console.log(basketModule.getItemCount());
    
    // Outputs: 0.8
    console.log(basketModule.getTotal());
    
    // However, the following will not work:
    
    // Outputs: undefined
    // This is because the basket itself is not exposed as a part of our
    // public API
    console.log(basketModule.basket);
    
    // This also won't work as it only exists within the scope of our
    // basketModule closure, but not in the returned public object
    console.log(basket);
    ```
    
    

* **揭示模块模式**
