import requests
from bs4 import BeautifulSoup
import pandas as pd

for i in range(164):
# for i in range(2):
    inp_dir=f"anime-links/zoro_page_{i+1}.xlsx"
    out_dir=f"anime-content/zoro_page_{i+1}.xlsx"
    df_links=pd.read_excel(inp_dir,usecols=["Link"])
    data_list = []
    for link in df_links["Link"]:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        original_link = link
        poster = soup.find('div', {'class': 'film-poster'}).find('img')['src']
        jname = soup.find('h2', {'class': 'film-name dynamic-name'})['data-jname']
        ename = soup.find('h2', {'class': 'film-name dynamic-name'}).text.strip()
        stats_data = soup.find('div', {'class': 'film-stats'}).text.strip()
        anime_link = soup.find('a', {'class': 'btn btn-radius btn-primary btn-play'})['href']
        description = soup.find('div', {'class': 'film-description m-hide'}).find('div', {'class': 'text'}).text.strip()
        other_data = soup.find('div', {'class': 'anisc-info'}).text.strip()
        data_list.append({
        'link': original_link,
        'poster': poster,
        'jname': jname,
        'ename': ename,
        'stats-data': stats_data,
        'anime-link': anime_link,
        'description': description,
        'other data': other_data
        })
    df = pd.DataFrame(data_list)
    df.to_excel(out_dir, index=False)