import pandas as pd
import matplotlib.pyplot as plt

#-----------
#CSVファイルをロード/Load CSV file
#-----------
df =pd.read_csv("data/sample_sales.csv")

df["data"]=pd.to_datetime(df["data"])

#-----------
#日経表作成/Create Daily Summary
#-----------
#Group by data and calculate to sales per day
daily_sales=(
    df.groupby("data")["sales"].sum().reset_index()
)

#-----------
#月間表/Create Month Summary 
#-----------
#月と日のカラムを作製/Create month and daily column
df["month"] = df["date"].dt.to_period("M")
#Group by month and calculate  total sales per month
monthly_sales=(
    df.groupby("month")["sales"]
.sum().reset_index()
)
#グラフ描画のため"month"を文字列化している
monthly_sales["month"]= monthly_sales["month"].astype(str)


# ==========================
# Visualization - Daily Sales
# ==========================
#新しいグラフを作成
plt.figure()
#折れ線グラフを描画,X=Daily,y=Monhty
plt.plot(daily_sales["date"], daily_sales["sales"])
#グラフのタイトル
plt.title("Daily Sales")
#横ラベルを設定
plt.xlabel("Date")
plt.ylabel("Total Sales")
#日付を45回転させる
plt.xticks(rotation=45)
#レイアウトを自動修正する・ラベルが切れないようにする
plt.tight_layout()
#画像ファイルとして保存する
plt.savefig("output/daily_sales.png")
#メモリ解放して次のグラフと重ならないようにする
plt.close()

# ==========================
# Visualization - Monthly Sales
# ==========================
#新しいグラフを作成
plt.figure()
#棒グラフにしている
plt.bar(monthly_sales["month"], monthly_sales["sales"])
#タイトル設定
plt.title("Monthly Sales")
#横ラベルを設定
plt.xlabel("Month")
plt.ylabel("Total Sales")
#日付を45回転させる
plt.xticks(rotation=45)
#レイアウトを自動修正する・ラベルが切れないようにする
plt.tight_layout()
#画像ファイルとして保存する
plt.savefig("output/monthly_sales.png")
#メモリ解放して次のグラフと重ならないようにする
plt.close()
#処理完了メッセージを出力
print("Report generated successfully!")