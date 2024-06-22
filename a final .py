from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError
from time import sleep

def coinranking______R():
    coinrank_ing = urlopen('https://coinranking.com/')
    bbs4_ranking = BeautifulSoup(coinrank_ing.read(), 'lxml')
    table_ranking = bbs4_ranking.find_all('div', {'class': 'coin-list__body'})
    
    price_ranking = {}
    for row in table_ranking[:10]:  # First 10 coins
        symbol = row.find('span', {'class': 'coin-name'}).get_text().strip()
        price_ranking = row.find('div', {'class': 'coin-list__price'}).get_text().replace('$', '').replace(" ", "").replace("\n", "").replace(",", "")
        price = float(price_ranking)
        prices_coin_ranking[symbol] = price
    return prices_coin_ranking

def coincap_________R():
    coincap = urlopen('https://coinmarketcap.com/')
    bs4_coin_cap = BeautifulSoup(coincap.read(), 'lxml')
    table_coin = bs4_coin_cap.ind_all('tr', {'class': 'cmc-table-row'})
    
    price_cap = {}
    for row in table_coin[:10]:  # First 10 coins
        symbol = row.find('td', {'class': 'cmc-table_cell--sort-by_symbol'}).get_text().strip()
        price_cap = row.find('td', {'class': 'cmc-table_cell--sort-by_price'}).get_text().replace('$', '').replace(" ", "").replace("\n", "").replace(",", "")
        price = float(price_cap)
        price_cap[symbol] = price
    return price_cap

while True:
    try:
        prices_coin_ranking = coinranking______R()
        prices_coin_market_cap = coincap_________R()

        for h in prices_coin_ranking:
            if h in prices_coin_market_cap:
                price_ranking = prices_coin_ranking[h]
                price_market_cap = prices_coin_market_cap[h]
                if price_ranking < price_market_cap:
                    print(f"{h}: CoinRanking")
                else:
                    print(f"{h}: CoinCap")

    except URLError as e:
        print('you should connect to internet')
        print ("try a gain")
        sleep(1)