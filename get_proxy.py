import requests
from bs4 import BeautifulSoup
class get_proxy_array() :
    def __init__(self,u) :
        self.u = u
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}
    def get_array(self) :
        req = requests.get(self.u,headers=self.headers)
        html = BeautifulSoup(req.text, "html.parser")
        html_proxy_array = html.select('.odd')
        proxy_array = []
        for proxy in html_proxy_array :
            ip = proxy.select('td')[1].string
            port = proxy.select('td')[2].string
            proxy_type = proxy.select('td')[5].string.lower()
            if proxy_type == 'socks4/5' :
                proxy_type = 'socks5'
            proxies = (proxy_type,ip,port)
            proxy_array.append(proxies)
        self.proxy_array = proxy_array
s = get_proxy_array('http://www.xicidaili.com/')
s.get_array()
print(s.proxy_array)
