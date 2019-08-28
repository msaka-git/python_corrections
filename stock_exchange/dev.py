import requests
import datetime

from bs4 import BeautifulSoup

## EPS


urleps="https://www.borsadirekt.com/sirket-karti/ACSEL"
response_eps = requests.get(urleps)
html_content_eps = response_eps.content
soup_eps = BeautifulSoup(html_content_eps, "html.parser")
eps = soup_eps.select_one('tbody:contains("Hisse Başı Kar") + td')
#eps=soup_eps.find_all('div', {'class': 'table-responsive'})

print(eps)