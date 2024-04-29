import openpyxl

wb = openpyxl.load_workbook("details.xlsx")
print(wb.sheetnames)
