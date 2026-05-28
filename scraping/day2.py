"""
 Challenge: Hacker News Top Posts Scraper

Build a Python script that:
1. Fetches the HN homepage (news.ycombinator.com).
2. Extracts the top 20 post titles and URLs.
3. Saves the results into a CSV file (`hn_top20.csv`) with columns:
   - Title
   - URL
4. Handles network errors and uses a clean CSV structure.
"""
import requests
import csv
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

def hacker_news(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request cannot be processed: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    get_links = soup.select("span.titleline > a")
    # print(get_links)

    post = []
    for link in get_links[:20]:
        title = link.text.strip()
        url = link.get("href").strip()
        print(f"\n Title: {title}\n url: {url}\n")

hacker_news(url)
    