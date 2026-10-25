# 来源：书页 P263，PDF 275
import requests
from lxml import etree      # 导入HTML 解析模块

def get_ip_by_page(url, headers, ip_list):
    # 发送网络请求
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"     # 设置编码方式
    if response.status_code == 200:    # 判断请求是否成功
        html = etree.HTML(response.text)    # 解析HTML
        # 获取每页的所有tr 标签
        tr_all = html.xpath("//tbody//tr")
        for tr in tr_all:
            ip = tr.xpath("./td[1]/text()")[0]   # 获取每个tr 中的ip
            port = tr.xpath("./td[2]/text()")[0]   # 获取每个tr 中的port
            ip_list.append(ip + ":" + port)
            print(f' 代理IP: {ip}, 对应端口: {port}')

# 头部信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/72.0.3626.121 Safari/537.36"
}

if __name__ == "__main__":
    ip_list = []  # 创建保存IP 地址的列表

    # 获取免费的代理地址
    for i in range(1, 5):
        url = f"http://www.ip3366.net/free/?stype=1&page={i}"
        get_ip_by_page(url, headers, ip_list)

    print()
    # 遍历获取到的地址，并通过代理发送网络请求
    for ip in ip_list:
        print(f"{ip} ", end="")
        proxies = {
            "http": f"http://{ip}",
            "https": f"https://{ip}",
        }
        try:
            response = requests.get(
                "http://httpbin.org/get", headers=headers, proxies=proxies, timeout=10
            )
            if response.status_code == 200:  # 请求成功说明代理可用，否则不可用
                print(' 代理可用')
            else:
                print(' 代理不可用')
        except Exception as e:
            print(' 代理不可用')               # 请求过程中发生异常，说明代理不可用
