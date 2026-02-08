import pandas as pd

#csvを読み込む(pandas の DataFrame にデータを載せる)
df = pd.read_csv("data/sample_sales.csv")
#中身を５行確認
print("=== Raw Data ===")
print(df.head())

# 2. Data cleaning / formatting
# Convert date column to datetime
#日付列をdatatimeに変換
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

print("\n=== Cleaned Data ===")
print(df.head())

# =========
# 日別集計
# =========

daily_sales =(
    df.groupby("data")["sales"].sum().reset_index()
    )
# =========
# 月別集計
# =========
df["month"]= df["data"].dt.to_period("M")
monthly_sales=(
    df.groupby("month")["sales"].sum().reset_index()
)
# 結果を表示
#show result
print("▼ 日別売上")
print(daily_sales)

print("\n▼ 月別売上")
print(monthly_sales)

# CSVとして保存
#save to CSV
daily_sales.to_csv("output/daily_sales.csv", index=False)
monthly_sales.to_csv("output/monthly_sales.csv", index=False)