import pandas as pd

# CSVを読み込む
df = pd.read_csv("data/sample_sales.csv")

# 日付列をdatetime型に変換
df["date"] = pd.to_datetime(df["date"])

# =========
# 日別集計
# =========
daily_sales = (
    df.groupby("date")["sales"]
    .sum()
    .reset_index()
)

# =========
# 月別集計
# =========
df["month"] = df["date"].dt.to_period("M")

monthly_sales = (
    df.groupby("month")["sales"]
    .sum()
    .reset_index()
)

# 結果を表示
print("▼ 日別売上")
print(daily_sales)

print("\n▼ 月別売上")
print(monthly_sales)

# CSVとして保存
daily_sales.to_csv("output/daily_sales.csv", index=False)
monthly_sales.to_csv("output/monthly_sales.csv", index=False)
