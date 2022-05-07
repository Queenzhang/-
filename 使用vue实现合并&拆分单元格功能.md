### 使用vue实现合并&拆分单元格功能

+ **前情提要**

  项目中需要实现视频分屏操作，除了传统的1、4、9……均匀分布，还需要支持用户自定义布局。这就类似excel的合并、拆分单元格功能。

+ **思路**

  首先，选择布局模式。在尝试了css的flex、grid布局之后，还是不得不选择table。

  其次，基于vue是数据驱动页面显示，所以不同于传统js的需要操作dom元素（这将提高代码量和难度），主要是需要定义一些关键参数来表示单元格之间的关系以及操作过程中的中间参数。

  最后，计算单元格的跨行跨列值，这里参考了

  [js实现单元格合并和取消合并操作]: https://blog.csdn.net/xiaozaq/article/details/110060714

  主要是通过计算选中的区域的x、y值来计算合并的colspan和rowspan。

+ **主要代码**

```js
<template>
  <div class="wrap">
    <div class="button_wrap">
      <el-row>
        <el-button type="primary" size="mini" @click="handleQuick(1)">1屏</el-button>
        <el-button type="primary" size="mini" @click="handleQuick(4)">4屏</el-button>
        <el-button type="primary" size="mini" @click="handleQuick(9)">9屏</el-button>
        <el-button type="primary" size="mini" @click="handleQuick(16)">16屏</el-button>
      </el-row>
      <el-row>
        <el-button type="primary" size="mini" @click="handleSplit">拆分</el-button>
        <el-button type="primary" size="mini" @click="handleMerge">合并</el-button>
        <el-button type="primary" size="mini" @click="handleSelectAll">全选</el-button>
        <el-button type="primary" size="mini" @click="handleCancelAll">全部取消</el-button>
      </el-row>
    </div>
    <div class="basic_wrap">
      <table ref="table_wrap" @mousedown="mousedown" @mouseenter="mouseenter" @mouseup="mouseup">
        <tr ref="table_tr" v-for="(item,index) in layoutTable" :key="index">
          <template v-if="item.rowspan">
            <td
              v-for="(td,idx) in item.colspan"
              :key="idx"
              :rowspan="item.rowspan[idx]"
              :colspan="item.colspan[idx]"
              :class="{default:true,isChosen:item.isChosen[idx]}"
              :style="computeTdStyle(item.rowspan[idx],item.colspan[idx])"
              @click="(el)=>clickTd(el,item,idx)"
            ></td>
          </template>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "EditLayout",
  computed: {},
  data() {
    return {
      num: 4,
      defaultW: 400,
      defaultH: 400,
      isChosenTds: [],
      area: [],
      layoutTable: [
        {
          colspan: [1, 1, 1, 1],
          rowspan: [1, 1, 1, 1],
          isChosen: [true, true, true, true]
        },
        {
          colspan: [1, 1, 1, 1],
          rowspan: [1, 1, 1, 1],
          isChosen: [true, true, true, true]
        },
        {
          colspan: [1, 1, 1, 1],
          rowspan: [1, 1, 1, 1],
          isChosen: [true, true, true, true]
        },
        {
          colspan: [1, 1, 1, 1],
          rowspan: [1, 1, 1, 1],
          isChosen: [true, true, true, true]
        }
      ]
    };
  },
  watch: {},
  created() {},
  mounted() {
    this.$nextTick(() => {
      this.selectTd();
    });
  },
  methods: {
    handleQuick(num) {
      let row = Math.sqrt(num);
      this.num = row;
      let arr = [];
      for (let i = 0; i < row; i++) {
        let colspan = [];
        let rowspan = [];
        let isChosen = [];

        for (let j = 0; j < row; j++) {
          colspan.push(1);
          rowspan.push(1);
          isChosen.push(true);
        }
        arr.push({ colspan, rowspan, isChosen });
      }
      this.layoutTable = arr;
      this.$nextTick(() => {
        this.selectTd();
      });
    },
    handleSplit() {
      let len = this.isChosenTds.length;
      // console.log(len, this.num);
      if (len !== 1) {
        this.$message({
          type: "warning",
          message:
            len === 0 ? "请选择需要拆分的屏幕！" : "请选择需要拆分的1块屏幕！"
        });
        return;
      } else if (this.num === 1) {
        this.handleQuick(4);
      } else {
        let item = this.isChosenTds[0];
        let { rowIndex, colIndex, colspan, rowspan } = item;
        for (let i = rowIndex; i < rowIndex + rowspan; i++) {
          let new_colspan = [];
          let new_rowspan = [];
          let new_isChosen = [];

          for (let j = 0; j < this.num; j++) {
            new_colspan.push(1);
            new_rowspan.push(1);

            let isChosen =
              j < colIndex || j > colIndex + colspan - 1 ? false : true;
            new_isChosen.push(isChosen);
          }

          let obj = {
            colspan: new_colspan,
            rowspan: new_rowspan,
            isChosen: new_isChosen
          };

          this.$set(this.layoutTable, i, obj);
        }
        this.$nextTick(() => {
          this.selectTd();
        });
      }
    },
    handleMerge() {
      let len = this.isChosenTds.length;
      if (len < 2) {
        this.$message({
          type: "warning",
          message: "请选择需要合并的屏幕！！"
        });
        return;
      }

      //全选 计算
      let isAllChosen = true;
      for (let i = 0; i < this.layoutTable.length; i++) {
        let isChosen = this.layoutTable[i].isChosen;
        if (!isChosen) {
          continue;
        }
        if (isChosen.indexOf(false) > -1) {
          isAllChosen = false;
          break;
        }
      }
      // console.log("rrrrr", this.isChosenTds,total);

      if (isAllChosen) {
        this.handleQuick(1);
        return;
      }

      // 一般合并
      let newArr = [];
      let a = 400 / this.num;
      for (var i = 0; i < this.isChosenTds.length; i++) {
        var td = this.isChosenTds[i];
        let obj = {};
        let rowspan = 0;
        let colspan = 0;

        if (td.pos.x == this.area.xMin && td.pos.y == this.area.yMin) {
          rowspan = Math.round((this.area.yMax - this.area.yMin) / a);
          colspan = Math.round((this.area.xMax - this.area.xMin) / a);
        }
        obj = { ...this.isChosenTds[i], rowspan, colspan };
        newArr.push(obj);
      }
      this.layoutTable = this.createNewLayout(newArr);
      this.$nextTick(() => {
        this.selectTd();
      });
    },
    createNewLayout(newArr) {
      for (let i = 0; i < newArr.length; i++) {
        let { colspan, rowspan, rowIndex, colIndex } = newArr[i];
        let obj = this.layoutTable[rowIndex];
        obj["colspan"][colIndex] = colspan;
        obj["rowspan"][colIndex] = rowspan;
        obj["isChosen"][colIndex] = colspan > 0 ? true : false;
      }
      let arr = this.layoutTable.map(item => {
        let { colspan, rowspan, isChosen } = item;
        if (!colspan) {
          return {};
        }
        let new_colspan = [];
        let new_rowspan = [];
        let new_isChosen = [];
        for (let i = 0; i < colspan.length; i++) {
          if (colspan[i] !== 0) {
            new_colspan.push(colspan[i]);
            new_rowspan.push(rowspan[i]);
            new_isChosen.push(isChosen[i]);
          }
        }
        if (new_colspan.length > 0) {
          return {
            colspan: new_colspan,
            rowspan: new_rowspan,
            isChosen: new_isChosen
          };
        }
        return {};
      });
      return arr;
    },
    handleSelectAll() {
      for (let i = 0; i < this.layoutTable.length; i++) {
        let item = this.layoutTable[i].isChosen;
        if (!item) {
          continue;
        }
        for (let j = 0; j < item.length; j++) {
          item[j] = true;
        }
      }
      this.layoutTable = this.layoutTable.concat([]);
      this.$nextTick(() => {
        this.selectTd();
      });
    },
    handleCancelAll() {
      for (let i = 0; i < this.layoutTable.length; i++) {
        let item = this.layoutTable[i].isChosen;
        if (!item) {
          continue;
        }
        for (let j = 0; j < item.length; j++) {
          item[j] = false;
        }
      }
      this.layoutTable = this.layoutTable.concat([]);
      this.$nextTick(() => {
        this.selectTd();
      });
    },
    clickTd(el, item, idx) {
      let val = !item.isChosen[idx];
      this.$set(item.isChosen, idx, val);
      this.$nextTick(() => {
        this.selectTd();
      });
    },
    mousedown(val) {
      // console.log("mousedown");
    },
    mouseenter(val) {
      // console.log("mouseenter");
    },
    mouseup(val) {
      // console.log("mouseup");
    },
    selectTd() {
      let table_tr = this.$refs.table_tr;

      let arr = [];
      for (let i = 0; i < this.layoutTable.length; i++) {
        let tr = table_tr[i];
        let { isChosen, colspan, rowspan } = this.layoutTable[i];
        if (!isChosen) {
          continue;
        }
        for (let j = 0; j < isChosen.length; j++) {
          let td = tr.children[j];
          if (isChosen[j]) {
            arr.push({
              rowIndex: i,
              colIndex: j,
              colspan: colspan[j],
              rowspan: rowspan[j],
              pos: {
                x: td.offsetLeft,
                y: td.offsetTop
              }
            });
          }
        }
      }
      this.isChosenTds = arr;
      this.area = this.getMinArea();
    },
    getAreaByTds() {
      let a = 400 / this.num;
      let containTds = this.isChosenTds;
      var area = { xMin: 99999, yMin: 99999, xMax: -1, yMax: -1 };
      for (var i = 0; i < containTds.length; i++) {
        var xMin = Number(containTds[i].pos.x);
        var yMin = Number(containTds[i].pos.y);
        var xMax = Number(containTds[i].pos.x + containTds[i].colspan * a);
        var yMax = Number(containTds[i].pos.y + containTds[i].rowspan * a);
        area.xMin = Math.min(area.xMin, xMin);
        area.yMin = Math.min(area.yMin, yMin);
        area.xMax = Math.max(area.xMax, xMax);
        area.yMax = Math.max(area.yMax, yMax);
      }
      return area;
    },
    getMinArea() {
      var newTds = [];
      var targetArea = this.getAreaByTds();
      return targetArea;
    },
    computeTdStyle(numH, numW) {
      let height = (400 / this.num) * numH;
      let width = (400 / this.num) * numW;
      return { height: height + "px", width: width + "px" };
    }
  }
};
</script>

<style lang="scss" scoped>
.wrap {
  width: 100%;
  max-height: 500px;
  overflow: auto;
  .button_wrap {
    .el-row {
      height: 40px;
    }
  }
  .basic_wrap {
    width: 405px;
    height: 405px;
    margin: 0 auto;
    // display: flex;
    // flex-flow: wrap;
    background: rgba(0, 12, 12, 0.5);
    border: 1px solid rgba(0, 12, 12, 0.9);
    table {
      width: 100%;
      height: 100%;
      text-align: center;
      border-spacing: 0;
      border: 1px solid #fff;
      // background: red;
      td {
        // border: 1px solid #fff;
        border-bottom: 1px solid #fff;
        border-right: 1px solid #fff; //给右和底边框,有重合2像素的,单独调
      }
      // & .default {
      //   border-bottom: 1px solid #fff;
      //   border-right: 1px solid #fff; //给右和底边框,有重合2像素的,单独调
      // }
      & .isChosen {
        // border: 1px solid red;
        background: red;
      }
    }
  }
}
</style>

```

+ **小结**

  个人认为难点在于合并，也就是跨行跨列的计算，拆分则比较简单，只需要生成标准表格即可。接着就是数据格式的定义和处理，我用了很多for循环，感觉代码不是很优雅。最后，代码还缺少类似参考博文中的能否进行合并拆分的判断以及鼠标移动选择的交互，整体上还可以继续优化的部分很多。至于布局的选择，table是最先想到的，但是由于个人不喜欢这个布局，所以中间走了很多弯路。事实证明不能任性。

