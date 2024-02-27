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

1. 关闭所有页面，重新打开浏览器，登录选课系统；

2. 随意选择一门未满课程，页面空白处右键选择检查或者F12打开开发者模式，选择`网络`，如下图所示。

  ![image](https://github.com/KW10-2/Gadgets/assets/150025813/859caa19-1842-4b35-9174-31f5c3ce5dba)


3. 点击`选择`并确认选课，此时会出现名为`volunteer.do`的请求，复制为cURL(bash)；

![image](https://github.com/KW10-2/Gadgets/assets/150025813/4d145047-7f0f-4139-9d8b-43dd0093fdc9)

4. 转到[Convert curl commands to code (curlconverter.com)](https://curlconverter.com/)网站，输入复制的cURL(bash)，转换为`python`代码，复制`cookies`，`headers`和`datas`的定义部分（示例如下）；
```{python}
cookies = {
    '_WEU': '8pxZlxmJmMTOS5a_QdJv_DmqNS4wzk37ie__vWlm54v9DG7_auhK9VGjzW5CQnjM',
    'JSESSIONID': 'C6499BFC6EF72DDDE086CAAD16BC1437',
    'iPlanetDirectoryPro': '7cus1fKdzbF7CTHNz4dgP2',
    'route': '988e192a8228227f3b6a6f17b66684c8',
    'user_id': '"211850047 1709013890070"',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': '_WEU=8pxZlxmJmMTOS5a_QdJv_DmqNS4wzk37ie__vWlm54v9DG7_auhK9VGjzW5CQnjM; JSESSIONID=C6499BFC6EF72DDDE086CAAD16BC1437; iPlanetDirectoryPro=7cus1fKdzbF7CTHNz4dgP2; route=988e192a8228227f3b6a6f17b66684c8; user_id="211850047 1709013890070"',
    'Origin': 'https://xk.nju.edu.cn',
    'Referer': 'https://xk.nju.edu.cn/xsxkapp/sys/xsxkapp/*default/grablessons.do?token=55a5c782-50b4-453a-b238-e75d03c75a05',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'language': 'zh_cn',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="123", "Google Chrome";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'token': '55a5c782-50b4-453a-b238-e75d03c75a05',
}

data = {
    'addParam': '{"data":{"operationType":"1","studentCode":"211850047","electiveBatchCode":"20232fb12e074bea91ad9a838255598a","teachingClassId":"2023202423000015001","courseKind":"12","teachingClassType":"KZY"}}',
}

```
5. 下载`CoursePyGar.py`,用`python`开发环境（如`spyder`）打开`CoursePyGar.py`，将从curlconverter.com复制的代码粘贴至`#(paste and correct codes here)`中；

6. 修改变量`data`中的`teachingClassId`为目标课程ID（仅需改变课程号，如“2023202420030016002”中仅需将“00310820”修改为目标课程号）；

7. 调整循环中的`time.sleep(10)`休眠时间，运行所有代码即可。显示“该课程超过课容量”即为正常情况，如下，可能需要运行1~4h才能选到，视运气而定。选课成功后会退出循化，结束脚本运行。
![image](https://github.com/KW10-2/Gadgets/assets/150025813/89acc8da-7759-400e-8ce5-440a8f3bb729)
![image](https://github.com/KW10-2/Gadgets/assets/150025813/5118ba8b-4454-429f-a4df-a3df1af77bd0)


> 注意：
> 若发生异常（如非法请求等），重登系统，替换cookies和headers重新尝试；
> 
> 记得退掉第2步选择的未满课程；
> 
> 可以并行运行多个脚本，`spyder`中只需打开多个控制台即可。
> 
> 若显示**“教学班不在开放选课轮次中”**，可尝试将`teachingClassId`结尾的“02”改为“01”（反之亦然）进行尝试。       
