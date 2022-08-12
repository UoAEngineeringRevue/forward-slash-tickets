# forward-slash-tickets

A webscraping tool to track how many seats are [un]available on any given iTicket event with 3 days of shows. This coincidentally aligns with the structure of all 3 Auckland revues. Isn't the world a beautiful place?

## Installation

```
python -m pip install beautifulsoup4
python -m pip install selenium
```

[Update the Selenium ChromeDriver if needed by downloading the version that matches your installed Chrome instance.](https://chromedriver.chromium.org/downloads)

## Usage

```
python -m scrape.py
```

Update the iTicket links if needed on lines 16, 19, and 22.
