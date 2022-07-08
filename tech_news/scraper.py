import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup
from tech_news.database import create_news


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

    all_comments = selector.css("ol.comment-list li").getall()
    comments_count = len(all_comments)

    first_paragraph = selector.css("div.entry-content p").getall()[0]
    summary = remove_tags_html(first_paragraph)

    tags = selector.css("a[rel*=tag]::text").getall()
    category = selector.css("a.category-style span.label::text").get()

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
    page_to_get_the_urls = 'https://blog.betrybe.com'
    news_urls = []
    news_data = []

    while len(news_urls) < amount:
        current_page = fetch(page_to_get_the_urls)
        urls_on_current_page = scrape_novidades(current_page)
        news_urls.extend(urls_on_current_page)
        page_to_get_the_urls = scrape_next_page_link(current_page)

    for index, url in enumerate(news_urls):
        if (index == amount):
            break
        else:
            current_news = fetch(url)
            current_data = scrape_noticia(current_news)
            news_data.append(current_data)

    create_news(news_data)

    return news_data
