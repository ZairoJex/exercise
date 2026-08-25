# 第一周第一天：Python 变量、类型、输入输出详细学习教程

> 适用对象：第一次系统学习 Python、目标是完成 AI Agent 工程学习路线的学习者  
> 当前环境：Windows 11、PowerShell、VS Code、`uv`、Python 3.11  
> 当天项目：摄氏温度转华氏温度命令行程序  
> 建议用时：约 5 小时 20 分钟  
> 最终文件：`D:\Agent\ai-agent-road\exercises\week01\day01.py`

---

## 1. 今天到底要学会什么

今天不是要记住 Python 的全部语法，而是建立第一个完整的编程闭环：

```text
用户输入文本
    ↓
把文本转换成数字
    ↓
使用公式计算
    ↓
把结果格式化后输出
    ↓
输入错误时给出友好提示
```

学完后，你应该能够独立完成以下事情：

1. 在正确的项目环境中创建并运行一个 Python 文件。
2. 使用变量保存数据，并遵守基本的命名规范。
3. 区分 `int`、`float`、`str`、`bool` 四种基础类型。
4. 理解 `input()` 得到的内容为什么一定是字符串。
5. 使用 `float()` 把可转换的字符串变成浮点数。
6. 使用算术运算符实现温度转换公式。
7. 使用函数封装计算逻辑，并用 `return` 返回结果。
8. 使用 f-string 输出保留两位小数的结果。
9. 使用 `try` / `except ValueError` 处理错误输入。
10. 在删除代码后，20 分钟内不看答案重新写出程序。

今天的最低交付物：

```text
D:\Agent\ai-agent-road\
├─ exercises\
│  └─ week01\
│     └─ day01.py
└─ notes\
   └─ week01_day01.md
```

---

## 2. 今日学习安排

| 阶段 | 建议用时 | 产出 |
|---|---:|---|
| 环境确认 | 10 分钟 | 确认使用项目的 Python 3.11 |
| 概念学习 | 60 分钟 | 理解变量、类型、输入、输出、运算符 |
| 跟练实验 | 45 分钟 | 在交互式环境中完成小实验 |
| 项目实现 | 135 分钟 | 分 5 步写出温度转换器 |
| 测试与排错 | 45 分钟 | 验证正常、边界和错误输入 |
| 闭卷重写 | 20 分钟 | 从空文件重写核心程序 |
| 笔记与 Git | 25 分钟 | 完成学习记录和一次提交 |

不要一次读完全文再开始写代码。每学完一个小节，就执行其中的实验。

---

## 3. 开始前：只使用当前项目环境

### 3.1 打开正确目录

打开 PowerShell，执行：

```powershell
cd D:\Agent\ai-agent-road
```

确认当前位置：

```powershell
Get-Location
```

预期路径：

```text
D:\Agent\ai-agent-road
```

### 3.2 检查环境

执行项目自带检查：

```powershell
uv run python scripts\check_environment.py
```

再确认 Python 版本：

```powershell
uv run python --version
```

预期看到 Python 3.11.x。具体的小版本号可能不同，但大版本和次版本应为 `3.11`。

### 3.3 今天禁止使用的命令

这台电脑上存在多个 Python，因此今天以及后续课程都不要使用：

```powershell
python day01.py
py day01.py
pip install ...
python -m pip ...
```

统一使用：

```powershell
uv run python 路径\文件名.py
```

这里的 `uv run` 会让命令使用当前项目锁定的 Python 和依赖，而不是误用电脑里的其他 Python。

### 3.4 创建今天需要的目录

在仓库根目录执行：

```powershell
New-Item -ItemType Directory -Force exercises\week01
New-Item -ItemType Directory -Force notes
```

`-Force` 在目录已经存在时不会报错，也不会删除其中的文件。

---

## 4. Python 程序是怎样运行的

Python 源代码保存在扩展名为 `.py` 的文本文件中。例如：

```text
day01.py
```

运行命令：

```powershell
uv run python exercises\week01\day01.py
```

可以把执行过程暂时理解为：

1. PowerShell 找到 `uv`。
2. `uv` 找到当前项目的 Python 3.11。
3. Python 从上到下读取 `day01.py`。
4. Python 检查语法并执行语句。
5. `print()` 把结果写到终端，`input()` 从终端读取输入。

### 4.1 第一条 Python 语句

在 `day01.py` 中写入：

```python
print("你好，Python")
```

运行：

```powershell
uv run python exercises\week01\day01.py
```

预期输出：

```text
你好，Python
```

这行代码由四部分组成：

| 部分 | 含义 |
|---|---|
| `print` | Python 内置的输出函数 |
| `(` 和 `)` | 函数调用的括号 |
| `"你好，Python"` | 一个字符串，也就是文本数据 |
| 行末换行 | 一条语句结束，不需要写分号 |

### 4.2 源代码必须使用英文标点

下面的代码是错误的：

```python
print（“你好，Python”）
```

其中的括号和引号是中文全角符号，运行时通常会出现 `SyntaxError`。写代码时切换到英文输入法，使用：

```python
print("你好，Python")
```

中文可以出现在字符串和注释里；Python 语法符号应使用英文半角字符。

### 4.3 注释

以 `#` 开头的内容是注释，Python 不会执行它：

```python
# 输出一行问候语
print("你好，Python")
```

注释应该解释“为什么”，不要重复代码已经清楚表达的内容。今天为了学习可以多写一点，熟练后再减少。

---

## 5. 变量：给数据起一个可读的名字

变量用于让程序在后续步骤中再次使用某个值。

```python
celsius = 25.0
```

这行代码的意思是：计算右侧的值 `25.0`，然后让名称 `celsius` 指向这个值。

可以暂时把变量想象成贴在数据上的标签，但要记住：变量名不是字符串，变量本身也不等于一个永久固定的盒子。

```python
celsius = 25.0
print(celsius)

celsius = 30.0
print(celsius)
```

输出：

```text
25.0
30.0
```

第二次赋值后，`celsius` 指向了新的值。

### 5.1 `=` 是赋值，不是数学等式

```python
count = 1
count = count + 1
```

第二行的执行顺序是：

1. 读取右侧旧的 `count`，得到 `1`。
2. 计算 `1 + 1`，得到 `2`。
3. 把结果 `2` 重新赋给左侧的 `count`。

因此最后 `count` 是 `2`。

判断两个值是否相等使用 `==`，以后会在分支课程中重点学习：

```python
print(count == 2)  # True
```

### 5.2 变量命名规则

合法变量名：

```python
temperature = 25.0
celsius_value = 25.0
day1_score = 100
```

不合法或不推荐的变量名：

```python
1day = 1          # 错误：不能用数字开头
user-name = "小明"  # 错误：减号会被当成运算符
float = 25.0      # 不推荐：覆盖了内置函数 float
x = 25.0          # 语法合法，但在这里含义不清楚
```

今天遵守四条即可：

1. 使用小写英文字母。
2. 多个单词之间使用下划线 `_`。
3. 名字要能说明数据含义。
4. 不要把 `input`、`print`、`float`、`str`、`type` 当作变量名。

温度转换器中推荐使用：

```python
raw
celsius
fahrenheit
```

其中 `raw` 表示“未经转换的原始输入”。

---

## 6. 基础数据类型

Python 中“值”有类型。类型决定一个值能参加哪些操作，以及操作结果是什么。

### 6.1 四种基础类型

| 类型 | 中文 | 示例 | 典型用途 |
|---|---|---|---|
| `int` | 整数 | `0`、`100`、`-7` | 数量、编号、整数计数 |
| `float` | 浮点数 | `3.14`、`25.0`、`-40.0` | 温度、比例、测量值 |
| `str` | 字符串 | `"25"`、`"你好"` | 文本、用户输入 |
| `bool` | 布尔值 | `True`、`False` | 是/否、成功/失败状态 |

注意：

```python
25      # int
25.0    # float
"25"    # str
```

它们看起来相似，但类型不同。

### 6.2 使用 `type()` 检查类型

进入项目的交互式 Python：

```powershell
uv run python
```

看到 `>>>` 后逐行输入：

```python
type(25)
type(25.0)
type("25")
type(True)
```

预期分别得到：

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

输入以下命令退出交互式环境：

```python
quit()
```

`type()` 适合学习和调试。正式业务代码通常不需要到处打印类型。

### 6.3 类型为什么重要

数字相加：

```python
print(20 + 5)
```

输出：

```text
25
```

字符串相加表示拼接：

```python
print("20" + "5")
```

输出：

```text
205
```

字符串和数字直接相加会失败：

```python
print("20" + 5)
```

错误类型通常是：

```text
TypeError
```

这说明“值长得像数字”并不等于“值就是数字”。

### 6.4 类型转换

Python 提供了多个内置转换函数：

```python
float("25")     # 25.0
float("25.5")   # 25.5
int("25")       # 25
str(25.0)       # "25.0"
```

无法转换时会产生异常：

```python
float("abc")
```

错误类型是：

```text
ValueError
```

这里不是 Python 不认识 `float`，而是字符串 `"abc"` 不能表示合法的浮点数。

### 6.5 `float` 的精度边界

`float` 很适合本项目的温度计算，但它使用二进制浮点表示，并不能精确表示所有十进制小数。例如：

```python
print(0.1 + 0.2)
```

可能输出：

```text
0.30000000000000004
```

今天不需要研究浮点数底层原理。只要记住：

- 温度、普通测量和大多数科学计算可以先使用 `float`。
- 金额等要求精确十进制的数据不能简单依赖 `float`。
- `:.2f` 只是格式化显示，不会把底层值永久改成两位小数。

---

## 7. 输入：`input()` 永远返回字符串

运行下面的程序：

```python
raw = input("请输入摄氏温度：")
print(raw)
print(type(raw))
```

即使输入 `25`，`type(raw)` 仍会显示：

```text
<class 'str'>
```

### 7.1 为什么输入数字后得到的还是字符串

键盘输入本质上是一串字符。Python 不会擅自猜测：

- `001` 是数字 1，还是编号字符串 `"001"`？
- `2026-08-23` 是日期，还是普通文本？
- `1e3` 是科学计数法，还是产品型号？

所以 `input()` 统一返回 `str`，由程序根据业务规则决定如何转换。

### 7.2 正确的数据流

```python
raw = input("请输入摄氏温度：")
celsius = float(raw)
```

此时：

```text
raw       -> str
celsius   -> float
```

### 7.3 常见错误：直接拿输入做算术

错误写法：

```python
celsius = input("请输入摄氏温度：")
fahrenheit = celsius * 9 / 5 + 32
```

`celsius` 是字符串，不能直接完成这组数值运算，所以会出现 `TypeError`。

正确写法：

```python
raw = input("请输入摄氏温度：")
celsius = float(raw)
fahrenheit = celsius * 9 / 5 + 32
```

---

## 8. 运算符和温度转换公式

### 8.1 今天会用到的算术运算符

| 运算符 | 含义 | 示例 | 结果 |
|---|---|---|---|
| `+` | 加 | `2 + 3` | `5` |
| `-` | 减或负号 | `5 - 2`、`-40` | `3`、`-40` |
| `*` | 乘 | `3 * 4` | `12` |
| `/` | 除 | `9 / 5` | `1.8` |
| `//` | 整除 | `9 // 5` | `1` |
| `%` | 取余数 | `9 % 5` | `4` |
| `**` | 幂 | `2 ** 3` | `8` |

温度公式必须使用 `/`，不能使用 `//`。`9 // 5` 会得到 `1`，从而让公式结果错误。

### 8.2 摄氏度转华氏度

公式：

```text
华氏度 = 摄氏度 × 9 ÷ 5 + 32
```

Python 表达式：

```python
fahrenheit = celsius * 9 / 5 + 32
```

也可以写成：

```python
fahrenheit = celsius * 1.8 + 32
```

本教程使用第一种写法，因为它能直接对应公式。

### 8.3 运算优先级

乘法和除法先于加法，因此：

```python
celsius * 9 / 5 + 32
```

相当于：

```python
((celsius * 9) / 5) + 32
```

如果不确定优先级，使用括号表达意图：

```python
fahrenheit = (celsius * 9 / 5) + 32
```

不要把公式误写成：

```python
fahrenheit = celsius * 9 / (5 + 32)
```

括号改变了计算顺序，也改变了公式含义。

### 8.4 手算三个基准值

在写程序前先手算，这些值之后就是测试依据。

摄氏 `0`：

```text
0 × 9 ÷ 5 + 32 = 32
```

摄氏 `100`：

```text
100 × 9 ÷ 5 + 32 = 212
```

摄氏 `-40`：

```text
-40 × 9 ÷ 5 + 32 = -40
```

`-40` 是摄氏和华氏刻度相等的特殊点，很适合检查负数和公式是否正确。

---

## 9. 输出：`print()`、f-string 和两位小数

### 9.1 输出普通文本和变量

```python
fahrenheit = 77.0
print("华氏温度：")
print(fahrenheit)
```

也可以一次输出多个值：

```python
print("华氏温度：", fahrenheit)
```

`print()` 默认会在多个参数之间添加空格。

### 9.2 f-string

推荐使用 f-string 把变量嵌入文本：

```python
print(f"华氏温度：{fahrenheit}")
```

关键结构：

```text
f"文本 {Python 表达式}"
```

字符串前面的 `f` 不能漏，变量或表达式写在 `{}` 中。

### 9.3 `:.2f` 的含义

```python
print(f"华氏温度：{fahrenheit:.2f}")
```

拆开理解：

| 部分 | 含义 |
|---|---|
| `{fahrenheit}` | 取变量的值 |
| `:` | 开始书写格式说明 |
| `.2` | 小数点后显示两位 |
| `f` | 按定点浮点数格式显示 |

示例：

```python
value = 32
print(f"{value:.2f}")
```

输出：

```text
32.00
```

再看一个四舍五入显示的例子：

```python
value = 98.678
print(f"{value:.2f}")
```

输出：

```text
98.68
```

`:.2f` 控制的是显示形式。变量 `value` 本身仍然保存原来的浮点数值。

### 9.4 常见格式化错误

漏掉 `f`：

```python
print("华氏温度：{fahrenheit:.2f}")
```

它会原样输出花括号中的文本。

把格式写到花括号外：

```python
print(f"华氏温度：{fahrenheit}:.2f")
```

它不会把变量格式化成两位小数。

正确写法：

```python
print(f"华氏温度：{fahrenheit:.2f}")
```

---

## 10. 函数：把计算规则单独封装

今天只掌握函数最小知识，不需要提前学习复杂参数。

```python
def celsius_to_fahrenheit(value: float) -> float:
    return value * 9 / 5 + 32
```

### 10.1 逐部分解释

| 代码 | 含义 |
|---|---|
| `def` | 开始定义函数 |
| `celsius_to_fahrenheit` | 函数名，表示“摄氏转华氏” |
| `(value: float)` | 接收一个名为 `value` 的参数，期望它是 `float` |
| `-> float` | 表示函数预期返回 `float` |
| `:` | 函数头结束，下一行开始函数体 |
| 四个空格 | 表示下一行属于函数体 |
| `return` | 把计算结果返回给调用者 |

### 10.2 定义函数不等于执行函数

只写：

```python
def celsius_to_fahrenheit(value: float) -> float:
    return value * 9 / 5 + 32
```

不会自动打印任何东西。需要调用：

```python
result = celsius_to_fahrenheit(0.0)
print(result)
```

执行过程：

```text
传入 0.0
    ↓
函数内部 value = 0.0
    ↓
计算 value * 9 / 5 + 32
    ↓
return 32.0
    ↓
外部变量 result 接收 32.0
```

### 10.3 `return` 和 `print` 不一样

错误理解：函数只要 `print` 结果就等于返回结果。

```python
def wrong_convert(value: float) -> None:
    print(value * 9 / 5 + 32)
```

这个函数把结果显示到屏幕，但没有把结果交给调用者继续使用。

推荐：

```python
def celsius_to_fahrenheit(value: float) -> float:
    return value * 9 / 5 + 32
```

外部可以决定如何使用返回值：

```python
result = celsius_to_fahrenheit(25.0)
print(f"华氏温度：{result:.2f}")
```

核心区别：

- `return`：把值交还给调用函数的代码。
- `print`：把文本显示到终端。
- `return` 执行后，函数本次调用立即结束。

### 10.4 类型标注不是自动转换

```python
def celsius_to_fahrenheit(value: float) -> float:
    return value * 9 / 5 + 32
```

`value: float` 是给读者和检查工具看的说明，不会自动执行 `float(value)`，也不会在运行时绝对禁止传入其他类型。

所以用户输入仍然需要显式转换：

```python
value = float(raw)
```

---

## 11. 异常处理：错误输入不能显示长堆栈

### 11.1 先观察失败

假设程序直接执行：

```python
raw = input("请输入摄氏温度：")
value = float(raw)
```

输入：

```text
abc
```

`float("abc")` 无法完成转换，会抛出 `ValueError`。如果没有处理，终端会显示一段 traceback，并停止程序。

traceback 对开发者排错很有价值，但普通用户不应该因为一次可预期的错误输入看到长堆栈。

### 11.2 使用 `try` / `except`

```python
try:
    value = float(raw)
except ValueError:
    print("请输入数字")
    return
```

执行逻辑：

```text
尝试执行 float(raw)
    ├─ 成功：跳过 except，继续向下执行
    └─ ValueError：执行 except 中的代码
                     输出“请输入数字”
                     return 结束 main()
```

### 11.3 为什么只捕获 `ValueError`

本程序明确知道 `float(raw)` 可能因为输入格式错误产生 `ValueError`，因此只捕获它：

```python
except ValueError:
```

不推荐今天写：

```python
except:
```

也不推荐无差别吞掉所有错误：

```python
except Exception:
    pass
```

过宽的捕获可能隐藏代码缺陷，让程序“看起来没报错”，实际上什么也没完成。

### 11.4 为什么 `try` 中只放转换语句

推荐：

```python
try:
    value = float(raw)
except ValueError:
    print("请输入数字")
    return

fahrenheit = celsius_to_fahrenheit(value)
```

不要把一大段无关逻辑全部放进 `try`。`try` 范围越小，就越清楚究竟在处理哪一种可预期错误。

---

## 12. 主程序入口：`main()` 和 `__name__`

完整程序会包含：

```python
def main() -> None:
    ...


if __name__ == "__main__":
    main()
```

### 12.1 `main()` 的职责

今天的 `main()` 负责组织交互流程：

1. 读取用户输入。
2. 尝试转换类型。
3. 调用计算函数。
4. 输出结果。

计算公式本身放在 `celsius_to_fahrenheit()` 中。

### 12.2 `-> None` 是什么意思

```python
def main() -> None:
```

表示 `main()` 的职责是执行流程，不需要向调用者返回一个业务结果。

### 12.3 `if __name__ == "__main__"` 是什么意思

当 Python 直接运行这个文件时，内置变量 `__name__` 的值是 `"__main__"`，于是执行 `main()`。

当以后其他文件导入这里的转换函数时，`__name__` 不是 `"__main__"`，交互式输入不会自动开始。

这让一个文件可以同时做到：

- 被直接运行时，启动命令行程序。
- 被其他代码导入时，只提供函数。

今天先会写、会解释这个目的即可，不要求研究 Python 的模块加载细节。

---

## 13. 项目实战：分五步完成温度转换器

不要直接跳到完整答案。每完成一步，都运行一次程序。

### 第一步：固定数据完成计算

先不接收输入，只验证公式：

```python
celsius = 0.0
fahrenheit = celsius * 9 / 5 + 32
print(f"华氏温度：{fahrenheit:.2f}")
```

运行：

```powershell
uv run python exercises\week01\day01.py
```

预期：

```text
华氏温度：32.00
```

然后把 `celsius` 依次改成 `100.0` 和 `-40.0`，确认公式正确。

检查点：

- 能解释为什么使用 `float` 数据。
- 能解释 `/` 和 `//` 的区别。
- 能解释 `:.2f`。

### 第二步：读取用户输入

把固定数据改成：

```python
raw = input("请输入摄氏温度：")
celsius = float(raw)
fahrenheit = celsius * 9 / 5 + 32
print(f"华氏温度：{fahrenheit:.2f}")
```

分别输入 `0`、`100`、`-40`。

然后故意输入 `abc`。此时看到 traceback 是正常的，因为还没有添加异常处理。阅读最后一行，找到 `ValueError`。

检查点：

- `raw` 是 `str`。
- `celsius` 是 `float`。
- `float(raw)` 是输入边界上的类型转换。

### 第三步：封装计算函数

把公式移动到函数中：

```python
def celsius_to_fahrenheit(value: float) -> float:
    return value * 9 / 5 + 32


raw = input("请输入摄氏温度：")
celsius = float(raw)
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"华氏温度：{fahrenheit:.2f}")
```

再次验证三个基准值。

检查点：

- 函数只负责计算，不读取输入，也不打印结果。
- 参数名 `value` 在函数内部使用。
- 调用函数时传入外部的 `celsius`。
- `return` 的值赋给 `fahrenheit`。

### 第四步：处理错误输入

在输入转换处增加：

```python
try:
    celsius = float(raw)
except ValueError:
    print("请输入数字")
```

如果只写到这里，程序在错误后可能还会继续使用未成功赋值的 `celsius`。因此错误分支必须结束当前流程。最清晰的方式是把交互放入 `main()`，然后使用 `return`：

```python
def main() -> None:
    raw = input("请输入摄氏温度：")
    try:
        celsius = float(raw)
    except ValueError:
        print("请输入数字")
        return

    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"华氏温度：{fahrenheit:.2f}")
```

检查点：

- 输入 `abc` 时只显示友好提示，不显示 traceback。
- 错误时不会继续计算。
- 正确输入仍然正常工作。

### 第五步：添加入口保护

在文件末尾加入：

```python
if __name__ == "__main__":
    main()
```

然后完成全部手工测试。

---

## 14. 完整参考实现

先自己完成上一节，再对照以下实现。不要用“看懂了”代替亲手运行。

```python
def celsius_to_fahrenheit(value: float) -> float:
    return value * 9 / 5 + 32


def main() -> None:
    raw = input("请输入摄氏温度：")
    try:
        value = float(raw)
    except ValueError:
        print("请输入数字")
        return

    fahrenheit = celsius_to_fahrenheit(value)
    print(f"华氏温度：{fahrenheit:.2f}")


if __name__ == "__main__":
    main()
```

### 14.1 逐行解释

```python
def celsius_to_fahrenheit(value: float) -> float:
```

定义一个计算函数，接收摄氏温度 `value`，预期返回浮点数。

```python
    return value * 9 / 5 + 32
```

根据公式计算华氏温度并返回。四个空格表示这行属于函数体。

```python
def main() -> None:
```

定义主流程函数。它负责输入、转换、错误处理、调用计算函数和输出。

```python
    raw = input("请输入摄氏温度：")
```

显示提示，等待用户输入，把字符串保存到 `raw`。

```python
    try:
        value = float(raw)
```

尝试把输入字符串转换为浮点数。成功后，`value` 可以参与数值运算。

```python
    except ValueError:
        print("请输入数字")
        return
```

如果转换失败，输出友好提示并立即结束 `main()`，避免继续执行计算。

```python
    fahrenheit = celsius_to_fahrenheit(value)
```

调用计算函数，把返回值保存到 `fahrenheit`。

```python
    print(f"华氏温度：{fahrenheit:.2f}")
```

使用 f-string 输出结果，并显示两位小数。

```python
if __name__ == "__main__":
    main()
```

仅在直接运行当前文件时启动主流程。

### 14.2 为什么这样拆分

输入输出和计算分离以后，核心函数可以直接验证：

```python
print(celsius_to_fahrenheit(0.0))
print(celsius_to_fahrenheit(100.0))
print(celsius_to_fahrenheit(-40.0))
```

不需要每次都模拟键盘输入。这是后续编写自动化测试的重要基础。

---

## 15. 手工测试：不仅测试“能运行”

### 15.1 测试矩阵

| 编号 | 输入 | 类型 | 预期关键输出 | 检查目的 |
|---:|---|---|---|---|
| 1 | `0` | 基准值 | `32.00` | 检查加 32 |
| 2 | `100` | 基准值 | `212.00` | 检查公式整体 |
| 3 | `-40` | 负数边界 | `-40.00` | 检查负号和公式 |
| 4 | `37.5` | 小数 | `99.50` | 检查浮点输入 |
| 5 | ` 25 ` | 带空格数字 | `77.00` | `float` 可处理首尾空白 |
| 6 | `abc` | 非数字 | `请输入数字` | 检查 `ValueError` |
| 7 | 空输入 | 非数字 | `请输入数字` | 检查空字符串 |
| 8 | `二十五` | 非数字 | `请输入数字` | 检查中文数字文本 |

### 15.2 交互式运行

```powershell
uv run python exercises\week01\day01.py
```

每次输入一个测试值，记录实际输出。

### 15.3 用管道快速重复测试

PowerShell 可以把一行文本传给程序的标准输入：

```powershell
"0" | uv run python exercises\week01\day01.py
"100" | uv run python exercises\week01\day01.py
"-40" | uv run python exercises\week01\day01.py
"abc" | uv run python exercises\week01\day01.py
```

注意：提示语和结果可能出现在同一行，这不影响测试。

### 15.4 直接验证纯函数

在仓库根目录执行：

```powershell
uv run python -c "from exercises.week01.day01 import celsius_to_fahrenheit; print(celsius_to_fahrenheit(0.0))"
```

预期输出：

```text
32.0
```

如果导入时程序立即要求输入，说明可能漏写了：

```python
if __name__ == "__main__":
    main()
```

### 15.5 可选：最小自动化断言

今天不要求正式学习 pytest，但可以先体验断言：

```powershell
uv run python -c "from exercises.week01.day01 import celsius_to_fahrenheit as convert; assert convert(0) == 32; assert convert(100) == 212; assert convert(-40) == -40; print('核心计算测试通过')"
```

全部正确时会输出：

```text
核心计算测试通过
```

如果断言不成立，会出现 `AssertionError`，说明公式或实现有误。

### 15.6 检查代码风格

```powershell
uv run ruff check exercises\week01\day01.py
```

如果没有问题，Ruff 会给出通过信息。Ruff 检查的是常见代码问题和风格，不会替你证明公式一定正确，所以它不能替代测试。

---

## 16. 常见错误与排查方法

遇到错误时，先读 traceback 的最后一行，再看它指出的文件和行号。

### 16.1 `SyntaxError: invalid character`

常见原因：使用中文括号、中文引号或其他全角标点。

错误：

```python
print（“请输入数字”）
```

修复：切换英文输入法，重新输入标点。

### 16.2 `IndentationError`

常见原因：函数体、`try`、`except` 或 `if` 下方没有正确缩进。

错误：

```python
def main() -> None:
raw = input("请输入摄氏温度：")
```

正确：

```python
def main() -> None:
    raw = input("请输入摄氏温度：")
```

统一使用四个空格，不要混用 Tab 和空格。

### 16.3 `NameError`

示例：

```text
NameError: name 'celcius' is not defined
```

检查变量拼写。`celsius` 很容易被误写成 `celcius`。Python 区分大小写，`value` 和 `Value` 也不是同一变量。

### 16.4 `TypeError`

如果错误发生在公式处，检查是否忘了执行：

```python
value = float(raw)
```

`input()` 返回字符串，不能直接参加温度公式运算。

### 16.5 `ValueError`

如果输入 `abc` 后仍出现 traceback，检查：

1. `float(raw)` 是否位于 `try` 内。
2. 是否写成了准确的 `except ValueError:`。
3. `except` 是否与对应的 `try` 处于同一缩进层级。
4. 每个冒号是否存在。

### 16.6 输出不是两位小数

检查是否准确写成：

```python
f"华氏温度：{fahrenheit:.2f}"
```

常见漏项是字符串前的 `f`，或花括号内的 `:.2f`。

### 16.7 `0` 转换结果不是 `32.00`

逐项检查：

- 是否使用 `9 / 5`，而不是 `9 // 5`。
- 是否在最后加了 `32`。
- 公式是否意外加了错误括号。
- 你实现的是“摄氏转华氏”，还是把教材里的“华氏转摄氏”公式直接抄过来了。

摄氏转华氏：

```text
F = C × 9 ÷ 5 + 32
```

华氏转摄氏：

```text
C = (F - 32) ÷ 1.8
```

方向不同，公式也不同。

### 16.8 找不到文件

如果看到类似：

```text
can't open file ...
```

先确认当前位置：

```powershell
Get-Location
```

再确认文件存在：

```powershell
Get-Item exercises\week01\day01.py
```

应当从 `D:\Agent\ai-agent-road` 运行教程中的相对路径命令。

### 16.9 程序运行后像“卡住了”

如果终端显示：

```text
请输入摄氏温度：
```

程序不是卡住，而是在等待 `input()`。输入一个值并按 Enter。

### 16.10 输入 `nan` 或 `inf`

`float("nan")` 和 `float("inf")` 在 Python 中是合法的特殊浮点值，所以基础版程序不会把它们当作格式错误。

今天的必做验收只要求对 `abc`、空输入等无法转换的文本给出提示。是否拒绝非有限数属于扩展业务规则，不要为了它阻塞今天通关。

---

## 17. 分层练习

先独立完成，再运行验证。不要只在脑中判断。

### 17.1 基础练习：预测类型和输出

写下答案后再运行：

```python
a = 10
b = 2.5
c = "10"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a + int(c))
print(c + str(a))
```

你需要解释为什么最后两行分别得到数值相加和字符串拼接。

### 17.2 基础练习：长方形面积

要求：

1. 输入长和宽。
2. 转换为 `float`。
3. 计算面积。
4. 输出两位小数。
5. 任意输入无法转换时提示“请输入数字”。

参考交互：

```text
请输入长：5
请输入宽：2.5
面积：12.50
```

### 17.3 基础练习：分钟转小时

输入总分钟数，输出“小时”和“剩余分钟”。例如 `135` 输出 `2 小时 15 分钟`。

提示：

```python
hours = total_minutes // 60
minutes = total_minutes % 60
```

这个练习用于体会 `/`、`//` 和 `%` 的不同用途。

### 17.4 进阶练习：反向温度转换

实现：

```python
def fahrenheit_to_celsius(value: float) -> float:
    ...
```

公式：

```text
摄氏度 = (华氏度 - 32) × 5 ÷ 9
```

至少验证：

```text
32 -> 0.00
212 -> 100.00
-40 -> -40.00
```

### 17.5 进阶练习：拒绝非有限数

这是可选练习。使用标准库 `math`：

```python
import math

if not math.isfinite(value):
    print("请输入有限数字")
    return
```

加入后验证 `nan`、`inf`、`-inf`。完成时要能解释：这是额外业务校验，不是 `float()` 转换失败。

### 17.6 挑战练习：不要复制核心公式

让程序同时输出摄氏度、华氏度和开尔文温度，但每个转换规则都放在单独函数中。要求主流程只负责组织输入输出。

开尔文公式：

```text
K = C + 273.15
```

注意：真实物理意义上，低于绝对零度的输入应被拒绝。你需要自己确定校验条件和提示语。

---

## 18. 闭卷重写挑战

完成项目和测试后，休息 10 分钟，然后进行闭卷重写。

### 18.1 操作方法

1. 关闭这份教程和参考代码。
2. 把原文件临时重命名为 `day01_reference.py`。
3. 新建空的 `day01.py`。
4. 设置 20 分钟计时器。
5. 根据下面的需求从零实现。

需求：

```text
读取摄氏温度
转换为 float
转换失败时输出“请输入数字”
按 F = C × 9 ÷ 5 + 32 计算
结果保留两位小数
计算逻辑必须放在函数中
直接运行文件时调用 main()
```

### 18.2 完成后验证

```powershell
"0" | uv run python exercises\week01\day01.py
"100" | uv run python exercises\week01\day01.py
"-40" | uv run python exercises\week01\day01.py
"abc" | uv run python exercises\week01\day01.py
uv run ruff check exercises\week01\day01.py
```

### 18.3 重写失败时怎么处理

不要立刻复制参考答案。先判断卡点属于哪一类：

| 卡点 | 应复习的小节 |
|---|---|
| 忘记运行命令 | 第 3、4 节 |
| 输入后无法计算 | 第 6、7 节 |
| 公式错误 | 第 8 节 |
| 两位小数写不出 | 第 9 节 |
| 函数不会写 | 第 10 节 |
| `abc` 会崩溃 | 第 11 节 |
| 导入时要求输入 | 第 12 节 |

只看对应小节，随后再次从空白处写。第二次仍失败，就把失败原因记录到当天笔记。

---

## 19. 必须能口头解释的知识点

不要背定义，用自己的话回答。

### 19.1 `float` 是什么

合格解释应包含：

- `float` 是 Python 的浮点数类型，可表示带小数的数值。
- `float(raw)` 在本程序中负责把输入字符串转换成可计算的数字。
- 如果字符串不能表示数字，会产生 `ValueError`。

### 19.2 `return` 是什么

合格解释应包含：

- `return` 把函数的计算结果交还给调用者。
- 执行 `return` 后，本次函数调用结束。
- `return` 和把内容显示到终端的 `print()` 不同。

### 19.3 `:.2f` 是什么

合格解释应包含：

- 它是 f-string 中的格式说明。
- `.2` 表示小数点后显示两位。
- `f` 表示定点浮点数格式。
- 它主要改变显示形式，不等于修改原始变量的底层值。

### 19.4 为什么要捕获 `ValueError`

因为用户输入不可完全信任。无法转换的文本是命令行程序中可预期的失败，程序应该给出清楚提示，而不是直接显示长 traceback。

### 19.5 为什么计算函数中不写 `input()`

把纯计算和用户交互分离后：

- 公式更容易重复使用。
- 不需要键盘输入就能测试。
- 后续改成 Web API 时可以继续复用计算函数。

---

## 20. 当天笔记模板

在 `notes\week01_day01.md` 中填写：

```markdown
# Week 01 Day 01 学习记录

## 今天完成了什么

- 

## 我现在能独立解释什么

- 变量：
- int、float、str、bool：
- input()：
- float()：
- return：
- :.2f：
- try / except ValueError：

## 测试结果

| 输入 | 预期 | 实际 | 是否通过 |
|---|---|---|---|
| 0 | 32.00 |  |  |
| 100 | 212.00 |  |  |
| -40 | -40.00 |  |  |
| abc | 请输入数字 |  |  |
| 空输入 | 请输入数字 |  |  |

## 今天遇到的错误

错误信息：

原因：

修复方法：

我下次如何更快定位：

## 闭卷重写

- 用时：
- 是否在 20 分钟内完成：
- 卡住的位置：
- 需要补的知识：
```

不要只写“今天学会了 Python 基础”。笔记要能帮助未来的你重现错误和解决方法。

---

## 21. Git 提交

### 21.1 提交前检查

```powershell
cd D:\Agent\ai-agent-road
git status
uv run ruff check exercises\week01\day01.py
uv run pytest -q
```

`pytest` 当前主要验证项目环境。今天的手工测试结果应记录在笔记中。

确认没有把 `.env`、`.venv` 或真实密钥加入提交。

### 21.2 查看本次要提交的内容

```powershell
git diff
git status --short
```

你应该理解将要提交的每个文件。

### 21.3 创建提交

```powershell
git add exercises\week01\day01.py notes\week01_day01.md
git commit -m "feat: 完成摄氏温度转换器"
```

提交信息说明“完成了什么能力”，比 `update`、`test`、`day1` 更清楚。

### 21.4 验证提交

```powershell
git status
git log -1 --oneline
```

理想状态是工作区干净，并能看到刚才的提交。

---

## 22. 最终验收清单

以下项目全部完成后，第一周第一天才算通关。

### 代码

- [ ] 文件位于 `exercises\week01\day01.py`。
- [ ] 使用 `celsius_to_fahrenheit()` 封装计算公式。
- [ ] 函数参数和返回值有 `float` 类型标注。
- [ ] 使用 `main()` 组织输入输出。
- [ ] 使用 `if __name__ == "__main__":` 启动主流程。
- [ ] 没有把 `input`、`float`、`print` 等内置名称当变量。

### 行为

- [ ] 输入 `0`，输出包含 `32.00`。
- [ ] 输入 `100`，输出包含 `212.00`。
- [ ] 输入 `-40`，输出包含 `-40.00`。
- [ ] 输入小数可以正确计算。
- [ ] 输入 `abc` 时提示“请输入数字”。
- [ ] 错误输入不显示 traceback。

### 理解

- [ ] 能解释 `input()` 为什么返回 `str`。
- [ ] 能解释 `float()` 的作用和失败方式。
- [ ] 能解释 `/` 与 `//` 的区别。
- [ ] 能解释 `return` 与 `print()` 的区别。
- [ ] 能解释 `:.2f` 的每一部分。
- [ ] 能解释为什么计算函数和交互流程要分开。

### 工程习惯

- [ ] `uv run ruff check exercises\week01\day01.py` 通过。
- [ ] 项目原有测试通过。
- [ ] 完成 `notes\week01_day01.md`。
- [ ] 创建了一次有意义的 Git 提交。
- [ ] 能在 20 分钟内闭卷重写。

只要“看过”或“看懂”不算通关。必须有代码、运行结果、失败输入、笔记和提交记录。

---

## 23. 一页速查表

```python
# 变量与基础类型
count = 10              # int
temperature = 25.5     # float
message = "你好"        # str
is_valid = True        # bool

# 检查类型
print(type(temperature))

# 输入永远先得到字符串
raw = input("请输入：")

# 类型转换，失败时可能产生 ValueError
value = float(raw)

# 算术
result = value * 9 / 5 + 32

# 两位小数输出
print(f"结果：{result:.2f}")

# 函数和返回值
def convert(value: float) -> float:
    return value * 9 / 5 + 32


# 处理可预期的转换失败
try:
    value = float(raw)
except ValueError:
    print("请输入数字")

# 直接运行文件时启动主流程
if __name__ == "__main__":
    main()
```

---

## 24. 参考资料与阅读边界

今天只阅读与当前任务直接相关的部分：

1. [Python-100-Days：Day01-20 目录](https://github.com/jackfrued/Python-100-Days/tree/master/Day01-20)
2. [01. 初识 Python](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-20/01.%E5%88%9D%E8%AF%86Python.md)：了解 Python 和解释器；本机环境已完成，不重新安装。
3. [02. 第一个 Python 程序](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-20/02.%E7%AC%AC%E4%B8%80%E4%B8%AAPython%E7%A8%8B%E5%BA%8F.md)：关注 `.py` 文件、`print()` 和运行程序。
4. [03. Python 语言中的变量](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-20/03.Python%E8%AF%AD%E8%A8%80%E4%B8%AD%E7%9A%84%E5%8F%98%E9%87%8F.md)：关注变量、类型、命名、`type()` 和类型转换。
5. [04. Python 语言中的运算符](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-20/04.Python%E8%AF%AD%E8%A8%80%E4%B8%AD%E7%9A%84%E8%BF%90%E7%AE%97%E7%AC%A6.md)：关注算术、赋值、优先级、输入和温度转换示例。
6. [Python 3.11 官方教程：Python 速览](https://docs.python.org/zh-cn/3.11/tutorial/introduction.html)：补充数字、字符串和基础表达式。
7. [Python 3.11 官方教程：输入与输出](https://docs.python.org/zh-cn/3.11/tutorial/inputoutput.html)：重点看 f-string 和格式说明。
8. [Python 3.11 官方教程：错误和异常](https://docs.python.org/zh-cn/3.11/tutorial/errors.html)：重点看 `try` / `except` 和 `ValueError`。

今天暂时不要扩展到列表、字典、循环、类、第三方包或 Web 框架。这些内容会在后续 Day 中逐步加入。今天真正重要的是把最小的数据流写正确，并能够独立重建。
