import requests
import json
from bs4 import BeautifulSoup


data = {"anime": {}, "manga": {}}

def get_shows(show):
    
    rank = show.find(class_='rank ac').text.strip() #Anime rank

    name = show.find(class_='title al va-t word-break').find('img')['alt'].split('Anime:')[-1].strip() #Anime name

    try:
        rating = show.find(class_='text on score-label score-8').text #Anime rating
    except:
        try:
            rating = show.find(class_='text on score-label score-7').text 
        except:
            try:
                rating = show.find(class_='text on score-label score-9').text
            except:
                rating = "unknown"

    info = show.find(class_='information di-ib mt4').text

    return rank, name, rating, info

def get_manga(show):
    
    rank = show.find(class_='rank ac').text.strip() #Anime rank

    name = show.find(class_='hoverinfo_trigger fl-l ml12 mr8').find('img')['alt'].split('Manga:')[-1].strip() #Manga name

    try:
        rating = show.find(class_='text on score-label score-8').text #Anime rating
    except:
        try:
            rating = show.find(class_='text on score-label score-7').text 
        except:
            try:
                rating = show.find(class_='text on score-label score-9').text
            except:
                rating = "unknown"

    info = show.find(class_='information di-ib mt4').text

    return rank, name, rating, info


def get_info(info):

    type = info.lstrip().split()[0] + " " + info.lstrip().split()[1] + " " + info.lstrip().split()[2] 

    air_time = info.split('\n')[2].strip()

    return type, air_time


for i in range(0, 1000, 50):

    html_doc = requests.get(f'https://myanimelist.net/topanime.php?limit={i}').text

    soup = BeautifulSoup(html_doc, features="html.parser")
    shows = soup.find_all(class_="ranking-list")

    for show in shows:
        rank, name, rating, info = get_shows(show)

        type, air_time = get_info(info)

        data["anime"][f"id: {rank}"] = {"name" : name, "type": type, "rating" : rating, "air time" : air_time}

for i in range(0, 1000, 50):

    html_doc = requests.get(f'https://myanimelist.net/topmanga.php?limit={i}').text

    soup = BeautifulSoup(html_doc, features="html.parser")
    mangas = soup.find_all(class_="ranking-list")

    for manga in mangas:
        rank, name, rating, info = get_manga(manga)

        type, air_time = get_info(info)

        data["manga"][f"id: {rank}"] = {"name" : name, "type": type, "rating" : rating, "air time" : air_time} 


with open('data.json','w') as jsonFile:
    json.dump(data, jsonFile, indent=3)


