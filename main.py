import requests
from bs4 import BeautifulSoup
import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

url = 'https://store.micropython.org/'
r = requests.get(url)
html = BeautifulSoup(r.text, 'html.parser')


elems = html.select(".col-sm-4 > a")
links = []
for el in elems:
    links.append( url + el.attrs["href"])

print(links)
row = 0
for link in links :
    r = requests.get(link)
    html = BeautifulSoup(r.text, 'html.parser')
    worksheet.write(row, 0, html.select(".product-name")[0].text)
    price = html.select(".product-ppu")[0].text.replace("each", '')
    worksheet.write(row, 1, price)
    row += 1
workbook.close()
