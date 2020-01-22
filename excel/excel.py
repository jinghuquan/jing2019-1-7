import xlsxwriter

# 创建一个excel文件
work = xlsxwriter.Workbook("1.xlsx")
# 创建表格
worksheet = work.add_worksheet("for")
worksheet1 = work.add_worksheet("jack")
# 修改样式
     # 修改表格样式
worksheet.set_column("A:F",20)
     # 修改内容样式
bold = work.add_format({"bold":True})
# 写入内容
     # 1写入字符
worksheet.write("A1","hello",bold)
worksheet1.write("A1","python")
     # 2写入图片
# worksheet.insert_image("A2","1.jpg")
     # 写入函数
worksheet.write("B3",56,bold)
worksheet.write("B4",78,bold)
worksheet.write("B5","=SUM(B3:B4)")



work.close()