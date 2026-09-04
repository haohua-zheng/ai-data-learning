import pandas as pd

file = r"D:\mycode\ai-data-learning\day2-excel\小说章节表.xlsx"

df = pd.read_excel(file, sheet_name="Sheet1", engine="openpyxl")

print("列名:", df.columns.tolist())
print("\n前几行:")
print(df.head())

print("\n总字数:", df["字数"].sum())

print("\n历史分类平均字数:")
hist = df.loc[df["分类"] == "历史", "字数"]
print(hist.mean())

print("\n按分类统计:")
print(df.groupby("分类")["字数"].agg(["count", "sum", "mean"]))

print("\n按书名汇总总字数:")
print(df.groupby("书名")["字数"].sum().sort_values(ascending=False))