from datetime import datetime
from tech_news.database import search_news


def get_tuple_list(received_list):
    output_list = []
    for each_item in received_list:
        output_list.append((each_item["title"], each_item["url"]))
    return output_list


# Requisito 6
def search_by_title(title):
    if type(title) != str:
        return []
    else:
        news = search_news({"title": {"$regex": title, "$options": "i"}})
        return get_tuple_list(news)


def new_format_date(date):
    months = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }

    return f"{date.day} de {months[date.month]} de {date.year}"


# Requisito 7
def search_by_date(date):
    try:
        date_format = datetime.fromisoformat(date).date()
        new_date = new_format_date(date_format)
        news = search_news({
            "timestamp": {"$regex": new_date, "$options": "i"}
        })
        return get_tuple_list(news)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    if type(tag) != str:
        return []
    else:
        news = search_news({
            "tags": {"$regex": tag, "$options": "i"}
        })
        return get_tuple_list(news)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
