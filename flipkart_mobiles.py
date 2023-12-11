import requests
from bs4 import BeautifulSoup
import pandas as pd
for i in range(1,21):

    url = "https://www.flipkart.com/mobiles/smartphones~type/pr?sid=tyy%2C4io&page=" + str(i)
    req = requests.get(url)
    # print(r)

    bs = BeautifulSoup(req.text,features="html.parser")

    next_page = bs.find("a", {"class": "_1LKTO3"})
    complete_next_page = "https://www.flipkart.com" + next_page["href"]

    box = bs.find("div",{"class":"_1YokD2 _3Mn1Gg"})
    # print(bs)

    # retrieving mobile_name,price,description,reviews
    NAMES = []
    PRICES = []
    DESCRIPTION = []
    REVIEWS = []

    names = box.find_all("div",{"class":"_4rR01T"})
    # print(names)

    for i in names:
        n = i.text
        NAMES.append(n)
    # print(NAMES)

    price = box.find_all("div",{"class":"_30jeq3 _1_WHN1"})
    # print(price)

    for i in price:
        n = i.text
        PRICES.append(n)
    #print(PRICES)

    description = box.find_all("ul",{"class": "_1xgFaf"})
    # print(description)

    for i in description:
        n = i.text
        DESCRIPTION.append(n)
    #print(DESCRIPTION)

    review = box.find_all("div",{"class": "_3LWZlK"})
    # print(review)

    for i in review:
        n = i.text
        REVIEWS.append(n)
    # print(REVIEWS)

    # creating dataframe

    df = pd.DataFrame({"MOBILE":NAMES,"PRICES":PRICES,"DESCRIPTION":DESCRIPTION,"RATINGS & REVIEWS":REVIEWS})
    print(df)
