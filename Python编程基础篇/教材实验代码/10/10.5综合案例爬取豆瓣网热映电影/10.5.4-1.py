# 来源：书页 P298，PDF 310
import requests
from bs4 import BeautifulSoup

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/130.0.0.0 Safari/537.36"
)
headers = {"User-Agent": USER_AGENT}
params = {
    "status": "P",
    "percent_type": "h",  # 只看好评
    "sort": "new_score",  # 按热门排序
    "limit": "10",        # 单页获取10 条
    "start": "30",        # 从第31 条起获取
}
resp = requests.get(
    "https://movie.douban.com/subject/36154853/comments", params=params,
    headers=headers
)
print(resp.status_code)  # 如果是403 则意味着需要登录才能获取

# 使用BeautifulSoup 解析
soup = BeautifulSoup(resp.text, features="lxml")
# 筛选所有短评项
comments = soup.find_all("div", class_="comment-item")

# 逐个提取短评信息
results = []
for comment in comments:
    avatar = comment.find("div", class_="avatar").find("img")["src"]
    nickname = comment.find("span", class_="comment-info").find("a").text
    star_class = comment.find("span", class_="comment-info").find(
        "span", class_="rating"
    )
    star_rating = int(star_class["class"][0][-2:]) // 10 if star_class else None
    time = comment.find("span", class_="comment-time")["title"]
    location = (
        comment.find("span", class_="comment-location").text
        if comment.find("span", class_="comment-location")
        else None
    )
    content = (
        comment.find("p", class_="comment-content")
        .find("span", class_="short")
        .text.strip()
    )

    results.append(
        {
            "avatar": avatar,
            "nickname": nickname,
            "star_rating": star_rating,
            "time": time,
            "location": location,
            "content": content,
        }
    )

# 打印结果
for result in results:
    print(result)
