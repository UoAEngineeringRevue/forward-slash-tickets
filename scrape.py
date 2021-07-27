import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

print("Starting up Selenium...")

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')
driver = webdriver.Chrome("chromedriver.exe", options=options)

print("Retrieving iTicket website...")

driver.get("https://www.iticket.co.nz/events/2021/aug/cs-get-degrease")

print("Retrieved iTicket website")
print("Retrieving tickets...")

pages = []

for x in range(1, 4):
    driver.find_element_by_xpath(
        f'//*[@id="Showings"]/table/tbody/tr[{x}]/td[2]/div[1]/div/div[2]/button').click()
    time.sleep(5)
    pages.append(driver.page_source)

driver.quit()

print("Retrieved tickets.")


for x in range(3):
    print(f"DAY {x} TICKET SALES:")
    soup = BeautifulSoup(pages[x], 'html.parser')
    results = soup.find(id="seating-plan")
    seats = results.find_all("path", class_="leaflet-interactive")

    sold = 0
    remain = 0

    for seat in seats:
        if seat['fill'] == "#D2D7D3":
            sold = sold + 1
        else:
            remain = remain + 1

    print(str(sold) + " seats sold, " +
          str(remain) + " seats remaining")


exit()
