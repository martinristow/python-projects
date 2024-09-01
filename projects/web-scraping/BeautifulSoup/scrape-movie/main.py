from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
website_movie_text = response.text

soup = BeautifulSoup(website_movie_text, "html.parser")
# print(soup.prettify())
all_movies = soup.findAll(name="h3", class_="title")
movie_titles = [movie.text for movie in all_movies[::-1]]
# movie_titles = [all_movies[movie].getText() for movie in range(len(all_movies)-1, -1, -1)]

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in movie_titles:
        file.write(f"{title}\n")
