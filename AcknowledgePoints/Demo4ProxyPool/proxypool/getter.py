from Demo4ProxyPool.proxypool.utils import get_page
from pyquery import PyQuery as pq
import re
import time

class ProxyMetaclass(type):
    """
        元类，在FreeProxyGetter类中加入
        __CrawlFunc__和__CrawlFuncCount__
        两个参数，分别表示爬虫函数，和爬虫函数的数量。
    """
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count = count +1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class FreeProxyGetter(object,metaclass=ProxyMetaclass):
    def get_raw_proxies(self,callback):
        proxies = []
        print('callback',callback)
        for proxy in eval("self.{}()".format(callback)):#将字符串str当成有效的表达式来求值并返回计算结果。
            print('Getting',proxy,'from',callback)
            proxies.append(proxy)
        return proxies

    def crawl_kuaidaili(self):
        for page in range(1, 4):
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
                if re_ip_adress:
                    yield result.replace(' ', '')
                else:
                    continue