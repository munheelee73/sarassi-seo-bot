
import requests
from bs4 import BeautifulSoup

def get_post_list(blog_url, max_pages=5):
    post_links = []
    for page in range(1, max_pages + 1):
        res = requests.get(f"{blog_url}/page/{page}")
        soup = BeautifulSoup(res.text, "html.parser")
        for link in soup.select("a"):
            href = link.get("href")
            if href and "/entry/" in href:
                post_links.append(href)
    return list(set(post_links))
