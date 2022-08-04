import requests
import json
from bs4 import BeautifulSoup


data = {}

def get_shows(show):
    
    rank = show.find(class_='rank ac').text.strip() #Anime rank

    name = show.find(class_='title al va-t word-break').find('img')['alt'] #Anime name

    try:
        rating = show.find(class_='text on score-label score-8').text #Anime rating
    except:
        try:
            rating = show.find(class_='text on score-label score-7').text #Anime rating
        except:
            try:
                rating = show.find(class_='text on score-label score-9').text #Anime rating
            except:
                rating = "unknown"

    info = show.find(class_='information di-ib mt4').text

    return rank, name, rating, info


def get_show_info(info):

    show_type = info.lstrip().split()[0] + " " + info.lstrip().split()[1] + " " + info.lstrip().split()[2] 

    air_time = info.split('\n')[2].strip()

    return show_type, air_time


for i in range(0, 1050, 50):

    html_doc = requests.get(f'https://myanimelist.net/topanime.php?limit={i}').text

    soup = BeautifulSoup(html_doc, features="html.parser")
    shows = soup.find_all(class_="ranking-list")

    for show in shows:
        rank, name, rating, info = get_shows(show)

        show_type, air_time = get_show_info(info)

        data[f"id: {rank}"] = {"name" : name, "type": show_type, "rating" : rating, "air time" : air_time}


with open('data.json','w') as jsonFile:
    json.dump(data, jsonFile)


