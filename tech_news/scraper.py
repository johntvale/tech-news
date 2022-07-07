import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = selector.css("h2.entry-title a::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_btn = selector.css("div.nav-links a.next::attr(href)").get()
    return next_page_btn


def remove_tags_html(text_with_tags):
    text = BeautifulSoup(text_with_tags, "lxml").get_text()
    return text


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    base_url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()

    comments = selector.css("ol.comment-list li").getall()
    comments_count = len(comments)

    summary_full_text = selector.css("div.entry-content p").get()
    summary = remove_tags_html(summary_full_text)

    tags = selector.css("a[rel*=tag]::text").getall()
    category = selector.css("a.category-style span.label::text").get()

    print(summary)

    return {
        "url": base_url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
