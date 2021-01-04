import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(response, "html.parser")

list_title = soup.find(name="h1").text

movie_list = soup.findAll(name="h3", class_="title")
movie_list.reverse()

watch_list = []
for movie in movie_list:
    movie_title = movie.getText()
    if movie_title == "The Godfather":
        movie_title = f"1) {movie_title}"

    watch_list.append(movie_title)

with open("watch_list.txt", mode="w", encoding="utf8") as list_:
    list_.write(list_title + "\n")
    for title in watch_list:
        list_.write(title + "\n")
