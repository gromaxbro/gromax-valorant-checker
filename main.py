import requests
from bs4 import BeautifulSoup

res = requests.get("https://valorant.fandom.com/wiki/Weapon_Skins")
soup = BeautifulSoup(res.text, 'html.parser') 
# print(soup.prettify())
tr_elements = soup.select('tbody tr')

for index, tr in enumerate(tr_elements, start=1):
        # Find the img element within the current tr
    img_element = tr.find('img')

#         # Check if the img element is found
    if img_element:
        skin = img_element.get('alt')
        # print(skin)
        try:

            price_element = tr.find_all('td')[2]
            
            price = price_element.get("data-sort-value")
            
            print(skin+":"+price)
        except:
            pass
