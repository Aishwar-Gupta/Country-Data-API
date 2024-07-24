# pip install webdriver-manager
# pip install selenium

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.add_argument('--no-sandbox')
options.add_experimental_option("detach", False)  # stop from closing the chrome after done

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

URL = "https://data.worldbank.org/country"
driver.get(URL)


def all_countries():
    """ Scrape all countries in Alphabetical order and returns a list."""

    countries = []
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//section[@class="nav-item"]'))
        )
        sections = driver.find_elements(By.XPATH, '//section[@class="nav-item"]')
        for section in sections:
            country = section.find_elements(By.TAG_NAME, 'li')
            for c in country:
                countries.append(c.text)
    except Exception:
        raise SystemExit("Element was not found!")
    return countries


def country_by_letter(letter):
    """ Scrape country by starting letter and returns a list of countries."""

    countries = []
    mapping = {
        "A": "225",
        "B": "254",
        "C": "295",
        "D": "340",
        "E": "351",
        "F": "370",
        "G": "383",
        "H": "414",
        "I": "425",
        "J": "446",
        "K": "455",
        "L": "474",
        "M": "495",
        "N": "536",
        "O": "563",
        "P": "568",
        "Q": "591",
        "R": "596",
        "S": "605",
        "T": "662",
        "U": "689",
        "V": "706",
        "W": "717",
        "Y": "722",
        "Z": "727"
    }

    letter_id = mapping.get(letter, "")
    if not letter_id:
        return "No Countries Start With This Letter!"
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//ul[@data-reactid="' + letter_id + '"]'))
        )
        section = driver.find_element(By.XPATH, '//ul[@data-reactid="' + letter_id + '"]')
    except Exception:
        raise SystemExit("Element was not found!")
    country_list = section.find_elements(By.TAG_NAME, "li")
    for country in country_list:
        countries.append(country.text)
    return countries


def country_population(country):
    """Returns the GDP of the country as a dictionary"""

    population = {}
    remove_cookies()

    # Navigates to the country specific page
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//a[text()="' + country + '"]'))
    )
    country_info = driver.find_element(By.XPATH, '//a[text()="' + country + '"]')
    actions = ActionChains(driver)
    actions.move_to_element(country_info).click()
    actions.perform()

    time.sleep(2)
    # Finds the GDP of the country
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//div[@class ="indicator-item__col indicator-item__col--middle"]'))
    )
    col = driver.find_elements(By.XPATH, '//div[@class ="indicator-item__col indicator-item__col--middle"]')
    data = str(col[2].text).replace(",", "").split("\n")[0]
    population[country] = data
    driver.back()

    return population


def remove_cookies():
    """Removes cookies banner and returns control back to calling function"""
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//span[@data-reactid="875"]'))
        )
        cookies = driver.find_element(By.XPATH, '//span[@data-reactid="875"]')
        cookies.click()
    except Exception:
        pass
        # print("cookie button not found or already accepted")
    return


def population(count):
    """Returns the population of each country as a dictionary"""
    counts = int(count)
    countries = all_countries()
    countries = countries[:counts]
    residents = {}
    for country in countries:
        residents[country] = country_population(country).get(country)
        time.sleep(1)
    return residents






# all_countries()
# country_by_letter("X")
# country_gdp("Libya")
# population(5)
