## 使用说明
1. 主要参考视频：https://www.bilibili.com/video/BV1nG4y1K7XL/?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click&vd_source=ce3ea329f5c76cda87f230189d3b05a9
2. 适用对象：课程补选（主要是在补选开始没有抢到课时的“捡漏”，补选刚开始时抢课未测试，理论可行，但不建议）
3. 使用步骤：
（1）登录选课系统
（2）F12打开开发者模式/检查（监视网络）【或右键->检查】，选择A课程或同类课程
（3）选择“name”栏的volunteer.do-->copy(cURL(bash))
（4）在https://curlconverter.com将cURL转换为py代码（py0）
（5）若为A的同类课程，需将py0中data的"teachingClassId"（如"2023202410036009001"）改为相应值（只需改课程号部分，即00360090）。
（6）将`CoursePyGar.py`的`cookies`、`headers`和`data`替换为py0
（7）Run
（8）若异常（非法请求等），重登系统，替换cookies和headers即可
（9）可同时运行多个程序（合理设置sleep，如7个程序可设置>21s）

> 注意：
>
> 适当控制休眠时间`sleep`，不可设置过短，以免对选课系统造成过大压力，届时责任自负！

## 使用方法更新(2024.02.26)

由于本次选课系统隐藏了已满课程的`选择`按钮，因此进行使用方法简单更新：

1. 登录选课系统

2. 随意选择一门未满课程，页面空白处右键选择检查或者F12打开开发者模式，选择`网络`，如下图所示。

   ![image-20240226173139648](C:/Users/lvjih/.config/joplin-desktop/image-20240226173139648.png)

3. 点击`选择`并确认选课，此时会出现名为`volunteer.do`的请求，复制为cURL(bash)；

   ![image-20240226173402173](C:/Users/lvjih/.config/joplin-desktop/image-20240226173402173.png)

4. 转到[Convert curl commands to code (curlconverter.com)](https://curlconverter.com/)网站，输入复制的cURL(bash)，转换为`python`代码，复制到剪切板；

5. 用`python`开发环境（如`spyder`）打开CoursePyGar.py，将复制的代码粘贴至`import time`后面，修改变量`data`中的`teachingClassId`为目标课程ID（仅需改变课程号，如“2023202420030016002”中仅需将“00310820”修改为目标课程号），删除`response `变量定义；

6. 调整循环中的`time.sleep(10)`休眠时间，运行所有代码即可。

> 注意：若发生异常（如非法请求等），重登系统，替换cookies和headers重新尝试。
