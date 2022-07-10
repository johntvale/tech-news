from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    if type(title) != str:
        return []
    else:
        news = search_news({"title": {"$regex": title, "$options": "i"}})
        output_list = []
        for each_news in news:
            # print(each_news)
            output_list.append((each_news["title"], each_news["url"]))
        return output_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
