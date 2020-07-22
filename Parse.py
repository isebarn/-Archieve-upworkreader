from bs4 import BeautifulSoup
import urllib3
from selenium import webdriver
import selenium as se
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import codecs

BASE_URL = 'https://www.upwork.com{}'
SEARCH_URL = 'https://www.upwork.com/search/jobs/?q={}'

def openPage(url):
  try:
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path='/usr/bin/geckodriver')
    driver.get(url)

    return driver

  except Exception as e:
    return None


def sourceToBS4(source):
  soup = BeautifulSoup(source, "lxml")

  return soup


class Ads:
  ads = []

  def __init__(self, sites, testing=False):
    self.testing = testing

    for site in sites:

      if self.testing:
        f = codecs.open("list.html", 'r')
        source = f.read()

      else:
        driver = openPage(SEARCH_URL.format(site))
        source = driver.page_source

      self.soup = sourceToBS4(source)
      self.getAds()


  def getAds(self):
    ads = self.soup.find_all("a", class_="job-title-link break visited")

    for ad in ads:

      fixed = ad.findNext('strong', class_="js-budget")
      if fixed is not None:
        fixed = fixed.text.replace(' ', '').replace('\n', '')

      payment_type = ad.findNext('strong').text.replace(' ', '').replace('\n', '')

      if 'Hourly' in payment_type:
        payment = payment_type

      else:
        payment = 'Fixed: {}'.format(fixed)

      result = {}
      result['id'] = ad['href'].split('~')[-1].replace('/', '')
      result['title'] = ad.text.replace('\n', '')
      result['url'] = BASE_URL.format(ad['href'])
      result['payment'] = payment

      self.ads.append(result)



def getHourly(soup):
  ads = soup.find_all('div', class_="d-inline-block m-sm-right")
  return ads

if __name__ == "__main__":
  parseSites = Ads(['scrap'], True)
  for x in parseSites.ads:
    print(x['payment'])
  #driver = openPage('https://www.upwork.com/job/Leads-generator_~01332fb131cfa88ea0/')
  #source = driver.page_source
  #print(sourceToBS4(source))
  #f = codecs.open("text.html", 'r')
  #source = f.read()
  #soup = driverToBS4(source)


  #result = []
  #print(getIDs(soup))
  #print(getTitles(soup))