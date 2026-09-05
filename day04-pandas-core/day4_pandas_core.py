import pandas as pd

# ========== 读取数据 ==========
chapters = pd.read_csv(r"D:\mycode\ai-data-learning\day04-pandas-core\novel_chapters.csv", encoding="utf-8-sig")
categories = pd.read_csv(r"D:\mycode\ai-data-learning\day04-pandas-core\category_info.csv", encoding="utf-8-sig")

print("=== 章节表 ===")
print(chapters.head())
print("\n=== 分类表 ===")
print(categories)

# ========== 1. dropna（删空值）==========
print("\n=== 1. dropna ===")
chapters_clean = chapters.dropna(subset=["书名", "章节号", "章节名", "分类", "字数", "更新日期"])
print("去空后形状:", chapters_clean.shape)

# ========== 2. fillna（填空值）==========
print("\n=== 2. fillna ===")
# 假设"字数"有空值，用平均值填充
if chapters["字数"].isnull().sum() > 0:
    avg_words = chapters["字数"].mean()
    chapters["字数"] = chapters["字数"].fillna(avg_words)
    print("已用平均值", avg_words, "填充字数空值")
else:
    print("字数列没有空值，用模拟演示：")
    # 复制一列来演示
    chapters["字数_fill"] = chapters["字数"].fillna(chapters["字数"].mean())
    print(chapters[["书名", "字数", "字数_fill"]].head())

# ========== 3. drop_duplicates（去重）==========
print("\n=== 3. drop_duplicates ===")
before = len(chapters_clean)
chapters_clean = chapters_clean.drop_duplicates(subset=["书名", "章节号"])
after = len(chapters_clean)
print(f"去重前 {before} 行，去重后 {after} 行")

# ========== 4. merge（合并）==========
print("\n=== 4. merge ===")
# 把章节表和分类信息表按"分类"列合并
merged = pd.merge(chapters_clean, categories, on="分类", how="left")
print(merged[["书名", "章节名", "分类", "评分", "标签"]].head(10))

# ========== 5. groupby + agg（分组统计）==========
print("\n=== 5. groupby + agg ===")
group_result = merged.groupby("分类").agg(
    章节数=("章节名", "count"),
    总字数=("字数", "sum"),
    平均字数=("字数", "mean"),
    最大字数=("字数", "max"),
    最小字数=("字数", "min")
).reset_index()
print(group_result)

# ========== 6. 字符串 str.contains（条件筛选）==========
print("\n=== 6. str.contains ===")
# 筛选章节名包含"醒来"或"觉醒"的
mask = merged["章节名"].str.contains("醒来|觉醒", na=False)
awaken = merged[mask]
print("包含'醒来'或'觉醒'的章节：")
print(awaken[["书名", "章节名", "分类"]])

# 额外练习：筛选评分 >= 9 的分类
high_score = merged[merged["评分"] >= 9]
print("\n评分 >= 9 的章节：")
print(high_score[["书名", "章节名", "分类", "评分"]])

# ========== 保存合并结果 ==========
output = r"D:\mycode\ai-data-learning\day04-pandas-core\novel_with_category.csv"
merged.to_csv(output, index=False, encoding="utf-8-sig")
print("\n已保存合并结果:", output)