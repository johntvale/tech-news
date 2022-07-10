from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    if type(title) != str:
        return []
    else:
        news = search_news({"title": {"$regex": title, "$options": "i"}})
        output_list = []
        for each_news in news:
            output_list.append((each_news["title"], each_news["url"]))
        return output_list


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

    year = date.year
    month = months[date.month]
    day = date.day

    return f"{day} de {month} de {year}"


# Requisito 7
def search_by_date(date):
    try:
        date_format = datetime.fromisoformat(date).date()
        new_date = new_format_date(date_format)
        print(new_date)
        news = search_news({
            "timestamp": {"$regex": new_date, "$options": "i"}
        })
        output_list = []
        for each_news in news:
            output_list.append((each_news["title"], each_news["url"]))
        return output_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
