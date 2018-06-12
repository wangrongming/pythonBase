from pyquery import PyQuery as pq
from Demo4ProxyPool.proxypool.utils import get_page
import re
import time
import requests
from requests.exceptions import ConnectTimeout
from Demo4ProxyPool.proxypool.db import RedisClient

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

def crawl_kuaidaili():
    for page in range(10, 15):
        time.sleep(1)
        # 国内高匿代理
        start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
        html = get_page(start_url)
        ip_adress = re.compile(
            '<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\w+)</td>'
        )
        re_ip_adress = ip_adress.findall(html)
        for adress, port in re_ip_adress:
            result = adress + ':' + port
            yield result.replace(' ', '')

#发起请求,记得取消注释
def get_request():
    # proxies = {
	# 	"http": "http://"+ip,
	# 	"https": "http://"+ip,
	# }
    proxies = {
    	"http": "http://"+'218.56.132.155:8080',
    	"https": "http://"+'218.56.132.155:8080',
    }
    url = "http://www.baidu.com "

    html=requests.get(url,headers=headers, timeout=1)
    print(html.status_code)

if __name__ == '__main__':
    for i in crawl_kuaidaili():
        conn = RedisClient()
        conn.put(i)

