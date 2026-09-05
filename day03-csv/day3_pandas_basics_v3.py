import pandas as pd

file = r"D:\mycode\ai-data-learning\day03-csv\novel_chapters.csv"

df = pd.read_csv(file, encoding="utf-8-sig")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.shape)

print("=== 统计摘要 ===")
print(df.describe())

df_drop_all = df.dropna().drop_duplicates()
print("删空值后形状：", df_drop_all.shape)

key_cols = ["书名", "章节号", "章节名", "分类", "字数", "更新日期"]
df_key_clean = df.dropna(subset=key_cols).drop_duplicates()
print("按关键列去空后形状：", df_key_clean.shape)

df_drop_all.to_csv(
    r"D:\mycode\ai-data-learning\day03-csv\novel_chapters_clean_dropall.csv",
    index=False,
    encoding="utf-8-sig"
)

df_key_clean.to_csv(
    r"D:\mycode\ai-data-learning\day03-csv\novel_chapters_clean_core.csv",
    index=False,
    encoding="utf-8-sig"
)

print("已保存两个清洗结果文件")