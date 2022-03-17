### 函数式编程的curry与compose思想

#### 柯里化

把一个多参数的函数转化为单一参数函数, curry 主要有 3 个作用：缓存函数、暂缓函数执行、分解执行任务。

```js
const curry=(fn,arity=fn.length)=>{
  const curried=(...args)=>args.length>=arity?fn(...args):(...restArgs)=>curried(...args,...restArgs);
  return curried;
};

const add=(a,b,c,d,e)=>a+b+c+d+e;

const addResult=curry(add)(1)(3)(5)(7)(9); //25
```

```js
实现：
sum(1).valueOf() => 1;
sum(1,2).valueOf() => 3;
sum(1,2)(3).valueOf() => 6;

//其实考察的就是curry化：
function sum(...args) {
    var saveArg = args || [];

    function sub(...ags) {
        saveArg = saveArg.concat(ags);
        return sub;
    }
    sub.valueOf = function() {
        return saveArg.reduce(function(a, b){
            return a + b;
        });
    }
    return sub;
}
```

柯里化带给我们的好处：

- 语义更加清晰
- 可复用性更高
- 可维护性更好
- 作用域局限，副作用少

#### 组合

将多个函数的能力合并，创造一个新的函数。compsoe函数可以接受任意的参数，所有的参数都是函数，且执行方向是自右向左的，初始函数一定放到参数的最右面。

```js
var compose = function (f, g) {
    return function (x) {
        return f(g(x));
    };
};
```

compose 函数的作用就是组合函数，将函数串联起来执行，一个函数的输出结果是另一个函数的输入参数，一旦第 1 个函数开始执行，就会像多米诺骨牌一样推导执行了。

koa.js

