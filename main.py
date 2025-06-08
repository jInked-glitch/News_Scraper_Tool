# ニュースページにアクセスして、記事のタイトルとリンクを集めて、CSVに保存する。

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Hacker Newsページ
url = "https://news.ycombinator.com/"
headers = {"User-Agent": "Mozilla/5.0"}

# === スクレイピングページ取得 ===
# ページ取得
response = requests.get(url, headers=headers)
# HTMLの中身を解析 ページを読み取れる形に変換
soup = BeautifulSoup(response.content, "html.parser")

# === スクレイピング対象の抽出 ===
# 見出しの抽出
articles = []

# 記事リンクを探す
# <a> タグで1記事のブロックを取得
for tag in soup.find_all("span", class_="titleline"):
    a_tag = tag.find("a", href=True)
    if a_tag:
        # タイトルの文字だけを抜き出す
        title = a_tag.get_text(strip=True)
        # リンク先情報を取り出す URLリンクを取得
        link = a_tag["href"]
        articles.append({
            "title": title,
            "url": link,
            "summary": "",  # Hacker Newsにはsummaryがないため空欄
            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

# === CSVに保存 ===
# タイトル・URL・取得時間を記録
filename = f"hacker_news_{datetime.now().strftime('%Y%m%d')}.csv"
with open(filename, mode="w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "url", "summary", "scraped_at"])
    writer.writeheader()
    for article in articles[:10]:  # 最初の10件だけ
        writer.writerow(article)

print(f"✅ Saved {len(articles[:10])} articles to {filename}")
