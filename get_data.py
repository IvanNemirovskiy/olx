from bs4 import BeautifulSoup
import requests

req = requests.get("https://www.olx.ua/uk/nedvizhimost/kvartiry/kiev/", 'html.parser').text

with open('olx.html', 'w') as save_file:
    save_file.write(req)

price_list = []
flat_href_list = []
with open('olx.html', 'r') as r_file:
    content = r_file.read()

    soup = BeautifulSoup(content, 'lxml')
    prices_s = soup.find_all('p', class_='price')
    flat_hrefs = soup.find_all('a', class_="marginright5 link linkWithHash detailsLink", href=True)
    for price_s in prices_s:
        price = str(price_s.strong).replace('</strong>', '').replace('<strong>', '')
        price_list.append(price)

    for href in flat_hrefs:
        flat_href_list.append(href['href'])

del price_list[0:5]
zip_flat_data = zip(flat_href_list, price_list)
flat_dict = dict(zip_flat_data)
print(flat_dict)