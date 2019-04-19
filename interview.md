# python 
-  高级语言，解释型脚本语言
   - 语言分高级和低级，低级语言是指计算机直接能执行的程序，高级语言指需要要通过编译或者翻译成低级语言的语言。 
   - （举例，a=3+4）
```mermaid
graph LR;
    词法分析-->语法分析;
    语法分析-->语义分析;
    语义分析-->中间代码生成;
    中间代码生成-->代码优化;
    代码优化-->目标代码生成;
```
```mermaid
graph LR;
3-->+;
4-->+;
+-->=;
=-->a;

```

   - 写python代码两种方式：1.交互环境中，python shell 2.编写成脚本，指定名称运行
![avatar](/photo/pythonshell.jpg)
   - 现代计算机结构都是参考了冯诺依曼结构：1. 运算器 2. 控制器 3. 存储器 4. 输入 5. 输出。

## 示例代码
```python
q=PriorityQueue()
n=input("请输入元素个数:\n")
n=int(n)
for i in range(n):
    name=str(input("请输入元素名称:\n"))
    prio=int(input("请输入优先值\n"))
    q.push(Item(name),prio)
for i in range(n):
    print(q.pop())
```