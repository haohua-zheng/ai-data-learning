# 导入 pandas 库，起个别名叫 pd（行业惯例）
import pandas as pd

# 读取 CSV 文件
# 注意：把路径改成你自己的实际路径
file = r"D:\mycode\ai-data-learning\day03-csv\novel_chapters.csv"

df = pd.read_csv(file,encoding="utf-8")

# 1. 看前 5 行
print("=== 前 5 行 ===")
print(df.head())

# 2. 看表格基本信息（行数、列数、每列数据类型、非空值数量）
print("\n=== 基本信息 ===")
print(df.info())

# 3. 数空值：每列有多少个空值
print("\n=== 每列空值数量 ===")
print(df.isnull().sum())

# 4. 看表格形状（多少行、多少列）
print("\n=== 形状 ===")
print(df.shape)

# 5. 看统计摘要（数值列的平均值、最大值、最小值等）
print("\n=== 统计摘要 ===")
print(df.describe())

# 6. 删空值：删除任何有空值的行，得到新表
df_clean = df.dropna()

print("\n=== 删空值后形状 ===")
print(df_clean.shape)

# 7. 去重：删除完全重复的行
df_clean = df_clean.drop_duplicates()

print("\n=== 去重后形状 ===")
print(df_clean.shape)

# 8. 保存清洗后的数据为新 CSV
output = r"D:\mycode\ai-data-learning\day03-csv\novel_chapters_clean.csv"
df_clean.to_csv(output, index=False, encoding="utf-8-sig")

print("\n=== 清洗完成，已保存 ===")
print(output)