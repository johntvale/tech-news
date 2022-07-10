from tech_news.analyzer.search_engine import get_tuple_list
from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    sorted_news = get_collection().find({}).sort("comments_count", -1).limit(5)
    top_five = get_tuple_list(sorted_news)

    return top_five


# Requisito 11
def top_5_categories():
    news = get_collection().find({})
    category_count = {}

    for each_news in news:
        if each_news["category"] in category_count:
            category_count[each_news["category"]] += 1
        else:
            category_count[each_news["category"]] = 1

    sorted_by_quantity = sorted(
        category_count,
        key=lambda x: category_count[x],
        reverse=True,
    )

    return sorted_by_quantity[:5]

# referencias da orderação:
# https://careerkarma.com/blog/python-sort-a-dictionary-by-value/#:~:text=To%20sort%20a%20dictionary%20by%20value%20in%20Python%20you%20can,Dictionaries%20are%20unordered%20data%20structures.
# https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
