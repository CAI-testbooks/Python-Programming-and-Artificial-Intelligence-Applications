# 来源：书页 P295，PDF 307
import requests
from bs4 import BeautifulSoup

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/130.0.0.0 Safari/537.36"
)
headers = {"User-Agent": USER_AGENT}
# 替换下面的URL，即可爬取其他电影的海报和信息
resp = requests.get("https://movie.douban.com/subject/36154853/", headers=headers)

soup = BeautifulSoup(resp.text, features="lxml")
pic_div = soup.select("div#mainpic")[0]
info_div = soup.select("div#info")[0]
print(info_div.prettify(formatter="minimal"))

# 海报图片URL
poster_url = pic_div.find("img")["src"]
# 获取并保存图片
resp = requests.get(poster_url, headers=headers)
with open("poster.png", "wb") as f:
    f.write(resp.content)

# 提取字段信息
fields = {}
for span in info_div.find_all("span", class_="pl"):
    field_name = span.text.strip().strip(":")  # 获取字段名并去除冒号
    field_value = []                           # 临时存储字段值的各部分
    # 遍历class="pl" 的span 之后的所有兄弟节点，直到遇到<br> 为止
    current = span.next_sibling
    while current and current.name != "br":
        if hasattr(current, "text") and current.text.strip() != ":":
            field_value.append(current.text.strip())
        current = current.next_sibling
    # 将各部分的字段值拼接为完整的字段值，再存储到字典中
    fields[field_name] = "".join(field_value)

# 打印提取的字段信息
for key, value in fields.items():
    print(f"{key}: {value}")
