import xlrd
import xlwt

excel = xlrd.open_workbook("Mann Whitney U Test Analysis_ Emma Update 3.xlsx")


sheet = excel.sheets()[1]
# unit = sheet.row_values(2)
# print(unit)

row_index = []
wb = xlwt.Workbook()
w_conv = wb.add_sheet("convincing")
w_nonconv = wb.add_sheet("non_convincing")
row = 0
for i in range(0,32,2):
    #if i = 3 + 3 * n
    rows = 2 + 3 * i
    row_content = sheet.row_values(rows)
    print(len(row_content))
    for j in range(0,len(row_content)):
        w_conv.write(row, j, row_content[j])
    row += 1

row = 0
for i in range(1,32,2):
    #if i = 3 + 3 * n
    rows = 2 + 3 * i
    row_content = sheet.row_values(rows)
    print(len(row_content))
    for j in range(0,len(row_content)):
        w_nonconv.write(row, j, row_content[j])
    row += 1
#print(row_content[0])
#
# col_index = [0, 94]
# wb = xlwt.Workbook()
# ws = wb.add_sheet("Testing")
# for n in range(0,32):
#     ws.write(n, row_content[n])
wb.save("Con&Non-con.xls")

