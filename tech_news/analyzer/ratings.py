from tech_news.analyzer.search_engine import get_tuple_list
from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    sorted_news = get_collection().find({}).sort("comments_count", -1)
    top_five = get_tuple_list(list(sorted_news)[:5])

    return top_five


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
