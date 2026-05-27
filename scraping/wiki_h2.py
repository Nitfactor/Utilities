"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests
from bs4 import BeautifulSoup

url = "https://website-eta-self-23.vercel.app/"

def get_h1_headers(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch the page due to: {e}")
        return[]

    soup = BeautifulSoup(response.text, "html.parser")
    h1_tags = soup.find_all("h1")
    headers = []
    for tag in h1_tags:
        header_text = tag.get_text(strip=True)
        if header_text and header_text.lower() != "contents":
            headers.append(header_text)
    print(headers)
get_h1_headers(url)