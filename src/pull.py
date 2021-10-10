import requests
from bs4 import BeautifulSoup

class scrapinfo:
    def scnew(self):
        self.coiname = input("Input the name of the coin: ")
        url = "https://coinmarketcap.com/ru/currencies/" + self.coiname + "/news/"
        page = requests.get(url)
        soup= BeautifulSoup(page.text, "html.parser")
        findid = soup.find("meta", property="og:image")
        info = findid['content']
        coinid = info.rpartition('/')[2].rpartition('.')[0]
        content = requests.get('https://api.coinmarketcap.com/content/v3/news?coins='+coinid+'&page=1&size=20')
        data = content.json()
        
        for n in range(20):
            print(data.get('data')[n].get('meta').get('title')+": ")
            pageurl = data.get('data')[n].get('meta').get('sourceUrl')
            print(pageurl)
            newspage = requests.get(pageurl)
            soup2 = BeautifulSoup(newspage.text, 'html.parser')
            try:
                news = soup2.findAll('p', limit=None)
                lengthnews = len(news)
                for m in range(lengthnews):
                    print(news[m].text)
                print('\n')
            except: AttributeError

