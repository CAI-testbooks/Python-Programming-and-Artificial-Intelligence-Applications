# 来源：书页 P303，PDF 315
import requests
from bs4 import BeautifulSoup

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/130.0.0.0 Safari/537.36"
)
headers = {"User-Agent": USER_AGENT}
params = {
    "sort": "hotest",  # 按" 最受欢迎的" 排序
    "start": "0",      # 从第1 条起获取
}
resp = requests.get(
    "https://movie.douban.com/subject/36154853/reviews", params=params, headers=headers
)
print(resp.status_code)  # 如果是403 则意味着需要登录才能获取

# 使用BeautifulSoup 解析
soup = BeautifulSoup(resp.text, features="lxml")
# 定位到影评列表div
review_list = soup.find("div", class_="review-list")
# 影评列表div 下的所有直接子节点，就是存放每一条影评的顶级div
reviews = review_list.find_all(
    attrs={"data-cid": True}  # True 表示只要有data-cid 属性即可
)

for i in range(0, 2):  # 此处为演示方便，只获取前2 条影评的完整内容
    review = reviews[i]
    review_id = review["data-cid"]
    resp = requests.get(
        f"https://movie.douban.com/j/review/{review_id}/full",
        params=params,
        headers=headers,
    )
    print(resp.status_code)  # 如果是403 则意味着需要登录才能获取
    print(resp.json())       # 该请求的响应格式是JSON，故可以JSON 解析
