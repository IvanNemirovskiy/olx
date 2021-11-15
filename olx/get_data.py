from bs4 import BeautifulSoup
import requests

req = requests.get("https://www.olx.ua/uk/nedvizhimost/kvartiry/kiev/").text

price_list = []
flat_href_list = []
soup = BeautifulSoup(req, 'lxml')
prices_s = soup.find_all('p', class_='price')
flat_hrefs = soup.find_all('a', class_="marginright5 link linkWithHash detailsLink", href=True)
for price_s in prices_s:
    price = str(price_s.strong).replace('</strong>', '').replace('<strong>', '')
    price_list.append(price)

for href in flat_hrefs:
    flat_href_list.append(href['href'])


flat_location_list = []

for flat in flat_href_list[0:1]:
    flat_req = requests.get(flat).text
    soup_loc = BeautifulSoup(flat_req, 'lxml')
    # flat_locs = soup_loc.find_all('h1', class_="css-r9zjja-Text")
    # for title in flat_locs:
        # if "," in title:
        #     location = str(title).split(',')[1:]
        # else:
    descriptions = soup_loc.find_all('div', class_="css-g5mtbi-Text")
    for description in descriptions:
        print(description)
        print(str(description).split('<br/>')[0].replace('<div class="css-g5mtbi-Text">', ''))
    # flat_location_list.append(flat_locs)

del price_list[0:5]
# print(price_list)
# print(flat_href_list)
# print("!!!")
# print(flat_location_list)
