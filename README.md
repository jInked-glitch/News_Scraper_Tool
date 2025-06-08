📰 News Scraper Tool
A lightweight Python script that scrapes the latest headlines from a news website and saves them in a neatly formatted CSV file — perfect for learning web scraping and data handling basics.

🎬 New Features (as of 8 June 2025)
✨ This version includes:

🔍 Headline Extraction: Automatically scrapes the top article titles and links from Hacker News.

📄 CSV Export: Saves results with timestamp to news_YYYYMMDD.csv for easy data tracking.

🕒 Datetime Stamping: Each article is tagged with the exact time it was scraped.

🌐 Link Handling: Resolves relative URLs into complete clickable links.

📑 Article Summary (optional): Some news sources may include short descriptions (if available).

⚙️ How It Works
The script fetches the target news page using requests.

Parses HTML with BeautifulSoup.

Finds article blocks and extracts:

title

URL

scraped_at timestamp

summary (if provided by the site)

Outputs all collected info into a CSV file with today’s date.

🛠 Technologies Used
Python 3.x

requests (for HTTP requests)

BeautifulSoup (bs4, for HTML parsing)

csv and datetime (Python standard libraries)

📁 Project Structure
graphql
コピーする
編集する
news_scraper/
├── main.py           # Entry point and scraping logic
├── news_YYYYMMDD.csv # Output CSV file (auto-generated)
└── README.md
🧠 Learning Goals
This beginner-friendly project reinforces key Python concepts:

Web scraping basics (requests + BeautifulSoup)

HTML element parsing

CSV file handling

Date/time formatting

Clean script structuring

🚀 Next Steps
🔧 Planned Upgrades:

Switch between different news sources (BBC, Reuters, etc.)

Automatically detect structure for multiple sites

Add keyword filtering (e.g., tech, finance, etc.)

Create a GUI or CLI menu for scraping options

Connect to Google Sheets for cloud-based results

✨ Special Thanks
Inspired by the “100 Days of Code” Python Bootcamp on Udemy.
This tool is part of my journey to become a Python programmer who can create useful automation scripts and handle real-world data.

🧑‍💻 Author
jInked-glitch
Based in France — marathon runner & passionate Python learner
GitHub: jInked-glitch
