from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from books.models import Ieee
from selenium.common.exceptions import TimeoutException



def run(keyword):
    browser = webdriver.Chrome(executable_path='/home/abdeljalil/Desktop/SearchEngine/chromedriver')
    browser.implicitly_wait(10)
    browser.get('https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText={keyword}&highlight=true&returnType=SEARCH&matchPubs=true&rowsPerPage=100&pageNumber=1&returnFacets=ALL'.format(keyword=str(keyword)))
    elements = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//h2/a"))
    )
    links = [elem.get_attribute('href') for elem in elements]

    print(links)
    #book = Books(title=title.text)
    #book.save()
    #print(title.text)
    for link in links:

        browser.get(link)
        try:
            button_cookies= WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='dismiss cookie message']"))
            )
            button_cookies.click()
        except TimeoutException:
            pass
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        abstract = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//xpl-document-abstract/section/div[3]/div/div)[1]/div/div"))
        )
        published_date = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='LayoutWrapper']//xpl-document-details//xpl-document-abstract/section/div[3]/div[3]/div[1]/div[1]"))
        )
        published_by = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@id='LayoutWrapper']//xpl-publisher/span/span/span)[1]/span[2]"))
        )
        title = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1/span"))
        )
        books=Ieee(title=title.text,abstract=abstract.text,published_by=published_by.text,published_date=published_date.text)
        books.save()
    time.sleep(10)
    #print(browser.page_source)
