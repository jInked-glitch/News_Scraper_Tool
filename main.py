import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://news.ycombinator.com/"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

articles = []

for tag in soup.find_all("span", class_="titleline"):
    a_tag = tag.find("a", href=True)
    if a_tag:
        title = a_tag.get_text(strip=True)
        link = a_tag["href"]
        articles.append({
            "title": title,
            "url": link,
            "summary": "",  # Hacker Newsにはsummaryがないため空欄
            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

# CSV保存
filename = f"hacker_news_{datetime.now().strftime('%Y%m%d')}.csv"
with open(filename, mode="w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "url", "summary", "scraped_at"])
    writer.writeheader()
    for article in articles[:10]:  # 最初の10件だけ
        writer.writerow(article)

print(f"✅ Saved {len(articles[:10])} articles to {filename}")



