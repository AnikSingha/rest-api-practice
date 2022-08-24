# MAL REST API

### About
This API contains data about the top 1000 anime and manga on [MAL](https://myanimelist.net/)(MyAnimeList) ranked by user submitted ratings. You can access the API by clicking [here](https://mal-rest-api-practice.herokuapp.com/). I obtained the data by webscraping the website using BeautifulSoup.

### How to Query Data
Start by adding navigating to either the /anime or /manga subdirectories, depending on what type of data you want to query. Due to the limited variety of data there is only one query paramter, which is id. Going to https://mal-rest-api-practice.herokuapp.com/anime?id=100 would give you info about the 100th highest rated anime.

### Warning
I decided to limit my API to only the top 1000 anime and manga as to not put strain on MAL\'s servers. If you choose to alter my script to obtain more data be sure to contact MAL and obtain their permission before doing so. You should always look at a website\'s policy on webscraping before taking any action that could potentially break their terms of service.