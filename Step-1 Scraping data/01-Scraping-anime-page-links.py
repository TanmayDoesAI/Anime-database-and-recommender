import requests
from bs4 import BeautifulSoup
import pandas as pd
for i in range(164):
# for i in range(2):
    # print(i+1)
    data=[]
    url=f"https://zoro.to/az-list/?page={i+1}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    block_area_category = soup.find("section", class_="block_area block_area_category")
    flw_items = block_area_category.find_all("div", class_="flw-item")
    for flw_item in flw_items:
        film_detail = flw_item.find("div", class_="film-detail")
        film_name = film_detail.find("h3", class_="film-name")
        dynamic_name = film_name.find("a", class_="dynamic-name")
        title = dynamic_name.text
        href = dynamic_name["href"]
        data.append([title,f"https://zoro.to/{href}"])
        print(title+" https://zoro.to/"+href)
        df = pd.DataFrame(data, columns=["Film Name", "Link"])
        df.to_excel(f"anime-links/zoro_page_{i+1}.xlsx", index=False)
