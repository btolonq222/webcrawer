def bookSearch(book,page):
    import requests
    from bs4 import BeautifulSoup
    import time
    import random
    d = {}
    for i in range(page):
        url = 'https://search.books.com.tw/search/query/cat/all/key/{}/sort/1/page/{}/v/0/'.format(book,i)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        time.sleep(random.randint(0,50))
        #print(soup.prettify())
        for j in soup.find_all(class_='item'):
            d[j.find_all('a')[0]['title']]=[]
            d[j.find_all('a')[0]['title']].append(j.find_all('span')[0].text)
            d[j.find_all('a')[0]['title']].append(j.find_all('a')[2]['title'])
            d[j.find_all('a')[0]['title']].append(j.find_all('a')[3]['title'])
            d[j.find_all('a')[0]['title']].append(j.text.replace(' ','').replace('\t','').split(',')[3].split(' ')[0].split('\n')[0])
            d[j.find_all('a')[0]['title']].append(j.find_all(class_='price')[0].text.replace(' ','').replace('\t','').split('\n')[1])
    return d
#     print(j.find_all('a')[0]['title'])
#     print(j.find_all('span')[0].text)
#     print(j.find_all('a')[2]['title'])
#     print(j.find_all('a')[3]['title'])
#     print(j.text.replace(' ','').replace('\t','').split(',')[3].split(' ')[0].split('\n')[0])
#     print(j.find_all(class_='price')[0].text.replace(' ','').replace('\t','').split('\n')[1])
    

x = bookSearch(20)

print(len(x))