import xlwings as xw

app = xw.App(visible = True, add_book = False)
workbook = app.books.add()
worksheet = workbook.sheets.add('书单')
worksheet.range('A1').value = '编号'
workbook.save('amzaon.xlsx')
workbook.close()
app.quit()
