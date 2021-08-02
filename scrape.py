import time
from bs4 import BeautifulSoup
from selenium import webdriver

scrape_target = ""

while True:
    print("Enter the Revue you'd like scrape:")
    print("")
    print("1) Engineering Revue")
    print("2) Med Revue")
    print("3) Law Revue")
    choice = int(input(">>> "))

    if choice == 1:
        scrape_target = "https://www.iticket.co.nz/events/2021/aug/cs-get-degrease"
        break
    elif choice == 2:
        scrape_target = "https://www.iticket.co.nz/events/2021/aug/med-sch-musical"
        break
    elif choice == 3:
        scrape_target = "https://www.iticket.co.nz/events/2021/aug/nightmare-short-st"
        break
    else:
        print("Whoops, try again")

print("Webscraping - this takes about 15 seconds...")

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.get(scrape_target)

pages = []

for x in range(1, 4):
    driver.find_element_by_xpath(
        f'//*[@id="Showings"]/table/tbody/tr[{x}]/td[2]/div[1]/div/div[2]/button').click()
    time.sleep(3)
    pages.append(driver.page_source)

driver.quit()

season_total = 0
total_sold = 0

for x in range(3):
    print()
    print(f"DAY {x + 1} TICKET SALES:")
    soup = BeautifulSoup(pages[x], 'html.parser')
    results = soup.find(id="seating-plan")
    seats = results.find_all("path", class_="leaflet-interactive")

    night_total = 0
    sold = 0
    remain = 0

    for seat in seats:
        night_total += 1
        if seat['fill'] == "#D2D7D3":
            sold += 1
            total_sold += 1
        else:
            remain += 1

    percent = "{:.1%}".format(sold/night_total)

    print(str(sold) + " seats sold, " +
          str(remain) + " seats remaining (" + percent + " sold)")

    season_total += night_total

total_remain = season_total - total_sold
total_percent = "{:.1%}".format(total_sold/season_total)

print()
print("IN TOTAL:")
print(str(total_sold) + " seats sold, " + str(total_remain) +
      " seats remaining (" + total_percent + " sold)")

exit()
