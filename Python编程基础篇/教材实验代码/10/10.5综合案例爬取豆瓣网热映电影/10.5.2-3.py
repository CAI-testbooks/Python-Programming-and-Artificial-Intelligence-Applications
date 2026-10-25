# 来源：书页 P290，PDF 302
import requests
from bs4 import BeautifulSoup

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/130.0.0.0 Safari/537.36"
)
headers = {"User-Agent": USER_AGENT}
resp = requests.get("https://www.douban.com/", headers=headers)

soup = BeautifulSoup(resp.text, features="lxml")
movie_div_list = soup.select("div.movie-list")
print(len(movie_div_list))
print(movie_div[0].prettify())
