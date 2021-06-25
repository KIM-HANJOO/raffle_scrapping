import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

URL_luck_d = 'https://www.luck-d.com/'
URL_musinsa = 'https://store.musinsa.com/app/raffle/lists?raffle_state_gb=S'

response_luck_d = requests.get(URL_luck_d)
response_musinsa = requests.get(URL_musinsa)

if response_luck_d.status_code == 200:
    html_luck_d = response_luck_d.text
    soup_luck_d = BeautifulSoup(html_luck_d, 'html.parser')
    
else:
    print("status_code for luck_d != 200")
    print("statuse_code for luck_d = ", response_luck_d.status_code)

if response_musinsa.status_code == 200:
    html_musinsa = response_musinsa.text
    soup_musinsa = BeautifulSoup(html_musinsa, 'html.parser')
    
else:
    print("status_code for musinsa != 200")
    print("statuse_code for musinsa = ", response_musinsa.status_code)

# now_raffle_luck_d = soup_luck_d.find_all('div', 'product_thumb_layer') #'gallery_cell_layer')
# print(now_raffle_luck_d)

now_raffle_luck_d_1 = soup_luck_d.find('h4', 'sub_title')
now_raffle_luck_d_2 = soup_luck_d.find('div', 'gallery')
now_raffle_luck_d_3 = now_raffle_luck_d_3.find('a')
print(now_raffle_luck_d_1)
print(now_raffle_luck_d_2)

# soup = BeautifulSoup("<html>data</html>")

# if __name__ == "__main__":
#     soup = BeautifulSoup(html_doc, 'html.parser')
#     print('1. ', soup.title)
#     print('2. ', soup.title.name)
#     print('3. ', soup.title.string)
#     print('4. ', soup.title.parent.name)
#     print('5. ', soup.p)
#     print('6. ', soup.p['class'])
#     print('7. ', soup.a)
#     print('8. ', soup.find_all('a'))
#     print('9. ', soup.find(id="link3"))





# URL_luck_d = 'https://www.luck-d.com/'
# URL_musinsa = 'https://store.musinsa.com/app/raffle/lists?raffle_state_gb=S'

# response_luck_d = requests.get(URL_luck_d)
# response_musinsa = requests.get(URL_musinsa)

# if response_luck_d.status_code == 200:
#     html_luck_d = response_luck_d.text
# else:
#     print("status_code for luck_d != 200")
#     print("statuse_code for luck_d = ", response_luck_d.status_code)

# if response_musinsa.status_code == 200:
#     html_musinsa = response_musinsa.text
# else:
#     print("status_code for musinsa != 200")
#     print("statuse_code for musinsa = ", response_musinsa.status_code)

# # now_raffle_luck_d = html_luck_d.find_all('div', 'gallery_cell_layer')
# # print(now_raffle_luck_d)

# with open("https://www.luck-d.com/") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
#     all_divs = soup.find_all('div', 'gallery_cell_layer')
#     print(all_divs)

