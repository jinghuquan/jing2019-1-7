### xlsxwriter库的安装

> pip install xlsxwriter

#### 1、创建一个Excel文件

```python
work = xlsxwriter.Workbook("1.xlsx")
```

#### 2、创建表格

```python
worksheet = work.add_worksheet("Json")
```

#### 3、修改内容样式

- 表格样式

  ```python
  worksheet.set_column("A:A",20)
  ```

- 内容样式(我们这里设置了一个字体加粗)

  ```python
  bold =work.add_format({"bold":True})
  ```

#### 4、写入内容

- 写入字符

  ```python
  worksheet.write("A1","Json",bold)
  ```

- 写入图片

  ```python
  worksheet.insert_image("A2","1.jpg")
  ```

- 写入函数

  ```python
  worksheet.write("A3",2,bold)
  worksheet.write("A4",64,bold)
  worksheet.write("A5","=SUM(A3:A4)",bold)
  ```

#### 5、创建图表

```python
chart = work.add_chart({'type':'column'})
```

PS：

- column         柱状图
- area              面积图
- bar                条形图
- line                折线图
- radar              雷达图

#### 6、声明一个容器：

```python
title = "abcdefghi"
data = [1,21,3,2,12,13,14,112,156]

for i,j in enumerate(title):
    print(i,j)
    point = "A%d"%(i+1)
    worksheet.write_string(point,j)
    
for i,j in enumerate(data):
    point = "B%d"%(i+1)
    worksheet.write(point,j)
```

#### 7、为图标添加数据

```python
chart.add_series(
        {
            "categories":"=Sheet1!$a$1:$a$9",#类别标签的范围
            "values":"=Sheet1!$b$1:$b$9",#图标数据的范围
            "line":{"color":"red"}#图标线条的属性
        }
    )
worksheet.insert_chart("A10",chart)
```

#### 8、关闭并保存Excel

```python
work.close()
```





