import time
from bs4 import BeautifulSoup
from selenium import webdriver

print("Webscraping - this takes about 15 seconds...")

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.get("https://www.iticket.co.nz/events/2021/aug/cs-get-degrease")

pages = []

for x in range(1, 4):
    driver.find_element_by_xpath(
        f'//*[@id="Showings"]/table/tbody/tr[{x}]/td[2]/div[1]/div/div[2]/button').click()
    time.sleep(3)
    pages.append(driver.page_source)

driver.quit()

total_sold = 0

for x in range(3):
    print()
    print(f"DAY {x + 1} TICKET SALES:")
    soup = BeautifulSoup(pages[x], 'html.parser')
    results = soup.find(id="seating-plan")
    seats = results.find_all("path", class_="leaflet-interactive")

    sold = 0
    remain = 0

    for seat in seats:
        if seat['fill'] == "#D2D7D3":
            sold += 1
            total_sold += 1
        else:
            remain += 1

    percent = "{:.1%}".format(sold/717)

    print(str(sold) + " seats sold, " +
          str(remain) + " seats remaining (" + percent + " sold)")

total_remain = 2151 - total_sold
total_percent = "{:.1%}".format(total_sold/2151)

print()
print("IN TOTAL:")
print(str(total_sold) + " seats sold, " + str(total_remain) +
      " seats remaining (" + total_percent + " sold)")

exit()
