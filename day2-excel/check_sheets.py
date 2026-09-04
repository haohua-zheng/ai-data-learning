import pandas as pd

file = r"D:\mycode\ai-data-learning\day2-excel\小说章节表.xlsx"

xls = pd.ExcelFile(file, engine="openpyxl")
print("Sheet列表:", xls.sheet_names)