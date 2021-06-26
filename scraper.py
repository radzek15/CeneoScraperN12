from bs4 import BeautifulSoup
import requests
import json

def get_feature(dom_tree, selector, attribute=None):
    try:
        if isinstance(attribute,str):
            return dom_tree.select_one(selector)[attribute].strip()
        if isinstance(attribute, list):
            return [element.text.strip() for element in dom_tree.select(selector)]
        return dom_tree.select_one(selector).text.strip()
    except (AttributeError, TypeError):
        return None

features = {
    "author": ["span.user-post__author-name"],
    "recomm": ["span.user-post__author-recomendation"],
    "stars": ["span.user-post__score-count"],
    "content": ["div.user-post__text"],
    "pros": ["div.review-feature__title--positives ~ .review-feature__item", []],
    "cons": ["div.review-feature__title--negatives ~ .review-feature__item", []],
    "useful": ["button.vote-yes > span"],
    "useless": ["button.vote-no > span"],
    "purchased": ["div.review-pz"],
    "publish_date": ["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchase_date": ["span.user-post__published > time:nth-child(2)", "datetime"]
}

product_id = input("Podaj kod produktu: ")
next_page = "https://www.ceneo.pl/{}#tab=reviews".format(product_id)
all_opinions = []

while next_page:
    respons = requests.get(next_page)
    page_dom = BeautifulSoup(respons.text, "html.parser")
    opinions = page_dom.select("div.js_product-review")

    for opinion in opinions:
        single_opinion = {key:get_feature(opinion,*value) for key, value in features.items()}
        single_opinion["opinion_id"] = opinion["data-entry-id"],
        all_opinions.append(single_opinion)

    try:
        next_page = 'https://www.ceneo.pl' + \
            get_feature(page_dom, "a.pagination__next", "href")
    except TypeError:
        next_page = None 
    print(next_page)

with open("opinions/{}.json".format(product_id), "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)

# print(json.dumps(all_opinions, indent=4, ensure_ascii=False))