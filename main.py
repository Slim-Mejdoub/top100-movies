import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text
soup = BeautifulSoup(data, "html.parser")


list_all_movies = soup.find_all("h3", class_="title")
list_movies = [movie.getText() for movie in list_all_movies]

movies = list_movies[::-1]
movie = "\n".join(movies)

with open("movies.txt", "w", encoding='utf-8') as file:
    file.write(movie)


